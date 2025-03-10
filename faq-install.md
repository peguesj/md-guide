## Local Installation notes


## Sequence Diagram

Once installation is complete you should first try creating some **Sequence Diagrams**. Since these work without Graphviz this is the fastest way to check that the installation worked. If they do not work, __other diagrams will probably not work__.

You should make sure to test **Sequence Diagrams** using the command line and not in the target tool you want to install (Eclipse, Word, Mediawiki...) :

```
java -jar plantuml.jar -verbose sequenceDiagram.txt
```

In the ``sequenceDiagram.txt`` file, you can have a very simple test:

```
@startuml
Alice -> Bob: test
@enduml
```

The ``-verbose`` flag is used to generated some logs that you can send to us, if no image is generated.

Under Unix, you must have X11 librairies installed (which is done by default). Otherwise, you will have some [HeadlessException](http://www.oracle.com/technetwork/articles/javase/headless-136834.html).
You may have to add a flag ``-Djava.awt.headless=true`` in the [command line](command-line).

If this is working, but not in your tool, it is probably due to a specific tool issue:

On MediaWiki & Windows, you must set the read & execute permissions on ``C:\Windows\system32\cmd.exe`` for the account the PHP web service extension is running under. PHP needs those permissions to "fork" other processes.


## Other Diagrams

Once sequence diagrams are working fine, you can focus on other diagrams.

If Graphviz is not installed on your system, you have to [install it first](graphviz-dot).

Under Linux, try to launch ``dot`` command into a command shell. You *may* have to finalize the installation by typing ``dot -C``.

[You may have to set GRAPHVIZ\_DOT](graphviz-dot) variables if you have not chosen the default installation directory of Graphviz.

To test the installation of Graphviz, you can use the command line:
```
java -jar plantuml.jar -testdot
```

You can also use this special diagram description:

```
@startuml
testdot
@enduml
```

Once again, you should test using the command line and the ``-verbose`` flag:

```
java -jar plantuml.jar -verbose classDiagram.txt
```

The ``classDiagram.txt`` file can be very simple:

```
@startuml
A <|-- B
@enduml
```

If you still have issues, then you can [send us a mail](mailto:plantuml@gmail.com).


