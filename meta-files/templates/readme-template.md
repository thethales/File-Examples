# File-Examples
<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">

![Files Examples Horizontal](meta-files/img/FilesExamplesLogoAlternative.png)

This repository can be defined as:
- A collection of file examples of different formats.
- Samples of files and structures for everyday use.
- A compendium of links for sample files troughout the internet.

The general ideia, is providing material for those situations in software development or design where you might need to do some unit testing while manipulating real world files.

An experimental webpage is avaliable at: https://thethales.github.io/File-Examples/


# How it works

![Files Examples Horizontal](./meta-files/img/diagram.png)

The files are organized in directories named after either their extensions or their context (still working on that). Each folder in the entire directory, is populated with  the file samples and their respectives ```.yml``` files, representing their metadata.

The ```directory.yml``` file, describes the folder metadata and contains ilustratory info, such as, the headers and descriptions that later will be put together in the ```README.ME```.

The ```README.ME``` file is dynamically built from a Python [script](./meta-files/run_updateReadmeFile.py), that amalgamates every metadata file into a single document. While the _metadata .yml files_ themselves are updated and created by another _Python_ [script](./meta-files/run_updateMetadata.py).

The resulting _summary_ of files is presented below. For the specific inner workings consult the [docs section](./meta-files/docs), where the everything is describe in detail.

# Summary

