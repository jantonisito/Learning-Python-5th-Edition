This is the "Learning Python 5th Edition" book examples package. 
Release 1.0, June 18, 2013.

----

The book example files are in the \code directory (folder);
it corresponds to "C:\code" in the book's example listings.

For unlabeled code and code run interactively in the book, 
either type manually, or cut-and-paste from an ebook copy (*).

Some examples that evolve may be given here in their final form 
only; enter earlier versions' code manually as needed or desired.

Copying is convenient, but be sure to type some code yourself 
too; it's an important part of learning a language's syntax. 

The \__admin__ directory here has various packaging tools and 
logs, borrowed from the book "Programming Python 4th Edition".
They were written initially for Python 3.X only, and may serve
as additional self-study examples.

----

(*) Ebook code hints: on Windows, using the open source "calibre"
reader on the EPUB file seems to handle whitespace well in 
cut-and-paste code.  Other combinations may work too, but Adobe 
Reader does not retain formatting for code copied from the PDF, 
and Adobe Digital Editions seems to lose line breaks (today).

Also note that some characters may have been altered by book
production: if you have trouble saving pasted code as ASCII 
text, you may need to delete and retype one or more "-" dashes.

See O'Reilly for ebook bundles, and for more ideas, including 
Firefox EPUB support, see the Web at large and: 
    http://support.safaribooksonline.com/view?id=1168

----

UPDATE May 2020: the prior June 2013 zipfile of this package started
failing to unzip with Finder clicks on Mac OS Catalina for unknown 
reasons (with an "Error 22").  This looks like an archive-manager bug
in the latest Mac OS; the zip was created some time ago on Windows
with unknown tools, but it unzips fine in other tools today (more at 
thread https://discussions.apple.com/thread/250741052).  It happens; 
in computing, if you wait long enough, things break...

To fix, this package was simply unzipped and rezipped with the more 
recent ziptools program (see learning-python.com/ziptools.html), and
now unzips correctly again on Mac OS with Finder clicks.

If you encounter other failures, please use ziptools' portable 
zip-extract.py to unzip this package with a command line similar 
to this ($Z is the folder where you've unzipped ziptools; see 
ziptools' docs for more details): 

  $ py3 $Z/zip-extract.py lp5e-code-1.0-may2020.zip . -permissions

This creates an lp5e-code-1.0-may2020/ subfolder in the folder
where the command is run.  For reference, the new zipfile for 
this package was created like this:

  $ py3 $Z/zip-create.py lp5e-code-1.0-may2020.zip lp5e-code-1.0-may2020 -skipcruft

There are NO CONTENT CHANGES in the new zip, apart from this note,
and the minor addition of an alternative for one book example 
(reloadall3-alts.py) hashed out recently on the errata page
(oreilly.com/catalog/errata.csp?isbn=0636920028154&order=date).
There is also a full log of the rezip process in __admin__/.
