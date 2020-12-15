# The Indexer

This project is somewhat automated, all file samples are indexed for easy of access. 

The index of example files is dynamically built by a Python [script](./meta-files/run.py) that amalgamates every avaliable metadata file into a single document, while updating or creating said _metadata files_ themselves when needed.

The indexer _per se_ is the aforementioned script, that outputs human readable form ([Markdown](./index.md)) and a machine readable [JSON file](./meta-files/file-examples.json).

This method, adds good atomicity allowing for a good plasticity in the way the files can be handled in the far future.

# How to add files

**To add new files to the Github repository:**

1. Open a new issue, listing a link to the file and all information you are able to provide, including:
    - Function of the file 
    - Which areas and places the file is commonly used
    - How did you obtain the file

2. The submission will be reviewd and verified at [VirusTotal.com](https://virustotal.com)

**To add new files to your local copy of the project:**

1. Create a new folder into the ```default folder of file examples```, (currently named ```file-examples```), preferebly within the default name scheme of the project

    - ``` Note: The aforementioned folder is customizable and definied as a parameter at the parameters file: [parameters.yml]```

2. Add your files to the folder. 
    - If the file is to be hosted in an external repository have a look a the [External URLs support](./meta-files/docs/general_information.md#External URLs support) section. There you will be instructed to replace your file with a link in text format.
3. Run the script ```run.py```. The script will create all the necessary metada files and prepend known info.
4. Fill in the blanks. Add complementary metadata to the ```.yml``` files avaliable.
    


# External URLs support

To keep the repository within [Github's healthy size limits](https://github.community/t/working-with-large-files-and-repositories/10203) the use of external realiable links is encouraged for anything bigger than 5MB.

For that, the ```Indexer``` supports the usage of ```.url``` [shortcuts](https://en.wikipedia.org/wiki/Shortcut_(computing)), wich are simple text files containing keys poiting to a web address.

How they work:

```
A URL file is a shortcut file referenced by web browsers. It contains
a web URL and may also store a reference to the favicon.ico icon file, which is
displayed as the icon for the shortcut file. Creting an ```.url``` file on Windows
is quite simple, simply drag the URL address from your browser window onto your
desktop.
```

The file structure is pretty simple, and a template is avaliable [here](./meta-files/templates/sample.url)

```inf

[InternetShortcut]
URL=https://www.google.com

```

Once a file with the specified ```.url``` extension is located, the indexer will try to read and place the link as the destination for the file.
Currently the validation of size is unavaliable for those occurrences.
