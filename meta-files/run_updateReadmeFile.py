import os
import yaml
import json
import shutil 


from markdown import Markdown

#Script Local Parameters
config_file  = open("./meta-files/parameters.yml")
params = yaml.load(config_file, Loader=yaml.FullLoader)

def exportJsonToFile(file_contents:str):
    """
    Creates a files at the default Output location, see the ´params´ for fullpath
    
    Parameters
    ----------
        file_contents : str
            Contents of the file

    """
    f = open(params['output_json_full_file_name'], "w")
    f.write(file_contents)
    f.close



def getDirectoryInfo(dump_to_json_file:bool):
    """
    Creates a listing of the entire directory organized by category.
    The metadata listing is based on the .yml files
    
    Parameters
    ----------
        dump_to_json_file : bool
            If True, this function will also dump the 

    Returns
    -------
        dict
            A dict containing the entries

    """    
    json_content = {}
    
    for root, dirs, files in os.walk("."):
        for directory in dirs:
            
            #Get Directory BaseInfo from file
            try:
                yml_file = open(os.path.join(root,directory,params['dir_metadata_fileName']))
            except:
                if params['verbose']:
                    print(directory + ' - ' + 'directory lacks configuration file, skipping ...')
                continue

            info = yaml.load(yml_file, Loader=yaml.FullLoader)
            temp_file_category = info["category"]
            temp_listOfFiles = []
            temp_directoryInfo = {}
                        
            if  temp_file_category not in json_content:
                json_content[temp_file_category] = [] 

            temp_directoryInfo = {
                "filetype":info["title"],
                "description":info["description"]
            }

            files = os.listdir(os.path.join(root,directory))
     
            for file in files:
                if file.endswith(".yml") and file != os.path.basename(params['dir_metadata_fileName']) :
                    yml_file = open(os.path.join(root,directory,file))
                    info = yaml.load(yml_file, Loader=yaml.FullLoader)

                    temp_fileExampleInfo = {
                        "version":info["version"],
                        "name":info["name"],
                        "size":info["size"],
                        "description":info["description"],
                        "link":info["link"]
                    }

                    temp_listOfFiles.append(temp_fileExampleInfo)

            json_content[temp_file_category].append({
                "filetype":temp_directoryInfo["filetype"],
                "description":temp_directoryInfo["description"],
                "file_examples": temp_listOfFiles
            })
    if dump_to_json_file:            
        exportJsonToFile(json.dumps(json_content))
    return json_content


def generateReadme():

    dest = shutil.copyfile(params['readme_template_file'], params['readme_output_directory']) 
    directory_listing = getDirectoryInfo(True)
    f = open(dest, "a")
    for category in directory_listing:
        f.write(Markdown.lineBreak())
        category_header = category if (category != '') else params['unspecified_category_name']
        f.write(Markdown.header(1, category_header ))
        f.write(Markdown.lineBreak())

        for item in directory_listing[category]:
            f.write(Markdown.lineBreak())
            f.write(Markdown.header(2,item['filetype']))
            f.write(Markdown.lineBreak())
            f.write(item['description'])
            f.write(Markdown.lineBreak())
            f.write(Markdown.lineBreak())
            f.write(Markdown.tableHeader(item['file_examples']))
            f.write(Markdown.tableLines(item['file_examples']))
    f.close()
    return


def main():
    generateReadme()
    



if __name__ == "__main__":
    main()