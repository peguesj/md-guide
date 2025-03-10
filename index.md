# 🌱 PlantUML at a Glance


## 🚀 Getting Started

**PlantUML** is a highly versatile tool that facilitates the rapid and straightforward creation of a wide array of diagrams. 

Utilizing a simple and intuitive language, users can effortlessly draft various types of diagrams.
For a detailed exploration of the language's capabilities and syntax, please refer to the [PlantUML Language Reference Guide](guide).

If you are new to PlantUML, we recommend starting with our [quick start page](starting) to get up
and running quickly. Should you have any questions, our [F.A.Q. page](faq) is a valuable resource. 
Additionally, PlantUML can be seamlessly integrated with [a variety of other tools](running) to enhance your workflow.


## 🧩 Supported UML Diagrams

With PlantUML, you can create well-structured UML diagrams, including but not limited to:

* [Sequence diagram](sequence-diagram)
* [Usecase diagram](use-case-diagram)
* [Class diagram](class-diagram)
* [Object diagram](object-diagram)
* [Activity diagram](activity-diagram-beta) *(Find the [legacy syntax here](activity-diagram-legacy))*
* [Component diagram](component-diagram)
* [Deployment diagram](deployment-diagram)
* [State diagram](state-diagram)
* [Timing diagram](timing-diagram)


## 📈 Supported Non-UML Diagrams

Beyond traditional UML diagrams, PlantUML also supports the creation of various other diagram types, such as:

* [JSON data](json)
* [YAML data](yaml)
* [EBNF diagram](ebnf)
* [Regex diagram](regex)
* [Network diagram (nwdiag)](nwdiag)
* [UI mockups (salt)](salt)
* [Archimate diagram](archimate-diagram)
* [Specification and Description Language (SDL)](activity-diagram-beta#sdl)
* [Ditaa diagram](ditaa)
* [Gantt diagram](gantt-diagram)
* [Chronology diagram](chronology-diagram)
* [MindMap diagram](mindmap-diagram)
* [WBS diagram](wbs-diagram)
* [Mathematics with AsciiMath or JLaTeXMath notation](ascii-math)
* [Information Engineering (IE) diagram](ie-diagram)
* [Entity Relationship (ER) diagram](er-diagram)


## 📣 Additional Features

Enhance the dynamism and informativeness of your diagrams with these additional features:

* [Hyperlinks and tooltips](link) to provide extra context and interactivity
* [Rich text formatting, emoticons, Unicode, and icons with Creole](creole) for a visually appealing presentation
* [OpenIconic icons](openiconic) for enhanced visual representation
* [Sprite icons](sprite) to add custom symbols
* [AsciiMath mathematical expressions](ascii-math) for precise mathematical representation


## 📥 Input Formats

PlantUML allows you to generate diagrams from various source input formats:
* [Source input data: *How and where diagrams can be written*](sources)

You can choose from different internal encodings:
* [PlantUML Text Encoding](text-encoding)


## ⚙ Layout Engines and Options

PlantUML allows you to use several different [layout engines](layout-engines):

- [Graphviz](graphviz-dot) is the default engine. Relies on an external program;
- [Smetana](smetana02). *(Use ``!pragma layout smetana`` in the file or ``-Playout=smetana`` on the command-line.)* A port of Graphviz to Java. Tends to make slightly straighter arrows;
- [VizJs](vizjs) uses JavaScript. *(Use ``-graphvizdot vizjs`` on the command line.)* Tends to space out nodes more, resulting in a bigger diagram;
- [ELK (Eclipse Layout Kernel)](elk). *(Use ``!pragma layout elk``  in the file or ``-Playout=elk`` on the command-line.)* Supports only orthogonal layout, and doesn't cover all features.

[Sequence diagrams](sequence-diagram) have 2 engines:
- *Puma* is the older and still default engine;
- [Teoz](teoz) *(Use ``!pragma teoz true``  in the file or ``-Pteoz=true`` on the command-line)* is a new engine that has some unique features: *anchors (named arrows/messages), duration, nested boxes...*

> Achieving good layout with PlantUML is sometimes non-trivial. 
> *See [PlantUML GraphViz Layout](https://isgb.otago.ac.nz/infosci/mark.george/Wiki/wiki/PlantUML%20GraphViz%20Layout) by Mark George at University of Otago for more advice.*


## 📤 Output Formats

Export your diagrams in a variety of formats to suit your needs, including:

* PNG for easy image sharing
* [SVG](svg) for scalable vector graphics
* [LaTeX](latex) for high-quality typesetting
* [EPS (Encapsulated PostScript )](eps) for used with LaTeX
* [ASCII art](ascii-art) *(available only for sequence diagrams)* for a text-based representation


## 🎉 Enjoy

Get started today and elevate your diagramming capabilities with **PlantUML**. Transform your ideas into clear and professional diagrams effortlessly 🎉!


