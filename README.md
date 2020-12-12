# File-Examples

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


# Archive File Format


## 7Z

7z is a compressed archive file format that supports several different data compression, encryption and pre-processing algorithms. The 7z format initially appeared as implemented by the 7-Zip archiver. The 7-Zip program is publicly available under the terms of the GNU Lesser General Public License. See more at [7z](https://en.wikipedia.org/wiki/7z)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A 7z archive of a HTML file version of  Wikipedia.org|[Wikipedia.7z](7Z\Wikipedia.7z)|Wikipedia.7z|52.47 KB|LZMA2:192|

## GZ

gzip is a file format and a software application used for file compression and decompression. The program was created by Jean-loup Gailly and Mark Adler as a free software replacement for the compress program used in early Unix systems. See more at [gzip](https://en.wikipedia.org/wiki/Gzip)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A gzip archive of the HTML version of the page Wikipedia.org|[Wikipedia.html.gz](GZ\Wikipedia.html.gz)|Wikipedia.html.gz|56.4 KB||

## TAR

In computing, tar is a computer software utility for collecting many files into one archive file, often referred to as a tarball, for distribution or backup purposes A tar archive consists of a series of file objects, each file object includes any file data, and is preceded by a 512-byte header record. The file data is written unaltered except that its length is rounded up to a multiple of 512 bytes. See more at [tar](https://en.wikipedia.org/wiki/Tar_(computing))

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A tar archive containing two files: the HTML versions of the Wikipedia.org and the page www.isitchristmas.com|[Wikipedia.tar](TAR\Wikipedia.tar)|Wikipedia.tar|168.0 KB||

## WARC

This format is used especifically for archiving ```web-crawls```, and is a revision of the Internet Archives ARC File Format, specifying a method for combining multiple digital resources into an aggregate archive file together with related information.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|One page WARC archive of the Wikipedia.org homepage|[WikipediaOrg-20201212031238412.warc](WARC\WikipediaOrg-20201212031238412.warc)|WikipediaOrg-20201212031238412.warc|421.33 KB||

## ZIP

ZIP is an archive file format that supports lossless data compression. A ZIP file may contain one or more files or directories that may have been compressed.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A zip archive of the HTML version of the page Wikipedia.org|[WikipediaOrg.zip](ZIP\WikipediaOrg.zip)|WikipediaOrg.zip|56.52 KB|ZIP|

# 3D Modeling


## BLEND | Blender

```.blend``` is the dafult file system for [Blender](https://www.blender.org/) and can pack multiple scenes into a single file. The best place to find blender sample files is at [blender.org/download/demo-files/](https://www.blender.org/download/demo-files/) though they are offered in ```.zip``` containers. Below some independent samples are listed.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple 535kb file containing the default blender objet, _the cube_|[cube.blend](BLEND\cube.blend)|cube.blend|135.0 B|2.82|
|A simple 535kb file containing the default blender objet, _the cube_|[cube.blend](BLEND\cube.blend)|cube.blend|544.47 KB|2.82|

## FBX

```.fbx``` (Filmbox) is a proprietary file format owned by Autodesk since 2006. It is currently one of the main 3D exchange formats as used by many 3D tools[¹](https://code.blender.org/2013/08/fbx-binary-file-format-specification/) [²](https://en.wikipedia.org/wiki/FBX). FBX has a text based (ascii) and a binary version. There's no known public documentation avaliable, notes on the innerworkings of the format are provided in the following links:
- Blender Foundation, FBX Text-Based and Binary File Structure: [Original post](https://code.blender.org/2013/08/fbx-binary-file-format-specification/) | [Archive.org](http://web.archive.org/web/20200927125238/https://code.blender.org/2013/08/fbx-binary-file-format-specification/)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple 3D cube exported as FBX by Blender 2.82|[cube.fbx](FBX\cube.fbx)|cube.fbx|25.7 KB|Kaydara FBX Binary|

## X3D

X3D is a royalty-free ISO/IEC standard for declaratively representing 3D computer graphics. File format support includes XML, ClassicVRML, Compressed Binary Encoding (CBE) and a draft JSON encoding. See more at [x3d](https://en.wikipedia.org/wiki/X3D)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple file containing the default blender objet, _the cube_, exported on Blender 2.92|[cube.x3d](X3D\cube.x3d)|cube.x3d|3.59 KB||

# Documents


## DOC

```.doc``` and ```.docx``` are the formats of files created by [Microsoft Word](https://en.wikipedia.org/wiki/Microsoft_Word)
``` Mime Types: application/doc application/ms-doc application/msword ``` 

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
| One Page Document of [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)|[DOC_LoremIpsum_OnePage.docx](DOC\DOC_LoremIpsum_OnePage.docx)|DOC_LoremIpsum_OnePage.docx|8.81 KB||

## HTML

```.html``` is the extension for Hypertext Markup Language files, wich are the standard markup language for documents designed to be displayed in a web browser. Every web page on the web build based on html

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|A simple HTML page listing some Lorem Ipsum paragraphs|[HTMLLoremIpsumOnePage.html](HTML\HTMLLoremIpsumOnePage.html)|HTMLLoremIpsumOnePage.html|10.72 KB||
|A slimmed version of the sample Lorem Ipsum HTML page.|[HTMLLoremIpsumOnePage.min.html](HTML\HTMLLoremIpsumOnePage.min.html)|HTMLLoremIpsumOnePage.min.html|6.83 KB||

## PDF

The Portable Document Format (PDF) is a file format [developed](https://en.wikipedia.org/wiki/PDF) to present documents independent of hardware, software and operating system. This format is widely used and has several versions (as of Oct. 2020, 7 revisions in total). See the [ISO 32000-1:2008](https://www.iso.org/standard/51502.html) for PDF especification.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Human Rights Declaration PT-BR version|[Declara��o_Universal_Direitos_Humanos.pdf](PDF\Declara��o_Universal_Direitos_Humanos.pdf)|Declara��o_Universal_Direitos_Humanos.pdf|48.89 KB|1.5|
|One line PDF|[PDF_HelloWorld_OneLine_1.5.pdf](PDF\PDF_HelloWorld_OneLine_1.5.pdf)|PDF_HelloWorld_OneLine_1.5.pdf|10.39 KB|1.5|
|One Page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)  formated article|[PDF_LoremIpsum_OnePage_1.5.pdf](PDF\PDF_LoremIpsum_OnePage_1.5.pdf)|PDF_LoremIpsum_OnePage_1.5.pdf|36.64 KB|1.5|
| Two page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) document|[PDF_LoremIpsum_TwoPages_1.4.pdf](PDF\PDF_LoremIpsum_TwoPages_1.4.pdf)|PDF_LoremIpsum_TwoPages_1.4.pdf|44.55 KB|1.4|
|Two page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) document|[PDF_LoremIpsum_TwoPages_1.5.pdf](PDF\PDF_LoremIpsum_TwoPages_1.5.pdf)|PDF_LoremIpsum_TwoPages_1.5.pdf|41.93 KB|1.5|

## RTF

The Rich Text Format [RTF](https://en.wikipedia.org/wiki/Rich_Text_Format) is a proprietary document file format with published specification developed by Microsoft Corporation, and is used for word processing.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|DaVinci Resolve 17 Readme File|[DavinceResolve17_ReadMe.rtf](RTF\DavinceResolve17_ReadMe.rtf)|DavinceResolve17_ReadMe.rtf|21.51 KB|17|

## TXT

A _text-file_ is one  of the most simple file structures, is structured as a sequence of lines 

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|59641 Digitis of Pi|[TXT_DigitsofPi.txt](TXT\TXT_DigitsofPi.txt)|TXT_DigitsofPi.txt|58.25 KB||
| 3330 characters of Lorem Ipsum|[TXT_LoremIpsum.txt](TXT\TXT_LoremIpsum.txt)|TXT_LoremIpsum.txt|3.25 KB|Latin|
|A Thousand Words List EN-US  by [Eric Price](https://www.cs.utexas.edu/~ecprice/). Original source avaliable [here](http://www.mit.edu/~ecprice/wordlist.10000)|[TXT_wordlist_ENUS_10000.txt](TXT\TXT_wordlist_ENUS_10000.txt)|TXT_wordlist_ENUS_10000.txt|74.1 KB|EN-US|

# Ebook


## EPUB

```.epub``` is a container for digital publications. Widely used for e-book distribution.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|One page e-book document of the [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)|[EPUB_LoremIpsum_OnePage.epub](EPUB\EPUB_LoremIpsum_OnePage.epub)|EPUB_LoremIpsum_OnePage.epub|3.75 KB||

## MOBI

```.mobi``` is a container for digital publications on the [Kindle](https://en.wikipedia.org/wiki/Amazon_Kindle) electronicreader ecosystem

|
|

# Configuration Files


## INF

```.inf``` or Setup Information file is a plain-text file used by Microsoft Windows for the installation of software and drivers.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|```autorun.inf``` is a common file found in CD-ROMs for describing the procedures to auto launch the CD contents |[autorun.inf](INF\autorun.inf)|autorun.inf|41.0 B||

## INI

```.ini``` files are used by applications and the Windows operating system for storing initialization parameters. The information is stored in associative arrays, with a key and a value, as such: ``` [section] name=value ; comment text ```

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
||[setup.ini](INI\setup.ini)|setup.ini|358.0 B||
||[windows-desktop.ini](INI\windows-desktop.ini)|windows-desktop.ini|249.0 B||

# Images


## JPG

JPG is the extension used in image files compressed using the [JPEG method](https://en.wikipedia.org/wiki/JPEG). The images produced with this method are [_lossy_](https://en.wikipedia.org/wiki/Lossy_compression), there are multiple possible levels of quality, below the list includes some quality options.

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Blank JPG Color Black, Quality 100%, Size: 1920x1080|[JPG_Black_100_1920x1080.jpg](JPG\JPG_Black_100_1920x1080.jpg)|JPG_Black_100_1920x1080.jpg|24.01 KB||
|Blank JPG Color Black, Quality 30%, Size: 1920x1080|[JPG_Black_30_1920x1080.jpg](JPG\JPG_Black_30_1920x1080.jpg)|JPG_Black_30_1920x1080.jpg|12.23 KB||
|Blank JPG Color Black, Quality 70%, Size: 1920x1080|[JPG_Black_70_1920x1080.jpg](JPG\JPG_Black_70_1920x1080.jpg)|JPG_Black_70_1920x1080.jpg|12.23 KB||
|Blank JPG Color White, Quality 100%, Size: 1920x1080|[JPG_BlankWhite_100_1920x1080.jpg](JPG\JPG_BlankWhite_100_1920x1080.jpg)|JPG_BlankWhite_100_1920x1080.jpg|24.01 KB||
|Blank JPG Color White, Quality 30%, Size: 1920x1080|[JPG_BlankWhite_30_1920x1080.jpg](JPG\JPG_BlankWhite_30_1920x1080.jpg)|JPG_BlankWhite_30_1920x1080.jpg|12.23 KB||
|Blank JPG Color White, Quality 70%, Size: 1920x1080|[JPG_BlankWhite_70_1920x1080.jpg](JPG\JPG_BlankWhite_70_1920x1080.jpg)|JPG_BlankWhite_70_1920x1080.jpg|12.23 KB||

## PNG

The Portable Network Graphics [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) is a raster-graphics file format that supports lossless data compression. 

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|Blank PNG Color Black, Size: 1920x1080|[PNG_Black_1920x1080.png](PNG\PNG_Black_1920x1080.png)|PNG_Black_1920x1080.png|381.0 B||
|Blank PNG Color White, Size: 1920x1080|[PNG_Blank_White_1920x1080.png](PNG\PNG_Blank_White_1920x1080.png)|PNG_Blank_White_1920x1080.png|381.0 B||

# Programming Languages


## PHP



|Description|Link|Name|Size|Version|
|----|----|----|----|----|
||[PHP-OptionSelect.php](PHP\PHP-OptionSelect.php)|PHP-OptionSelect.php|327.0 B||

# WINDOWS


## VersionInfo

```VersionInfo```  is a text file used by windows 32bit applications that contains version information. This information is language and code page independent. And mostly describes the product, author, release, copyright, iternal names, among many others attributes. The specification is avaliable [here](https://docs.microsoft.com/pt-br/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo?redirectedfrom=MSDN)

|Description|Link|Name|Size|Version|
|----|----|----|----|----|
|[PythonUSBWebServer](https://github.com/thethales/PythonUSBWebServer) versioninfo file|[VERSIONINFO_PYTHOUSBWEBSERVER](WINDOWS\VERSIONINFO_PYTHOUSBWEBSERVER)|VERSIONINFO_PYTHOUSBWEBSERVER|1.41 KB||
|[Apache Software Foundation SVN](https://subversion.apache.org/) version info file|[VERSIONINFO_SVN](WINDOWS\VERSIONINFO_SVN)|VERSIONINFO_SVN|1.39 KB||

# Unspecified


## 



|Description|Link|Name|Size|Version|
|----|----|----|----|----|
||||||
