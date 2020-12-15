# File-Examples

![Files Examples Horizontal](meta-files/img/FilesExamplesLogoAlternative.png)

This repository can be defined as:
- A collection of file examples of different formats.
- Samples of files and structures for everyday use.
- A compendium of links of sample files throughout the internet.

The general ideia, is to provide an index of materials for those situations in software development or design where you might need to do some unit testing with real world files.
And keep said files in a reachable and easy to maitain repository, that does not require complicated databases.

To read the ```Index```, have a look at the [webpage](https://thethales.github.io/File-Examples/), the machine readable [JSON](./meta-files/file-examples.json), or the classy markdown document [here](/index.md)

# How it works

![Files Examples Horizontal](./meta-files/img/diagram.png)

The files are organized in directories named after either their extensions or their context inside the folder ```files-example```. Each subfolder, is populated with the file samples and their respectives ```.yml``` files, representing their metadata.

The ```directory.yml``` file, describes the folder metadata and contains ilustratory info, such as, the headers and descriptions that later will be put together in the ```index.md```, which is the human readable version of the this project's index of file examples.

The ```index.md``` file is dynamically built by a Python [script](./meta-files/run.py), that amalgamates every metadata file into a single document. While updating or creating the _metadata .yml files_ themselves (when needed).

The resulting _summary_  of files is presented [here](/index.md). For the specific inner workings consult the [docs section](./meta-files/docs/general_information.md), where everything is describe in detail.

# The Index

Ways of acessing the index of file examples:

- As a Markdown file easily acessible here: [Index of Files Examples](/index.md)
- As a machine readable JSON file, avaliable here: [Index of Files Examples](./meta-files/file-examples.json)
- As an experimental webpage hosted with love by Github Pages https://thethales.github.io/File-Examples/

# Roadmap

- ~~Reenable support for external links for files~~ ✔️
- Update docs
- Update Visuals
- Query JSON for specific file types
- Add Issue Templates
- Add VirusTotal Hashes


