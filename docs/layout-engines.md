## ⚙ Layout Engines and Options

PlantUML allows you to use several different layout engines.
The following 4 apply to most diagrams.

See these 4 variants of a [SAREF4CITY diagram](https://github.com/VladimirAlexiev/rdf2rml/tree/master/test/saref4city#diagram-with-graphviz-layout) for comparison 
(this is an RDF graph using the Smart Applications REFerence Ontology (SAREF) extension for Smart Cities).
The source is [example1-saref4city.puml](https://github.com/VladimirAlexiev/rdf2rml/blob/master/test/saref4city/example1-saref4city.puml) and is generated from a Turtle file).
The notes below are based on observing only these examples, so they are subjective.

- [Graphviz](graphviz-dot) is the default engine. Relies on an external program
- [Smetana](smetana02). Use `!pragma layout smetana` in the file or `-Playout=smetana` on the command-line. A port of Graphviz to Java. Tends to make slightly straighter arrows
- [VizJs](vizjs) uses JavaScript. Use `-graphvizdot vizjs` on the command line. Tends to space out nodes more, resulting in a bigger diagram.
- [ELK (Eclipse Layout Kernel)](elk). Use `!pragma layout elk`  in the file or `-Playout=elk` on the command-line. Supports only orthogonal layout, and doesn't cover all features

[Sequence diagrams](sequence-diagram) have 2 engines:
- "puma" is the older and still default engine
- [teoz](teoz) is a new engine that has some unique features: anchors (named arrows/messages), duration, nested boxes.  More features are in development (see [teoz in the forum](http://forum.plantuml.net/tag/teoz)), eg parallel messages

[ditaa](ditaa) (Ascii Art) diagrams have an optional engine:
- [noditaa](http://beta.plantuml.net/noditaa/) replaces `ditaa` with java code. It's a beta release from 2019 that hasn't been updated


A number of options affect aspects of the layout. We list them below with links to forum threads:
- [#4418](http://forum.plantuml.net/4418), [#3111](http://forum.plantuml.net/3111), [#4045](http://forum.plantuml.net/4045) `!pragma svek_trace`: saves `dot` and `svg` files for debugging
- [#1343](http://forum.plantuml.net/1343) `!pragma aspect`: aspect ratio. May be obsolete, since `aspect` is not found on the [graphviz attrs](https://www.graphviz.org/doc/info/attrs.html#d:aspect) page, and [attrs-test](http://www.graphviz.org/content/attrs-test#daspect) is missing altogether.
- [#1226](http://forum.plantuml.net/1226) `!pragma ratio`: aspect ratio. Currently seems broken: specifying two numbers `m,n` causes graphviz error.
- [#977](http://forum.plantuml.net/977) `skinparam nodesep`: space between nodes in pixels.
- [#977](http://forum.plantuml.net/977) `skinparam ranksep`: space between node ranks.
- [#1608](http://forum.plantuml.net/1608) `skinparam linetype ortho`: orthogonal layout (but label position is wrong, see [plantuml/backlog#11](https://github.com/plantuml/backlog/issues/11)) 
- [#1608](http://forum.plantuml.net/1608) `skinparam linetype polyline`: straight not curved edges
- [#4387](https://forum.plantuml.net/4387) [#5007](https://forum.plantuml.net/5007) `together`: keep nodes next to each other
- [#3188](http://forum.plantuml.net/3188) `norank`: edge doesn't count for the layout process
- [#8365](http://forum.plantuml.net/8365) `hidden`: invisible edge that counts for the layout process 
- [#4418](http://forum.plantuml.net/4418), [#1132](http://forum.plantuml.net/1132), [#3231](http://forum.plantuml.net/3231), [#3111](http://forum.plantuml.net/3111), [#3143](http://forum.plantuml.net/3143) `!pragma horizontalLineBetweenDifferentPackageAllowed`: allow to make a horizontal line between packages. (Also see [#1628](https://forum.plantuml.net/1628) on layout of grouping components)
- [#1296](http://forum.plantuml.net/1296) `skinparam minClassWidth`: make nodes not narrower than this
- [#1296](http://forum.plantuml.net/1296) `skinparam sameClassWidth`: make all nodes the same width
- [#4637](http://forum.plantuml.net/4637) `skinparam minClassWidth` on sequence diagrams
- [#2538](http://forum.plantuml.net/2538) `layout_new_line` for disconnected parts of a diagram
- [#3118](http://forum.plantuml.net/3118) `skinparam padding` and `margin` for title, footer, etc
- [#5493](http://forum.plantuml.net/5493) `skinparam ParticipantPadding` and `skinparam BoxPadding`: padding on sequence diagrams


Achieving good layout with PlantUML is sometimes non-trivial. 
See [PlantUML GraphViz Layout](https://isgb.otago.ac.nz/infosci/mark.george/Wiki/wiki/PlantUML%20GraphViz%20Layout) by Mark George at University of Otago
for more advice.


