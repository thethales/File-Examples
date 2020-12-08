# File-Examples
<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">

![Files Examples Horizontal](meta-files/img/logo_fileexamples.jpg)

This repository can be defined as:
- A collection of file examples of different formats.
- Samples of files and structures for everyday use.
- A compendium of links for sample files troughout the internet.

The general ideia, is providing material for those situations in software development or design where you might need to do some unit testing while manipulating real world files.

A experimental webpage is avaliable at: https://thethales.github.io/File-Examples/

# Summary


## 3D Modeling

### BLEND | BLENDER

```.blend``` is the dafult file system for [Blender](https://www.blender.org/) and can pack multiple scenes into a single file.

- [cube.blend](BLEND/cube.blend) a simple 535kb file containing the default blender objet, _the cube_


## Configuration Files

### INF

```.inf``` or Setup Information file is a plain-text file used by Microsoft Windows for the installation of software and drivers.

- ```autorun.inf``` is a common file found in CD-ROMs for describing the procedures to auto launch the CD contents : [autorun.inf](INF/autorun.inf)
  

### INI

```.ini``` files are used by applications and the Windows operating system for storing initialization parameters. The information is stored in associative arrays, with a key and a value, as such:

```
[section]
name=value
; comment text
```
Avaliable ```.ini``` samples:

- [Desktop.ini](INI/windows-desktop.ini) 
- [setup.ini](INI/setup.ini) 


### VersionInfo

```VersionInfo```  is a text file used by windows 32bit applications that contains version information. This information is language and code page independent. And mostly describes the product, author, release, copyright, iternal names, among many others attributes. The specification is avaliable [here](https://docs.microsoft.com/pt-br/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo?redirectedfrom=MSDN)

- [PythonUSBWebServer](https://github.com/thethales/PythonUSBWebServer) version info file: [PythonUSBWebServer](WINDOWS/VERSIONINFO_PYTHOUSBWEBSERVER)
- [Apache Software Foundation SVN](https://subversion.apache.org/) version info file: [VERSIONINFO_SVN](WINDOWS/VERSIONINFO_SVN)

## Documents

### Doc | Microsoft Word

```.doc``` and ```.docx``` are the formats of files created by [Microsoft Word](https://en.wikipedia.org/wiki/Microsoft_Word)

```
Mime Types:
  application/doc
  application/ms-doc
  application/msword
```


- [Lorem Ipsum DOCX File](DOC/DOC_LoremIpsum_OnePage.docx) - One Page Document of [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)


### Epub

```.epub``` is a container for digital publications. Widely used for e-book distribution.

- [Lorem Ipsum EPUB One Page](EPUB/EPUB_LoremIpsum_OnePage.epub) - One page e-book document of the [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)
- [Dracula by Bram Stoker EPUB (No Images)](http://www.gutenberg.org/ebooks/345.epub.noimages)  - A real ebook hosted by Project Gutenberg
- [Dracula by Bram Stoker EPUB (With Images)](http://www.gutenberg.org/ebooks/345.epub.images)  - A real ebook hosted by Project Gutenberg

### Mobi | Kindle

```.mobi``` is a container for digital publications on the [Kindle](https://en.wikipedia.org/wiki/Amazon_Kindle) eletronic reader ecosystem

- [Dracula by Bram Stoker EPUB (No Images)](http://www.gutenberg.org/ebooks/345.kindle.noimages)
- [Dracula by Bram Stoker EPUB (With Images)](http://www.gutenberg.org/ebooks/345.kindle.images)

### HTML

```.html``` is the extension for Hypertext Markup Language files, wich are the standard markup language for documents designed to be displayed in a web browser. 
Every web page on the web build based on html


- [Lorem Ipsum HTML Page](HTML/HTMLLoremIpsumOnePage.html) -  A simple HTML page listing some Lorem Ipsum paragraphs
- [Lorem Ipsum HTML Page Minified](HTML/HTMLLoremIpsumOnePage.min.html) - A slimmed version of the sample Lorem Ipsum HTML page.


### PDF

The Portable Document Format (PDF) is a file format [developed](https://en.wikipedia.org/wiki/PDF) to present documents independent of hardware, software and operating system. This format is widely used and has several versions (as of Oct. 2020, 7 revisions in total). See the [ISO 32000-1:2008](https://www.iso.org/standard/51502.html) for PDF especification.

|PDF Version| Description | Link |
|-------|-------------|------|
|1.5    | One line PDF|[PDF_HelloWorld_OneLine_1.5.pdf](PDF/PDF_HelloWorld_OneLine_1.5.pdf)|
|1.5    | One Page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)  formated article|[PDF_HelloWorld_OneLine_1.5.pdf](PDF/PDF_HelloWorld_OneLine_1.5.pdf)|
|1.4    | Two page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) document| [PDF_LoremIpsum_TwoPages_1.4.pdf](PDF/PDF_LoremIpsum_TwoPages_1.4.pdf)|
|1.5    | Two page [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) document| [PDF_LoremIpsum_TwoPages_1.5.pdf](PDF/PDF_LoremIpsum_TwoPages_1.5.pdf)|


### RTF

The Rich Text Format [RTF](https://en.wikipedia.org/wiki/Rich_Text_Format) is a proprietary document file format with published specification developed by Microsoft Corporation, and is used for word processing.

- [DaVinci Resolve 17 Readme File](RTF/DavinceResolve17_ReadMe.rtf)


### TXT

A _text-file_ is one  of the most simple file structure, is structured as a sequence of lines 

- [Lorem Ipsum TXT](https://github.com/thethales/File-Examples/blob/main/TXT/TXT%20-%20Lorem%20Ipsum.txt)
- [Digits of Pi TXT](https://github.com/thethales/File-Examples/blob/main/TXT/TXT%20-%20Digits%20of%20Pi.txt)


## Images


### JPG

JPG is the extension used in image files compressed using the [JPEG method](https://en.wikipedia.org/wiki/JPEG). The images produced with this method are [_lossy_](https://en.wikipedia.org/wiki/Lossy_compression), there are multiple possible levels of quality, below the list includes some quality options.

- [Blank JPG Color Black, Quality 30%, Size: 1920x1080](JPG/JPG_Black_30_1920x1080.jpg)
- [Blank JPG Color Black, Quality 70%, Size: 1920x1080](JPG/JPG_Black_37_1920x1080.jpg)
- [Blank JPG Color Black, Quality 100%, Size: 1920x1080](JPG/JPG_Black_100_1920x1080.jpg)
- [Blank JPG Color White, Quality 30%, Size: 1920x1080](JPG/JPG_BlankWhite_30_1920x1080.jpg)
- [Blank JPG Color White, Quality 70%, Size: 1920x1080](JPG/JPG_BlankWhite_70_1920x1080.jpg)
- [Blank JPG Color White, Quality 100%, Size: 1920x1080](JPG/JPG_BlankWhite_100_1920x1080.jpg)

### PNG

The Portable Network Graphics [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) is a raster-graphics file format that supports lossless data compression. 

- [Blank PNG Color Black, Size: 1920x1080](https://github.com/thethales/File-Examples/blob/main/PNG/PNG%20-%20Black%20-%201920x1080.png)
- [Blank PNG Color White, Size: 1920x1080](https://github.com/thethales/File-Examples/blob/main/PNG/PNG%20-%20Blank-White%20-%201920x1080.png)

