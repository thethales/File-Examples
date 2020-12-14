# The Indexer

~~This method, though still in construction, adds good atomicity allowing for a wide range of plasticity in the way the files can be handled in the far future
To change the~~

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
