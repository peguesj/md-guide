## Docutils (Install)

[Docutils](http://docutils.sourceforge.net) allows to
conveniently write and generate documents in various output formats ([see installation details here](http://docutils.sourceforge.net/sandbox/uml-plantUml/usage)):

1. Replace/patch your docutils distribution with the files in [src/](http://docutils.sourceforge.net/sandbox/uml-plantUml/src)
1. See usage examples in [usage/](http://docutils.sourceforge.net/sandbox/uml-plantUml/usage)including how to setup defaults PlantUML


## Usage

Use the "uml" directive and write an indented block of PlantUML commands. No arguments are required, an image will be generated and inlined. The name is derived from the input line number, the generated plantuml "source" is keep in the same directory.

```
.. uml::

actor User
participant "First Class" as A
participant "Second Class" as B
participant "Last Class" as C

User -> A: DoWork
activate A

```

You can pass a filename for the image (*WITHOUT extension*) as an optional parameter.

```
.. uml:: uml2/myDiagram123

actor User
participant "First Class" as A
participant "Second Class" as B
participant "Last Class" as C

User -> A: DoMoreWork
activate A
```



