## Groovy API Client Code

Since calling Java from [Groovy](http://groovy.codehaus.org) is pretty simple, the only thing to do is to copy [PlantUML.jar](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download) file to the [classpath](http://groovy.codehaus.org/Running#Running-Addingthingstotheclasspath) (for example, ``../Groovy/Groovy-1.7.6/lib`` directory).


The following script print the current PlantUML version, and encode a URL:
```
println net.sourceforge.plantuml.version.Version.version() println
net.sourceforge.plantuml.code.TranscoderUtil.getDefaultTranscoder().encode("Bob->Alice:hello")
```

If you want to generate an image from a description:
```
s = new net.sourceforge.plantuml.SourceStringReader("@startuml\nBob->Alice:hello\n@enduml")
FileOutputStream file = new FileOutputStream("c:/testGroovy2.png")
s.generateImage(file);
file.close()
```


