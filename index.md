# Files Examples

[gimmick:ForkMeOnGitHub (position: 'right', color: 'darkblue') ](http://www.github.com/thethales/File-Examples)

![Files Examples Horizontal](meta-files/img/FilesExamplesLogoAlternative.png)


Note: This is the file index containing the complete dataset of file examples.
The dataset is also avaliable as a JSON file [here](./meta-files/file-examples.json)

# Index of File Examples

This repository can be defined as:
- A collection of file examples of different formats.
- Samples of files and structures for everyday use.
- A compendium of links of sample files throughout the internet.

The general ideia, is to provide an index of materials for those situations in software development or design where you might need to do some unit testing with real world files.

Below the files are listed by _category_ and _type/context_.





## Archive File Format


### 7Z

7z is a compressed archive file format that supports several different data compression, encryption and pre-processing algorithms. The 7z format initially appeared as implemented by the 7-Zip archiver. The 7-Zip program is publicly available under the terms of the GNU Lesser General Public License. See more at [7z](https://en.wikipedia.org/wiki/7z)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A ```7z``` archive of the Wikipedia.org homepage HTML file|[WikipediaHomePage.7z](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/7Z/WikipediaHomePage.7z)|WikipediaHomePage.7z|52.47 KB||

### GZ

gzip is a file format and a software application used for file compression and decompression. The program was created by Jean-loup Gailly and Mark Adler as a free software replacement for the compress program used in early Unix systems. See more at [gzip](https://en.wikipedia.org/wiki/Gzip)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A gzip archive of the HTML version of the page Wikipedia.org|[Wikipedia.html.gz](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/GZ/Wikipedia.html.gz)|Wikipedia.html.gz|56.4 KB||

### ISO

An optical disc image (or ISO image, from the ISO 9660 file system used with CD-ROM media) is a disk image that contains everything that would be written to an optical disc, disk sector by disc sector, including the optical disc file system. See more at [ISO](https://en.wikipedia.org/wiki/Optical_disc_image)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|An iso image of a CD-ROM containing a copy of wikipedi.org HTML page inside one folder|[wikipedia-org-one-page.iso](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/ISO/wikipedia-org-one-page.iso)|wikipedia-org-one-page.iso|216.0 KB||

### TAR

In computing, tar is a computer software utility for collecting many files into one archive file, often referred to as a tarball, for distribution or backup purposes A tar archive consists of a series of file objects, each file object includes any file data, and is preceded by a 512-byte header record. The file data is written unaltered except that its length is rounded up to a multiple of 512 bytes. See more at [tar](https://en.wikipedia.org/wiki/Tar_(computing))

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A tar archive containing two files: the HTML versions of the Wikipedia.org and the page www.isitchristmas.com|[Wikipedia.tar](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/TAR/Wikipedia.tar)|Wikipedia.tar|168.0 KB||

### WARC

This format is used especifically for archiving ```web-crawls```, and is a revision of the [Internet Archives ARC File Format](https://www.loc.gov/preservation/digital/formats/fdd/fdd000235.shtml), specifying a method for combining multiple digital resources into an aggregate archive file together with related information.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|One page WARC archive of the Wikipedia.org homepage|[WikipediaOrg-20201212031238412.warc](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/WARC/WikipediaOrg-20201212031238412.warc)|WikipediaOrg-20201212031238412.warc|421.33 KB||

### ZIM

The ZIM file format is an open file format that stores wiki content for offline usage. Its primary focus is the contents of Wikipedia and other Wikimedia projects. The format allows for the compression of articles, features a full-text search index and native category and image handling similar to MediaWiki, and the entire file is easily indexable and readable using a program like Kiwix â€“ unlike native Wikipedia XML database dumps. ([source](https://en.wikipedia.org/wiki/ZIM_(file_format)))  the Kwix open source project offer a collection of ZIM archive [here](https://download.kiwix.org/zim/)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A zim archive containing every book from the english Open Source Collection of the Gutenberg Project (hosted by Kiwix)|[gutenberg_en_all_2020-12.zim.url](https://download.kiwix.org/zim/gutenberg/gutenberg_en_all_2020-12.zim)|gutenberg_en_all_2020-12.zim.url|61GB|2020-12|
|TOP 100 Articles from Wikipedia EN-US zim file, hosted by Kiwix|[wikipedia_en_100_2020-10.zim.url](https://download.kiwix.org/zim/wikipedia/wikipedia_en_100_2020-10.zim)|wikipedia_en_100_2020-10.zim.url|304M|2020-10|
|Every page and picture from Wikipedia EN-US hosted by Kiwix|[wikipedia_en_all_maxi_2020-11.zim.url](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2020-11.zim)|wikipedia_en_all_maxi_2020-11.zim.url|94GB|2020-11|
|A zim archive containing every page from Wikipedia EN-US without pictures (hosted by Kiwix)|[wikipedia_en_all_nopic_2020-10.zim.url](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_nopic_2020-10.zim)|wikipedia_en_all_nopic_2020-10.zim.url|39GB|2020-10|

### ZIP

ZIP is an archive file format that supports lossless data compression. A ZIP file may contain one or more files or directories that may have been compressed.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A zip archive of the HTML version of the page Wikipedia.org|[WikipediaOrg.zip](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/ZIP/WikipediaOrg.zip)|WikipediaOrg.zip|56.52 KB|ZIP|

## Programming Languages


### MAKEFILE | AM

```Makefile.am``` is a programmer-defined file and is used by ```automake``` to generate the Makefile.in file (the .am stands for automake). ```GNU Automake``` is a tool for automatically generating Makefile.in files compliant with the GNU Coding Standards ([See more](https://www.gnu.org/software/automake/)). This software is part of [Autoconf](https://www.gnu.org/software/autoconf/autoconf.html) wich is an extensible package of M4 macros that produce shell scripts to automatically configure software source code packages. These scripts can adapt the packages to many kinds of UNIX-like systems without manual user intervention. Autoconf creates a configuration script for a package from a template file that lists the operating system features that the package can use, in the form of M4 macro calls.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Makefile for HTTrack|[Makefile.am](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/AM/Makefile.am)|Makefile.am|196.0 B||

### C

```C``` is the default extension for the [C Programming Language](https://en.wikipedia.org/wiki/C_(programming_language). These are text files, that later are compiled into machine code by the C compiler.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|[HTTrack](https://www.httrack.com/) library example .c file, distributed under the GNU General Public License, Copyright (C) Xavier Roche and other contributors |[example.c](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/C/example.c)|example.c|7.65 KB||

### PHP



|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple PHP file that outputs a option box|[PHP-OptionSelect.php](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PHP/PHP-OptionSelect.php)|PHP-OptionSelect.php|327.0 B||

## Video


### BIK | BINK

Bink Video is a proprietary file format (extensions .bik and .bk2) for video developed by RAD Game Tools. It has been primarily used for full-motion video sequences in video games, and has been used in games for Windows, Mac OS, Xbox 360, Xbox, GameCube, Wii, PlayStation 3, PlayStation 2, Dreamcast, Nintendo DS, and PSP. See more at [Bink Video](https://en.wikipedia.org/wiki/Bink_Video)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|The Sierra Trademark presentation from a classic 2000's CD-ROM|[Sierra_Logo.bik](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/BIK/Sierra_Logo.bik)|Sierra_Logo.bik|3.91 MB||

### MP4

MPEG-4 Part 14 or MP4 is a digital multimedia container format most commonly used to store video and audio, but it can also be used to store other data such as subtitles and still images. See more [here](https://en.wikipedia.org/wiki/MPEG-4_Part_14)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|The sample introduction video from the [Nextcloud](https://nextcloud.com/) opensource platform]|[Nextcloud intro.mp4](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/MP4/Nextcloud intro.mp4)|Nextcloud intro.mp4|3.78 MB||

## 3D Modeling


### BLEND | Blender

```.blend``` is the dafult file system for [Blender](https://www.blender.org/) and can pack multiple scenes into a single file. The best place to find blender sample files is at [blender.org/download/demo-files/](https://www.blender.org/download/demo-files/) though they are offered in ```.zip``` containers. Below some independent samples are listed.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple 535kb file containing the default blender objet, _the cube_|[cube.blend](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/BLEND/cube.blend copy.backup)|cube.blend|135.0 B|2.82|
|A simple 535kb file containing the default blender objet, _the cube_|[cube.blend](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/BLEND/cube.blend)|cube.blend|544.47 KB|2.82|

### FBX

```.fbx``` (Filmbox) is a proprietary file format owned by Autodesk since 2006. It is currently one of the main 3D exchange formats as used by many 3D tools[Â¹](https://code.blender.org/2013/08/fbx-binary-file-format-specification/) [Â²](https://en.wikipedia.org/wiki/FBX). FBX has a text based (ascii) and a binary version. There's no known public documentation avaliable, notes on the innerworkings of the format are provided in the following links:
- Blender Foundation, FBX Text-Based and Binary File Structure: [Original post](https://code.blender.org/2013/08/fbx-binary-file-format-specification/) | [Archive.org](http://web.archive.org/web/20200927125238/https://code.blender.org/2013/08/fbx-binary-file-format-specification/)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple 3D cube exported as FBX by Blender 2.82|[cube.fbx](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/FBX/cube.fbx)|cube.fbx|25.7 KB|Kaydara FBX Binary|

### X3D

X3D is a royalty-free ISO/IEC standard for declaratively representing 3D computer graphics. File format support includes XML, ClassicVRML, Compressed Binary Encoding (CBE) and a draft JSON encoding. See more at [x3d](https://en.wikipedia.org/wiki/X3D)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple file containing the default blender objet, _the cube_, exported on Blender 2.92|[cube.x3d](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/X3D/cube.x3d)|cube.x3d|3.59 KB||

## Documents


### DOC

```.doc``` and ```.docx``` are the formats of files created by [Microsoft Word](https://en.wikipedia.org/wiki/Microsoft_Word)
``` Mime Types: application/doc application/ms-doc application/msword ``` 

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
| One Page Document of [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)|[DOC_LoremIpsum_OnePage.docx](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/DOC/DOC_LoremIpsum_OnePage.docx)|DOC_LoremIpsum_OnePage.docx|8.81 KB||

### GEDCOM

 A plain text file containing genealogical information about individuals, and metadata linking these records together.  This data model is based on the nuclear family and the individual. This contrasts with evidence-based models, where data is structured to reflect the supporting evidence. In the GEDCOM lineage-linked data model, all data is structured to reflect the believed reality, that is, actual (or hypothesized) nuclear families and individuals. [Source](https://en.wikipedia.org/wiki/GEDCOM)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A Sample file generated on Ancestry.com containing a simple family structure.|[Surname Family Tree.ged](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/GEDCOM/Surname Family Tree.ged)|Surname Family Tree.ged|979.0 B|5.5|

### HTML

```.html``` is the extension for Hypertext Markup Language files, wich are the standard markup language for documents designed to be displayed in a web browser. Every web page on the web build based on html

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple HTML page listing some Lorem Ipsum paragraphs|[HTMLLoremIpsumOnePage.html](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/HTML/HTMLLoremIpsumOnePage.html)|HTMLLoremIpsumOnePage.html|10.72 KB||
|A slimmed version of the sample Lorem Ipsum HTML page.|[HTMLLoremIpsumOnePage.min.html](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/HTML/HTMLLoremIpsumOnePage.min.html)|HTMLLoremIpsumOnePage.min.html|6.83 KB||

### PDF

The Portable Document Format (PDF) is a file format [developed](https://en.wikipedia.org/wiki/PDF) to present documents independent of hardware, software and operating system. This format is widely used and has several versions (as of Oct. 2020, 7 revisions in total). See the [ISO 32000-1:2008](https://www.iso.org/standard/51502.html) for PDF especification.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Human Rights Declaration PT-BR version|[Declaração_Universal_Direitos_Humanos.pdf](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PDF/Declaração_Universal_Direitos_Humanos.pdf)|Declaração_Universal_Direitos_Humanos.pdf|48.89 KB|1.5|
|One line PDF|[PDF_HelloWorld_OneLine_1.5.pdf](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PDF/PDF_HelloWorld_OneLine_1.5.pdf)|PDF_HelloWorld_OneLine_1.5.pdf|10.39 KB|1.5|
|One Page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)  formated article|[PDF_LoremIpsum_OnePage_1.5.pdf](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PDF/PDF_LoremIpsum_OnePage_1.5.pdf)|PDF_LoremIpsum_OnePage_1.5.pdf|36.64 KB|1.5|
| Two page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) document|[PDF_LoremIpsum_TwoPages_1.4.pdf](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PDF/PDF_LoremIpsum_TwoPages_1.4.pdf)|PDF_LoremIpsum_TwoPages_1.4.pdf|44.55 KB|1.4|
|Two page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) document|[PDF_LoremIpsum_TwoPages_1.5.pdf](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PDF/PDF_LoremIpsum_TwoPages_1.5.pdf)|PDF_LoremIpsum_TwoPages_1.5.pdf|41.93 KB|1.5|

### RTF

The Rich Text Format [RTF](https://en.wikipedia.org/wiki/Rich_Text_Format) is a proprietary document file format with published specification developed by Microsoft Corporation, and is used for word processing.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|DaVinci Resolve 17 Readme File|[DavinceResolve17_ReadMe.rtf](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/RTF/DavinceResolve17_ReadMe.rtf)|DavinceResolve17_ReadMe.rtf|21.51 KB|17|

### TXT

A _text-file_ is one  of the most simple file structures, is structured as a sequence of lines 

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|59641 Digitis of Pi|[TXT_DigitsofPi.txt](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/TXT/TXT_DigitsofPi.txt)|TXT_DigitsofPi.txt|58.25 KB||
| 3330 characters of Lorem Ipsum|[TXT_LoremIpsum.txt](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/TXT/TXT_LoremIpsum.txt)|TXT_LoremIpsum.txt|3.25 KB|Latin|
|A Thousand Words List EN-US  by [Eric Price](https://www.cs.utexas.edu/~ecprice/). Original source avaliable [here](http://www.mit.edu/~ecprice/wordlist.10000)|[TXT_wordlist_ENUS_10000.txt](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/TXT/TXT_wordlist_ENUS_10000.txt)|TXT_wordlist_ENUS_10000.txt|74.1 KB|EN-US|

## Ebook


### EPUB

```.epub``` is a container for digital publications. Widely used for e-book distribution.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|One page e-book document of the [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)|[EPUB_LoremIpsum_OnePage.epub](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/EPUB/EPUB_LoremIpsum_OnePage.epub)|EPUB_LoremIpsum_OnePage.epub|3.75 KB||

### MOBI

```.mobi``` is a container for digital publications on the [Kindle](https://en.wikipedia.org/wiki/Amazon_Kindle) electronicreader ecosystem

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Ebook Dracula by Bram Stoker hosted on Project Gutenberg, this version contains no images|[Dracula by Bram Stoker(NoImages).url](http://www.gutenberg.org/ebooks/345.kindle.noimages)|Dracula by Bram Stoker(NoImages).url|Unavailable||
|Ebook Dracula by Bram Stoker hosted on Project Gutenberg|[Dracula by Bram Stoker(WithImages) copy.url](http://www.gutenberg.org/ebooks/345.kindle.images)|Dracula by Bram Stoker(WithImages) copy.url|Unavailable||

## Configuration Files


### INF

```.inf``` or Setup Information file is a plain-text file used by Microsoft Windows for the installation of software and drivers.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|```autorun.inf``` is a common file found in CD-ROMs for describing the procedures to auto launch the CD contents |[autorun.inf](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/INF/autorun.inf)|autorun.inf|41.0 B||

### INI

```.ini``` files are used by applications and the Windows operating system for storing initialization parameters. The information is stored in associative arrays, with a key and a value, as such: ``` [section] name=value ; comment text ```

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|The application information file for the portable version of CPU-Z, [distributed by PortableApps.com](https://portableapps.com/apps/utilities/cpu-z-portable)|[appinfo.ini](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/INI/appinfo.ini)|appinfo.ini|463.0 B||
|PortableApps Installer license.ini|[license.ini](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/INI/license.ini)|license.ini|44.0 B||
|A [Install Shield](https://en.wikipedia.org/wiki/InstallShield) setup file from the LS-USBMX 1/2/3 Steering Wheel W/Vibration driver CD-ROM|[setup.ini](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/INI/setup.ini)|setup.ini|358.0 B||
|A windows ```.ini``` file used by the OS to store information about the arrangement of a Windows folder.|[windows-desktop.ini](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/INI/windows-desktop.ini)|windows-desktop.ini|249.0 B||

### PP3 | RawTherapee

The ```.pp3```file is a text file of associative arrays used to store what edits you made to your photo on the [RawTherapee](https://rawtherapee.com/) photo editor

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A Sample file generatd on [RawTherapee](https://rawtherapee.com/) version 5.8|[IMG_8181.CR2.pp3](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PP3/IMG_8181.CR2.pp3)|IMG_8181.CR2.pp3|12.17 KB|346|

## Images


### JPG

JPG is the extension used in image files compressed using the [JPEG method](https://en.wikipedia.org/wiki/JPEG). The images produced with this method are [_lossy_](https://en.wikipedia.org/wiki/Lossy_compression), there are multiple possible levels of quality, below the list includes some quality options.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Blank JPG Color Black, Quality 100%, Size: 1920x1080|[JPG_Black_100_1920x1080.jpg](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/JPG/JPG_Black_100_1920x1080.jpg)|JPG_Black_100_1920x1080.jpg|24.01 KB||
|Blank JPG Color Black, Quality 30%, Size: 1920x1080|[JPG_Black_30_1920x1080.jpg](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/JPG/JPG_Black_30_1920x1080.jpg)|JPG_Black_30_1920x1080.jpg|12.23 KB||
|Blank JPG Color Black, Quality 70%, Size: 1920x1080|[JPG_Black_70_1920x1080.jpg](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/JPG/JPG_Black_70_1920x1080.jpg)|JPG_Black_70_1920x1080.jpg|12.23 KB||
|Blank JPG Color White, Quality 100%, Size: 1920x1080|[JPG_BlankWhite_100_1920x1080.jpg](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/JPG/JPG_BlankWhite_100_1920x1080.jpg)|JPG_BlankWhite_100_1920x1080.jpg|24.01 KB||
|Blank JPG Color White, Quality 30%, Size: 1920x1080|[JPG_BlankWhite_30_1920x1080.jpg](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/JPG/JPG_BlankWhite_30_1920x1080.jpg)|JPG_BlankWhite_30_1920x1080.jpg|12.23 KB||
|Blank JPG Color White, Quality 70%, Size: 1920x1080|[JPG_BlankWhite_70_1920x1080.jpg](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/JPG/JPG_BlankWhite_70_1920x1080.jpg)|JPG_BlankWhite_70_1920x1080.jpg|12.23 KB||

### PNG

The Portable Network Graphics [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) is a raster-graphics file format that supports lossless data compression. 

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Blank PNG Color Black, Size: 1920x1080|[PNG_Black_1920x1080.png](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PNG/PNG_Black_1920x1080.png)|PNG_Black_1920x1080.png|381.0 B||
|Blank PNG Color White, Size: 1920x1080|[PNG_Blank_White_1920x1080.png](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/PNG/PNG_Blank_White_1920x1080.png)|PNG_Blank_White_1920x1080.png|381.0 B||

## Shortcut


### URL

A URL file is a shortcut file referenced by web browsers. It contains a web URL and may also store a reference to the favicon.ico icon file, which is displayed as the icon for the shortcut file. Creting an ```.url``` file on Windows is quite simple, simply drag the URL address from your browser window onto your desktop. ( On a Mac, that action will create a ```webloc```file).

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A sample shortcut file poiting to www.google.com|[google.url](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/URL/google.url)|google.url|55.0 B||

## WINDOWS


### VersionInfo

```VersionInfo```  is a text file used by windows 32bit applications that contains version information. This information is language and code page independent. And mostly describes the product, author, release, copyright, iternal names, among many others attributes. The specification is avaliable [here](https://docs.microsoft.com/pt-br/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo?redirectedfrom=MSDN)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|[PythonUSBWebServer](https://github.com/thethales/PythonUSBWebServer) versioninfo file|[VERSIONINFO_PYTHOUSBWEBSERVER](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/VERSIONINFO/VERSIONINFO_PYTHOUSBWEBSERVER)|VERSIONINFO_PYTHOUSBWEBSERVER|1.41 KB||
|[Apache Software Foundation SVN](https://subversion.apache.org/) version info file|[VERSIONINFO_SVN](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/VERSIONINFO/VERSIONINFO_SVN)|VERSIONINFO_SVN|1.39 KB||

## XML


### XMP | Darktable

```.xmp``` the so-called _sidecars files_, are ```.xml``` files used by [DarkTable](https://www.darktable.org/) a non-destructive image editor, to store information about the images as well as the full editing history without touching the original raw files. For a given source image, multiple editing versions, called duplicates, can co-exist, sharing the same input (raw) data but each having their own metadata, tags and history stack. Each duplicate is represented by a separate XMP sidecar file with a filename constructed in the form _<basename>_nn.<extension>.xmp_, where nn represents the (minimum two-digit) version number of that edit. Information for the initial edit â€“ the _duplicate_ with version number zero â€“ is stored in the sidecar file _<basename>.<extension>.xmp_.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A Blank ```.xmp``` from a ```.cr2``` raw file containing Adobe Color Presets|[IMG_8366.CR2.xmp](https://raw.githubusercontent.com/thethales/File-Examples/main//file-examples/XMP/IMG_8366.CR2.xmp)|IMG_8366.CR2.xmp|975.0 B||
