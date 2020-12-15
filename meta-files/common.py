
import os
import yaml

#Script Local Parameters
config_file  = open("./meta-files/parameters.yml")
params = yaml.load(config_file, Loader=yaml.FullLoader)


def getLocalParameters():
    """
        Loads the configuration parameters from the parameters file
    """
    try:
        config_file  = open("./meta-files/parameters.yml")
        params = yaml.load(config_file, Loader=yaml.FullLoader)
        return params
    except:
        raise ValueError("Unable to read or parse the system's parameters file")
    

#Consider a better name for this function ... 🤔
def print_verbose(message:str):
    """
        Outputs message to console if allowed in the key verbose at the parameters.yml files
    """
    if params['verbose']:
        print(message)
    return

