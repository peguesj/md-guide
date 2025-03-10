## Command line

You can run PlantUML using the command line.
(See [running](running) for ways to run PlantUML from various other tools and workflows).

The most basic way to run it is:
```
java -jar plantuml.jar file1 file2 file3
```

This will look for ``@startXYZ`` into ``file1``, ``file2`` and ``file3``. For each diagram, a ``.png`` file will be created.

For processing a whole directory, you can use:
```
java -jar plantuml.jar "c:/directory1" "c:/directory2"
```

This command will search for ``@startXYZ`` and ``@endXYZ`` into ``.txt``, ``.tex``, ``.java``, ``.htm``, ``.html``, ``.c``, ``.h``, ``.cpp``, ``.apt``, ``.pu``, ``.puml``, ``.hpp``, ``.hh`` or ``.md`` files of the ``c:/directory1`` and ``c:/directory2`` directories.

Docker images are released as [Github Packages](https://github.com/plantuml/plantuml/pkgs/container/plantuml) and to [Docker Hub](https://hub.docker.com/r/plantuml/plantuml).

```
docker run ghcr.io/plantuml/plantuml
```


## Wildcards

You can also use wildcards :

* For a single character, use ``?``
* For zero or more characters, use ``*``
* For zero or more characters, (including ``/`` or ``\``), use a double ``**``

So to process any ``.cpp`` files in all directories starting by *dummy* :
```
java -jar plantuml.jar "dummy*/*.cpp"
```

And to process any ``.cpp`` files in all directories starting by *dummy*, and theirs subdirectories :
```
java -jar plantuml.jar "dummy*/**.cpp"
```



## Excluded files

You can exlude some files from the process using the ``-x`` option:
```
java -jar plantuml.jar -x "**/common/**" -x "**/test/Test*" "dummy*/**/*.cpp"
```



## Output Directory

You can specify an output directory for all images using the ``-o`` switch:
```
java -jar plantuml.jar -o "c:/outputPng" "c:/directory2"
```

If you recurse into several directory, there is a slight difference if you provide an absolute or a relative path for this output directory:

* An __absolute path__ will ensure that all images are output to a single, specific, directory.


* If you provide a __relative path__ then the images is placed in that directory relative to the location of the **input file**, not the current directory (note: this applies even if the path begins with a ``.``). When Plantuml processes files from multiple directores then the corresponding directory structure is created under the computed output directory.

See [Sources](sources) section "File naming" on how output file names are calculated when you use multiple diagrams per input file.


## Types of Output File

Images for your diagrams can be exported in a variety of different formats. By default the format will be a PNG file but another type can be selected using the following extensions:

| Param name             | Short param name     | Output format | Comment
| ---------------------- | -------------------- | ------------- | ------------------------------------------------------------------------------ |
| ``-tpng``              | ``-png``             | PNG           | Default                                                                        |
| ``-tsvg``              | ``-svg``             | SVG           | Further details can be found [here](svg)                  |
| ``-teps``              | ``-eps``             | EPS           | Further details can be found [here](eps)                  |
| ``-teps:text``         | ``-eps:text``        | EPS           | Keeps EPS text as text  (more details [here](eps)) |
| ``-tpdf``              | ``-pdf``             | PDF           | Further details can be found [here](pdf)                  |
| ``-tvdx``              | ``-vdx``             | VDX           | Microsoft Visio Document                                                       |
| ``-txmi``              | ``-xmi``             | XMI           | Further details can be found [here](xmi)                  |
| ``-tscxml``            | ``-scxml``           | SCXML         |                                                                                |
| ``-thtml``             | ``-html``            | HTML          | Alpha feature: do not use                                                      |
| ``-ttxt``              | ``-txt``             | ATXT          | ASCII art. Further details can be found [here](ascii-art) |
| ``-tutxt``             | ``-utxt``            | UTXT          | ASCII art using Unicode characters                                             |
| ``-tlatex``            | ``-latex``           | LATEX         | Further details can be found [here](latex)                |
| ``-tlatex:nopreamble`` | ``-latex:nopreamble``| LATEX         | Contains no LaTeX preamble creating a document                                 |
| ``-tbraille``          | ``-braille``         | PNG           | Braille image *[Ref. [QA-4752](https://forum.plantuml.net/4752/translate-class-diagram-to-braille)]* |


Example:
```
java -jar plantuml.jar yourdiagram.txt -ttxt
```


## Configuration File

You can also provide a configuration file which will be included before each diagram:
```
java -jar plantuml.jar -config "./config.cfg" dir1
```



## Metadata

After all preprocessing (includes etc), PlantUML saves the diagram's source code in the generated PNG Metadata in the form of [encoded text](text-encoding).
* If you do not want plantuml to save the diagram's source code in the generated PNG Metadata, you can during generation use the option ``-nometadata`` to disable this functionality (To NOT export metadata in PNG/SVG generated files).
* It is possible to retrieve this source with the ``-metadata`` option. This means that the PNG is almost "editable": you can post it on a corporate wiki where you cannot install plugins, and someone in the future can update the diagram by getting the metadata, editing and re-uploading again. Also, the diagram is stand-alone.
* Conversely, the ``-checkmetadata`` option checks whether the target PNG has the same source and if there are no changes, doesn't regenerate the PNG, thus saving all processing time. This allows you to run PlantUML on a whole folder (or tree with the ``-recursive`` option) incrementally.

Sounds like magic! No, merely clever engineering :-)

Example:
```
  java -jar plantuml.jar -metadata diagram.png > diagram.puml
```

Unfortunately this option works only with local files. It doesn't work with ``-pipe`` so you cannot fetch a URL with eg ``curl`` and feed the PNG to PlantUML.

However, the Plantuml [server](server#metadata) has a similar feature, where it can get a PNG from a URL and extract its metadata.


## Exit code

When there are some errors in diagrams the command returns an error (-1) exit code. But even if some diagrams contain some errors, **all** diagrams are generated, which can be time consuming for large project.

You can use the ``-failfast`` flag to change this behavior to stop diagram generations as soon as one error occurs. In that case, some diagrams will be generated, and some will not.

There is also a ``-failfast2`` flag that does a first checking pass. If some error is present, no diagram will be generated at all. In case of error, ``-failfast2`` runs even faster than ``-failfast``, which may be useful for huge project.



## Standard report [stdrpt]

Using the ``-stdrpt`` (standard report)  option, you can change the format of the error output of your PlantUML scripts.

With this option, a different error output of your diagram is possible:
* none: two lines
* ``-stdrpt``: single line
* ``-stdrpt:1``: verbose
*  ``-stdrpt:2``: single line

*[Ref. [Issue#155](https://github.com/plantuml/plantuml/issues/155) and [QA-11805](https://forum.plantuml.net/11805/)]*

Examples, with the bad file `file1.pu`, where `as` is written `aass`:
```
@startuml
participant "Famous Bob" aass Bob
@enduml
```

### Without any option
```
java -jar plantuml.jar file1.pu
```
The error output is:
```
Error line 2 in file: file1.pu
Some diagram description contains errors
```

### -stdrpt option

```
java -jar plantuml.jar -stdrpt file1.pu
```
The error output is:
```
file1.pu:2:error:Syntax Error?
```

### -stdrpt:1 option

```
java -jar plantuml.jar -stdrpt:1 file1.pu
```
The error output is:
```
protocolVersion=1
status=ERROR
lineNumber=2
label=Syntax Error?
Error line 2 in file: file1.pu
Some diagram description contains errors
```

### -stdrpt:2 option (like -stdrpt)
```
java -jar plantuml.jar -stdrpt:2 file1.pu
```
The error output is:
```
file1.pu:2:error:Syntax Error?
```


## Standard Input & Output

Using the ``-pipe`` option, you can easily use PlantUML in your scripts.

With this option, a diagram description is received through standard input and the PNG file is generated to standard output. No file is written on the local file system.

Example:
```
cat somefile.puml | java -jar plantuml.jar -pipe > somefile.png
```

The ``-pipemap`` option can be used to generate PNG map data (hyperlink rectangles) for use in HTML, eg:
```
cat somefile.puml | java -jar plantuml.jar -pipemap > somefile.map
```

The map file looks like this:

```
<map id="plantuml_map" name="plantuml_map">
<area shape="rect" id="id1" href="http://plantuml.com" title="http://plantuml.com"
      alt="" coords="1,8,88,44"/>
</map>
```

Note: Also take a look at ``-pipedelimitor`` and ``-pipeNoStderr`` to implement proper multiplexing of several PNG in a stream (in case the puml file contains multiple diagrams), and error handling.


## Help

You can have a help message by launching :
```
java -jar plantuml.jar -help
```

This will output:
```
Usage: java -jar plantuml.jar [options] -gui
        (to execute the GUI)
    or java -jar plantuml.jar [options] [file/dir] [file/dir] [file/dir]
        (to process files or directories)

You can use the following wildcards in files/dirs:
        *       means any characters but '\'
        ?       one and only one character but '\'
        **      means any characters (used to recurse through directories)

where options include:
    -DVAR1=value                    Set a preprocessing variable as if '!define VAR1 value' were used
    -I\path\to\*.puml               Include files with pattern
    -I\path\to\file                 Include file as if '!include file' were used
    -Ppragma1=value                 Set pragma as if '!pragma pragma1 value' were used
    -Sparam1=value                  Set a skin parameter as if 'skinparam param1 value' were used
    -author[s]                      Print information about PlantUML authors
    -charset xxx                    Use a specific charset (default depends on system settings)
    -checkmetadata                  Skip PNG files that don't need to be regenerated
    -checkonly                      Check the syntax of files without generating images
    -computeurl|-encodeurl          Compute the encoded URL of a PlantUML source file
    -cypher                         Cypher texts of diagrams so that you can share them
    -darkmode                       Use dark mode for diagrams
    -debugsvek                      Generate intermediate svek files
    -decodeurl                      Retrieve the PlantUML source from an encoded URL
    -disablestats                   Disable statistics computation (default)
    -duration                       Print the duration of complete diagrams processing
    -e[x]clude pattern              Exclude files that match the provided pattern
    -enablestats                    Enable statistics computation
    -encodesprite 4|8|16[z] "file"  Encode a sprite at gray level (z for compression) from an image
    -extractstdlib                  Extract PlantUML Standard Library into stdlib folder
    -failfast                       Stop processing as soon as a syntax error in diagram occurs
    -failfast2                      Do a first syntax check before processing files, to fail even faster
    -filedir xxx                    Behave as if the PlantUML source is in this dir (only affects '-pipe' and PicoWeb 'POST /render')
    -filename "file.puml"           Override %filename% variable
    -graphvizdot "exe"              Specify dot executable
    -gui [<input-folder>]           Run the graphical user interface
    -h[elp]                         Display this help message
    -htmlstats                      Output general statistics in file plantuml-stats.html
    -language                       Print the list of PlantUML keywords
    -loopstats                      Continuously print statistics about usage
    -metadata                       Retrieve PlantUML sources from PNG images
    -nbthread N                     Use (N) threads for processing
    -nbthread auto                  Use all process cores for processing
    -noerror                        Skip images when error in diagrams
    -nometadata                     To NOT export metadata in PNG/SVG generated files
    -o[utput] "dir"                 Generate images in the specified directory
    -overwrite                      Allow to overwrite read only files
    -p[ipe]                         Use stdin for PlantUML source and stdout for PNG/SVG/EPS generation
    -picoweb                        Start internal HTTP Server. See https://plantuml.com/picoweb
    -pipeimageindex N               Generate the Nth image with pipe option
    -preproc                        Output preprocessor text of diagrams
    -printfonts                     Print fonts available on your system
    -progress                       Display a textual progress bar in console
    -quiet                          To NOT print error message into the console
    -realtimestats                  Generate statistics on the fly rather than at the end
    -splash                         Display a splash screen with some progress bar
    -stdlib                         Print standard library info
    -syntax                         Report any syntax error from standard input without generating images
    -teps                           Generate images using EPS format, rendering text as outlines
    -teps:text                      Generate images using EPS format, preserving text as text
    -testdot                        Test the installation of graphviz
    -theme xxx                      Use a specific theme
    -thtml                          Generate HTML file for class diagram (experimental, do not use yet)
    -timeout N                      Processing timeout in (N) seconds. Defaults to 15 minutes (900 seconds).
    -tlatex                         Generate images using LaTeX/Tikz format
    -tlatex:nopreamble              Generate images using LaTeX/Tikz format without preamble
    -tpdf                           Generate images using PDF format
    -tpng                           Generate images using PNG format (default)
    -tscxml                         Generate SCXML file for state diagram
    -tsvg                           Generate images using SVG format
    -ttxt                           Generate images with ASCII art
    -tutxt                          Generate images with ASCII art using Unicode characters
    -tvdx                           Generate images using VDX format
    -txmi                           Generate XMI file for class diagram
    -v[erbose]                      Have log information
    -version                        Display information about PlantUML and Java versions
    -xmlstats                       Output general statistics in file plantuml-stats.xml

If needed, you can setup the environment variable GRAPHVIZ_DOT.
```


