import os
import yaml
import json
import shutil
import math
import collections



#Script Local Parameters
config_file  = open("./meta-files/parameters.yml")
params = yaml.load(config_file, Loader=yaml.FullLoader)

def convert_size(size_bytes):
   """
        Converts a value in bytes to a friendly human readble version
        By James at https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
   """ 
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def generateYMLInfo():

    excludes = ['.vscode','.git','meta-files']
    root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    

    for dirs in os.listdir(root):
        if dirs not in excludes and os.path.isdir(dirs):
            
            #Create directory.yml if not found
            if not os.path.isfile(os.path.join(dirs,params['dir_metadata_fileName'])):
                shutil.copyfile(params['directory_metadata_template_file'], os.path.join(dirs,params['dir_metadata_fileName'])) 
                      
           
            #Create file.file.yml if not found
            files = os.listdir(os.path.join(root,dirs))
            for file in files:
                
                #Create file.file.yml if not found
                if not file.endswith(".yml") and file != os.path.basename(params['dir_metadata_fileName']) :
                    metadata_file_path = os.path.join(dirs,file+'.yml')
                    if not os.path.isfile(metadata_file_path):
                        shutil.copyfile(params['file_metadata_template_file'], metadata_file_path) 
                
                #Reviews the metadata file adding missing keys for the file.file.yml metadata file
                if file.endswith(".yml") and file != os.path.basename(params['dir_metadata_fileName']) :
                    
                    metadata_file_path = os.path.join(dirs,file)
                    metadata_template = yaml.load(open(params['file_metadata_template_file']), Loader=yaml.FullLoader)
                    metadata = yaml.load(open(metadata_file_path), Loader=yaml.FullLoader)
                
                    base_file_path = os.path.join(dirs,file.replace('.yml',''))
                    try:
                        base_file_size = os.stat(base_file_path).st_size
                    except:
                        base_file_size = 0

                    for item_template in metadata_template:
                        metadata_yml_file = open(metadata_file_path,'w')
                        
                        if item_template not in metadata:
                            metadata[item_template] = ""
                            yaml.safe_dump(metadata, metadata_yml_file)
                            metadata = yaml.load(open(metadata_file_path), Loader=yaml.FullLoader)
                        
                        if metadata['name'] == '':
                            metadata['name'] = os.path.basename(base_file_path)
                        
                        if metadata['link'] == '':
                            metadata['link'] = "[" + os.path.basename(base_file_path) + "]"+"(" + base_file_path + ")"

                        metadata['size'] = convert_size(base_file_size)
                        
                        
                        yaml.safe_dump(metadata, metadata_yml_file)

                #Reviews the metadata file adding missing keys for the directory.yml metadata file
                if file == os.path.basename(params['dir_metadata_fileName']):
                    metadata_file_path = os.path.join(dirs,file)
                    metadata_template = yaml.load(open(params['directory_metadata_template_file']), Loader=yaml.FullLoader)
                    metadata = yaml.load(open(metadata_file_path), Loader=yaml.FullLoader)

                    for item_template in metadata_template:
                        metadata_yml_file = open(metadata_file_path,'w')
                        
                        if item_template not in metadata:
                            metadata[item_template] = ""
                            yaml.safe_dump(metadata, metadata_yml_file)
                            metadata = yaml.load(open(metadata_file_path), Loader=yaml.FullLoader)


                        if metadata['title'] == '':
                            dir_name = os.path.dirname(metadata_file_path)
                            metadata['title'] = dir_name

                        yaml.safe_dump(metadata, metadata_yml_file)

def main():
    generateYMLInfo()


if __name__ == "__main__":  
    main()