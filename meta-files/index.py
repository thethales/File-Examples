import os
import yaml
import json
import shutil 
import common

from collections import OrderedDict

from markdown import Markdown

#Script Local Parameters
params = common.getLocalParameters()

def exportJsonToFile(json_object:dict):
    """
    Creates a files at the default Output location, see the ´params´ for fullpath
    
    Parameters
    ----------
        json_object : dict
            JSON Object

    """
    
    f = open(params['json_output']['output_path'], "w")
    f.write(json.dumps(json_object))
    f.close

    if params['json_output']['pretty_print_path'] != '':
        f = open(params['json_output']['pretty_print_path'] , "w")
        f.write(json.dumps(json_object,indent=4, sort_keys=True))
        f.close



def getDirectoryInfo(dump_to_json_file:bool):
    """
    Creates a listing of the entire directory organized by category.
    The metadata listing is based on the .yml files
    
    Parameters
    ----------
        dump_to_json_file : bool
            If True, this function will also dump the computed information into a default json file

    Returns
    -------
        dict
            A dict containing the entries

    """    
    json_content = {}
    parent_folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_examples_directory = parent_folder + params['file_examples_directory']

    for root, dirs, files in os.walk(file_examples_directory):
        for directory in dirs:
            
            #Get Directory BaseInfo from file
            try:
                yml_file = open(os.path.join(root,directory,params['dir_metadata_fileName']))
            except:
                common.print_verbose(directory + ' - ' + 'directory lacks configuration file, skipping ...')
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
                        "size": '0' if info["size"] == None else info["size"],
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
        exportJsonToFile(json_content)

    return json_content


def buildIndex():
    """
        Rebuilds the File Examples human readable index (index.md) with theproject JSON file specified at the parameters file (parameters.yml)
    """

    dest = shutil.copyfile(params['index_template_file'], params['index_output_directory']) 
    directory_listing = getDirectoryInfo(True)
    f = open(dest, "a")
    for category in directory_listing:
        f.write(Markdown.lineBreak())
        category_header = category if (category != '') else params['placeholders']['unspecified_category_name']
        f.write(Markdown.header(2, category_header ))
        f.write(Markdown.lineBreak())

        for item in directory_listing[category]:
            f.write(Markdown.lineBreak())
            f.write(Markdown.header(3,item['filetype']))
            f.write(Markdown.lineBreak())
            f.write(item['description'])
            f.write(Markdown.lineBreak())
            f.write(Markdown.lineBreak())
            f.write(Markdown.tableHeader(item['file_examples']))
            f.write(Markdown.tableLines(item['file_examples']))
    f.close()

    return