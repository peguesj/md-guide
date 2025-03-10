## LaTeX Support in PlantUML

As of version 7997, PlantUML has introduced the feature to generate diagrams directly into [LaTeX](http://en.wikipedia.org/wiki/LaTeX), leveraging the capabilities of the [Tikz package](http://en.wikipedia.org/wiki/Tikz).

### Beta Version Notice
Please be aware that this functionality is currently in beta. While it adds a promising direction for PlantUML, it might contain bugs or unsupported features. We encourage users to actively report any issues encountered on first forum (Q&A) thread listed below to help us improve this feature based on actual user feedback and needs.

### How to Use LaTeX Generation
To use LaTeX generation, apply the following settings in your PlantUML environment:
- Use the `-tlatex` flag when operating through the [command line](command-line).
- Set `format="latex"` when configuring the [Ant task](ant-task).

#### Embedding in LaTeX Documents
If you want to incorporate the LaTeX output directly within another LaTeX document, use option `-tlatex:nopreamble`. PlantUML will output only the tikz-picture component, excluding the document preamble, facilitating a seamless integration into your existing LaTeX files.


## Class diagram example

```
@startuml
class Subscriber {
  subscriberId
}

class AccumUsage {
  subscriberId
}

class IpSession {
  ipAddress
  specificData
  sapcOriginStateId
  apnId
}

Subscriber "1" -[#blue]-> "1..*" IpSession
Subscriber "1" --> "0..1" AccumUsage
@enduml
```


## Sequence diagram example

```
@startuml
Bob -> Alice: hello
return Ok
@enduml
```

(TODO: [#362](https://github.com/plantuml/plantuml/issues/362) provide some examples in Overleaf)


## Creating Links in LaTeX with the `hyperref` Package

When utilizing the `hyperref` package in your LaTeX documents, you have the ability to craft links that lead to defined anchors within the same LaTeX/PDF document. In the PlantUML example below, notice that the second and last links point to a specific resource within the LaTeX document:

```
@startuml
participant Bob   [[http://www.yahoo.com]]
participant Alice [[latex://resource-interaction]]
Bob -> Alice :    [[http://www.google.com]] hello
Bob -> Alice :    [[latex://resource-interaction]] interact
@enduml
```

For a detailed discussion and related queries, see the second Q&A thread below.


## Links
- [Q&A 1798](http://forum.plantuml.net/1798): Latex TikZ support
- [Q&A 3558](https://forum.plantuml.net/3558): export to TikZ loses links
- [Q&A 10761](https://forum.plantuml.net/10761): Latex export limitations (font size, hyperlinks, PNG in header, scaling image to page)
- [Q&A 10788](https://forum.plantuml.net/10788): How to set Latex Font Size
- Latex PlantUML package (Oliver Kopp 2018-2023): [home](https://koppor.github.io/plantuml/), [Github](https://github.com/koppor/plantuml), [CTAN](https://ctan.org/pkg/plantuml)
- [Stackoverflow 71409448](https://stackoverflow.com/questions/71409448) PlantUML in Latex
  - Extra idea: use Markdown with Pandoc (LaTeX runs under the hood to generate PDF files): PlantUML diagrams work fine
- [TeX Exchange 428174](https://tex.stackexchange.com/questions/428174): Can I use the plantUML language in LaTeX?  Yes, and prerequisites to install are listed


