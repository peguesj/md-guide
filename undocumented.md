## Undocumented PlantUML features

Page for list of **Undocumented PlantUML features** in order **to document**


## Undocumented PlantUML features in order to document

The list comes from [Issue\#261](https://github.com/plantuml/plantuml/issues/261) thanks to [@VladimirAlexiev](https://github.com/VladimirAlexiev),

And the list of [Issue\#261](https://github.com/plantuml/plantuml/issues/261) comes mostly from [QA\#7095](https://forum.plantuml.net/7095), [QA\#7140](https://forum.plantuml.net/7140) thanks to [@Anthony-Gaudino](https://github.com/Anthony-Gaudino),
and was complemented, categorized, and converted to a task list by @VladimirAlexiev.

Then the list is here in order to put, after each item:
* [[#98FB98#DONE]]
* [[#FFD700#TODO]]
* [[#AA1111#BUG]]
* [[#FF6600#deprecated]]
* [[#1111AA#SEE]]
* or [[#C8FBC8#*TBC*]]
and to follow and share the state of new documentation to produce.

### Preprocessor, Includes, Sectioning

[preprocessing-v2 (old)](preprocessing-v2) & [preprocessing (new)](preprocessing)

* [QA\#6577](https://forum.plantuml.net/6577) Ability to include blocks ("subsections") of code
* [QA\#7838](https://forum.plantuml.net/7838) ``!pragma http.proxyHost``
* [QA\#6289](https://forum.plantuml.net/6289) ``%filename%`` and ``%filenameNoExtension%``
* [QA\#6199](https://forum.plantuml.net/6199) ``%PLANTUML_VERSION%`` [[#FF6600#deprecated]][[#1111AA#SEE]] New [Builtin functions](preprocessing#0umqmmdy1n9yk362kjka) ``%version()``
* [QA\#5968](https://forum.plantuml.net/5968) ``%filedate%`` 
* [QA\#5769](https://forum.plantuml.net/5769) ``%filename%`` and ``%dirpath%`` variables [[#FF6600#deprecated]][[#1111AA#SEE]] New [Builtin functions](preprocessing#0umqmmdy1n9yk362kjka)
* [QA\#5171](https://forum.plantuml.net/5171) [[#98FB98#DONE]] Boolean not ``!`` and parenthesis on ``!ifdef`` [[#98FB98#DONE]] superseded by ``%not()`` [[#1111AA#SEE]] [QA\#12320](https://forum.plantuml.net/12320)
* [QA\#3868](https://forum.plantuml.net/3868) Use tilde ``~`` to escape ``@startuml``
* [QA\#5483](https://forum.plantuml.net/5483) ``@startuml`` filename for automatic extensions
* [QA\#4467](https://forum.plantuml.net/4467) [[#98FB98#DONE]] ``@startuml`` with identifier for includes [[#98FB98#DONE]] on [source file](sources)
* [QA\#1466](https://forum.plantuml.net/1466) [[#98FB98#DONE]] ``@startuml{OPTIONS}`` [[#98FB98#DONE]] on [source file](sources)
* [QA\#4596](https://forum.plantuml.net/4596) ``\startXXX`` instead of ``@startXXX``
* [QA\#5769](https://forum.plantuml.net/5769) [[#98FB98#DONE]] ``@startdef and @enddef`` [[#98FB98#DONE]] on [source file](sources)
* [QA\#1525](https://forum.plantuml.net/1525), [QA\#5793](https://forum.plantuml.net/5793) ``@pause @unpause``
* [QA\#1525](https://forum.plantuml.net/1525) ``@pause @unpause @continue @append and /' ... '/`` multiline comments [[#98FB98#DONE]] for comments [[#C8FBC8#*TBC*]] for pause/unpause/continue
* [QA\#4266](https://forum.plantuml.net/4266) ``-config`` parameter
* [QA\#2410](https://forum.plantuml.net/2410) Multiple include paths
* [QA\#7337](https://forum.plantuml.net/7337) [[#98FB98#DONE]] ``$Tags`` to include individual pieces [[#98FB98#DONE]] for [component](component-diagram) [[#C8FBC8#*TBC*]] for other diagram
* [QA\#7337](https://forum.plantuml.net/7337) [[#98FB98#DONE]] remove / restore [[#98FB98#DONE]] for [component](component-diagram) [[#C8FBC8#*TBC*]] for other diagram
*  wildcards in ``remove / hide / restore``, eg ``remove *`` [[#98FB98#DONE]] for [component](component-diagram) [[#C8FBC8#*TBC*]] for other diagram

### Running and Output

[Command-line](command-line) [[#98FB98#DONE]]

* [QA\#4752](https://forum.plantuml.net/4752) [[#98FB98#DONE]] Output Braille diagrams (``-tbraille``) [[#98FB98#DONE]] [command-line](command-line)
* [QA\#5037](https://forum.plantuml.net/5037) [[#98FB98#DONE]] ``-pipemap`` parameter (HTML clickable maps): [``command-line#standard_input_output``](command-line#standard_input_output)
* [QA\#3562](https://forum.plantuml.net/3562) [[#98FB98#DONE]] Diagram code is embedded in PNG metadata (``-metadata -checkmeta``)
* [QA\#1601](https://forum.plantuml.net/1601) [[#98FB98#DONE]] ``-gui`` parameter accepts a path [[#98FB98#DONE]]
* [QA\#3214](https://forum.plantuml.net/3214) [[#98FB98#DONE]] ``-eps:text`` parameter [[#98FB98#DONE]] [command-line](command-line)

[ASCII art](ascii-art) [[#98FB98#DONE]] output with ``-ttxt`` or ``-tutxt`` [[#98FB98#DONE]] [command-line](command-line)

* [QA\#4147](https://forum.plantuml.net/4147) [[#98FB98#DONE]] ``skinparam maxAsciiMessageLength`` [[#98FB98#DONE]]

[LaTeX](latex) output with ``-tlatex`` through Tikz [[#98FB98#DONE]] [command-line](command-line)

* [QA\#1798](https://forum.plantuml.net/1798) latex-tikz-support anything more to document?
* Latex "see result online" (eg https://www.writelatex.com/read/pgkkspzgzgpb) doesn't work because need to migrate to overleaf
* [QA\#6495](https://forum.plantuml.net/6495) ``skinparam tikzFont``
* [QA\#3558](https://forum.plantuml.net/3558) Latex link [[latex://]]

[SVG](svg) output with ``-tsvg`` [[#98FB98#DONE]]

* [QA\#5453](https://forum.plantuml.net/5453) [[#98FB98#DONE]] ``skinparam pathHoverColor`` [[#98FB98#DONE]]
* [QA\#7334](https://forum.plantuml.net/7334) [[#98FB98#DONE]] ``skinparam svgDimensionStyle`` [[#98FB98#DONE]]

### Layout

* [QA\#4418](https://forum.plantuml.net/4418), [QA\#3111](https://forum.plantuml.net/3111), [QA\#4045](https://forum.plantuml.net/4045) ``!pragma svek_trace``
* [QA\#1343](https://forum.plantuml.net/1343) ``!pragma aspect``
* [QA\#1226](https://forum.plantuml.net/1226) ``!pragma ratio``
* [QA\#977](https://forum.plantuml.net/977) ``skinparam nodesep``
* [QA\#977](https://forum.plantuml.net/977) ``skinparam ranksep``
* [QA\#3188](https://forum.plantuml.net/3188) norank arrow option
* [QA\#8365](https://forum.plantuml.net/8365) hidden and norank
* [QA\#4418](https://forum.plantuml.net/4418), [QA\#1132](https://forum.plantuml.net/1132), [QA\#3231](https://forum.plantuml.net/3231), [QA\#3111](https://forum.plantuml.net/3111), [QA\#3143](https://forum.plantuml.net/3143) ``!pragma horizontalLineBetweenDifferentPackageAllowed``
* [QA\#1296](https://forum.plantuml.net/1296) ``skinparam minClassWidth`` and ``skinparam sameClassWidth``
* [QA\#4637](https://forum.plantuml.net/4637) ``skinparam minClassWidth`` on sequence diagram
* [QA\#2538](https://forum.plantuml.net/2538) ``layout_new_line`` for disconnected parts
* [QA\#3118](https://forum.plantuml.net/3118) ``skinparam padding``
* [QA\#5493](https://forum.plantuml.net/5493) ``skinparam ParticipantPadding`` and ``skinparam BoxPadding``

### Text and Links

[Creole](creole), [Link](link), [ASCII Math, JLatexMath](ascii-math)

* [QA\#3104](https://forum.plantuml.net/3104) Use ``\`` for multiline stuff
* [QA\#3055](https://forum.plantuml.net/3055) Align text with ``\l`` and ``\r``
* [QA\#3601](https://forum.plantuml.net/3601) Creole on class titles with as
* [Issues\#104](https://github.com/plantuml/plantuml/issues/104) ``skinparam wrapWidth`` and ``skinparam wrapMessageWidth``
* [QA\#3820](https://forum.plantuml.net/3820) ``skinparam tabSize``
* [QA\#5254](https://forum.plantuml.net/5254) [[#98FB98#DONE]] ``<plain>...</plain>`` to remove default text style (eg ``skinparam classFontStyle``) [[#98FB98#DONE]] [on creole page](creole#xbti2cgar0ssk362kjd9)
* [QA\#5574](https://forum.plantuml.net/5574) [[#98FB98#DONE]] tooltip over link [[#98FB98#DONE]] Page [link](link)

### Images, Icons, Sprites, Shapes, Embellishments

* [QA\#4080](https://forum.plantuml.net/4080) Import images from jar/zip *(Link to [QA\#12578](https://forum.plantuml.net/12578))*
* [QA\#3790](https://forum.plantuml.net/3790) DATA URI as embeded image
* [QA\#7485](https://forum.plantuml.net/7485) ``skinparam DiagonalCorner``
* [QA\#2899](https://forum.plantuml.net/2899) ``skinparam activityShape``
* [QA\#4076](https://forum.plantuml.net/4076), [QA\#4079](https://forum.plantuml.net/4079) Sprites on stereotypes
* [QA\#8084](https://forum.plantuml.net/8084) listsprites of stdlib: [alphadoc sprite\#stdlib](sprite#hdvb3xdf1doekdtyqgs2) and [sprite\#listing-sprites](sprite#jq1w8ezst4vzkdtyqu8b)

### Color [[#98FB98#DONE]]

* [QA\#3770](https://forum.plantuml.net/3770) [[#98FB98#DONE]] Inline set of multiple colors in various diagrams (``text;line;back;header``) [[#98FB98#DONE]]
* [QA\#1487](https://forum.plantuml.net/1487) [[#98FB98#DONE]] ``##[style]color`` of node borders: works for class and state diagrams [[#98FB98#DONE]] [on class](class-diagram) and [state](state-diagram)
* [QA\#5340](https://forum.plantuml.net/5340) [[#98FB98#DONE]] Inline coloring of node borders [[#98FB98#DONE]] [on use-case](use-case-diagram) 
* [QA\#7287](https://forum.plantuml.net/7287) [[#98FB98#DONE]] Automatic color [[#98FB98#DONE]] [on color page](color) 
* [QA\#3648](https://forum.plantuml.net/3648) [[#98FB98#DONE]] Transparent color [[#98FB98#DONE]] [on color page](color) 

### Arrows

* [QA\#3636](https://forum.plantuml.net/3636) [[#98FB98#DONE]] Arrows from/to class members [[#98FB98#DONE]]
* [QA\#3621](https://forum.plantuml.net/3621) Component diagram consumer/provider arrows
* make sure all arrow params are documented: ``dotted|dashed|plain|bold|hidden|norank|single|thickness|left|right|up|down, color``
* [QA\#3816](https://forum.plantuml.net/3816) ``skinparam ArrowColor``, stereotyped arrows, new syntax for inline arrow style (Setting multiple arrow ``skinparams in one line``); [[#FF6600#deprecated]] (componentArrowColor is deprecated)
* [QA\#4949](https://forum.plantuml.net/4949) [[#98FB98#DONE]] Inline setting for edge style and thickness [[#98FB98#DONE]] on Class and  Deployment
* [QA\#4260](https://forum.plantuml.net/4260) [[#98FB98#DONE]] bold and plain arrow styles [[#98FB98#DONE]]
* [QA\#4181](https://forum.plantuml.net/4181) [[#98FB98#DONE]] bold, dashed, dotted [[#98FB98#DONE]]
* Make sure all arrow types are documented on one page: See ``arrows`` and ``arrows-2`` at [github.com/anoff/blog/tree/master/static/assets/plantuml/diagrams](https://github.com/anoff/blog/tree/master/static/assets/plantuml/diagrams)
* [QA\#1736](https://forum.plantuml.net/1736) [[#98FB98#DONE]] Multiple lollipop edge styles [[#98FB98#DONE]]
* [QA\#5261](https://forum.plantuml.net/5261) Crows foot edge
* [QA\#2259](https://forum.plantuml.net/2259) [[#98FB98#DONE]] Class diagram ``--(`` and ``-0)-`` arrows [[#98FB98#DONE]]
* [QA\#310](https://forum.plantuml.net/310) [[#98FB98#DONE]] Sequence diagram ``?->`` and ``->?`` arrows [[#98FB98#DONE]]

### Mixed and Embedded Diagrams

* [QA\#2335](https://forum.plantuml.net/2335) [[#98FB98#DONE]] ``allow_mixing vs mix_usecase mix_actor``... [[#98FB98#DONE]] on [Deployment](deployment-diagram#6d6863e19pu3l3t7uqw6)
* [QA\#375](https://forum.plantuml.net/375) Embed SVG in SVG diagram
* [QA\#2427](https://forum.plantuml.net/2427) [[#98FB98#DONE]] Embed SALT UI diagrams in notes and other texts ("Flowchat") [[#98FB98#DONE]] See [Salt](salt)

### Alternative Layoters

* [QA\#4436](https://forum.plantuml.net/4436), [QA\#5336](https://forum.plantuml.net/5336), [smetana02](smetana02) [[#98FB98#DONE]] ``!pragma graphviz_dot jdot``: replace graphviz with Java code [[#98FB98#DONE]] ➥ ``!pragma layout smetana`` *See [smetana02](smetana02)* 
* [vizjs](vizjs) ``-graphvizdot vizjs``: replace graphviz with JavaScript code
* [noditaa](http://beta.plantuml.net/noditaa/): replace ditaa with java code

### [Class Diagrams](class-diagram)

* [QA\#5835](https://forum.plantuml.net/5835) [[#98FB98#DONE]] Notes on class fields [[#98FB98#DONE]]
* [QA\#3054](https://forum.plantuml.net/3054) details on how the "attributes" vs "methods" boxes are formed, and what happens when you add your own divider line
* [QA\#2913](https://forum.plantuml.net/2913) [[#98FB98#DONE]] Hide private / protected / package class members [[#98FB98#DONE]]
* [QA\#3448](https://forum.plantuml.net/3448) [[#98FB98#DONE]] Tree structure inside class [[#98FB98#DONE]] *See [creole tree](creole#2u7lnfjrnmfdk362kjda)* 
* [QA\#3424](https://forum.plantuml.net/3424) Class attribute stereotype
* [QA\#2259](https://forum.plantuml.net/2259) Class diagram circle
* [QA\#2239](https://forum.plantuml.net/2239) [[#98FB98#DONE]] extends and implements can reference multiple nodes
* [QA\#3193](https://forum.plantuml.net/3193) ``skinparam groupInheritance`` to merge inheritance arrows going to the same parent [[#98FB98#DONE]] (+ Adding link to Defect [QA#13532](https://forum.plantuml.net/13532/groupinheritance-bug))
* [QA\#1638](https://forum.plantuml.net/1638) [[#98FB98#DONE]] package style card [[#98FB98#DONE]] [[#C8FBC8#*TBC*]]

### [Component Diagrams](component-diagram) [[#98FB98#DONE]] 

* [QA\#11052](https://forum.plantuml.net/11052) [[#98FB98#DONE]] ``remove @unlinked components;`` [[#98FB98#DONE]]  [[#C8FBC8#*TBC*]] for other diagram
* [QA\#11052](https://forum.plantuml.net/11052) [[#98FB98#DONE]]  ``component tags and hide/remove/restore $tag`` [[#98FB98#DONE]] for [component](component-diagram) [[#C8FBC8#*TBC*]] for other diagram

### [Sequence Diagrams](sequence-diagram) [[#98FB98#DONE]]

[teoz](teoz), [``sequence-diagram#anchors_and_duration``](sequence-diagram#anchors_and_duration), [tag/teoz](https://forum.plantuml.net/tag/teoz): new Teoz (vs old Puma) for sequence diagrams

* [QA\#4247](https://forum.plantuml.net/4247) [[#98FB98#DONE]] hide unlinked participants [[#98FB98#DONE]]
* [QA\#7119](https://forum.plantuml.net/7119) [[#98FB98#DONE]] ``%autonumber%``
* [QA\#8511](https://forum.plantuml.net/8511) [[#98FB98#DONE]] ``autonumber inc`` [[#98FB98#DONE]]
* [QA\#2794](https://forum.plantuml.net/2794) [[#98FB98#DONE]] ``skinparam lifelineStrategy`` [[#98FB98#DONE]]
* [QA\#2503](https://forum.plantuml.net/2503) [[#98FB98#DONE]] Secondary group label in sequence diagram [[#98FB98#DONE]]
* [QA\#7264](https://forum.plantuml.net/7264) [[#98FB98#DONE]] ``skinparam belowForResponse`` [[#98FB98#DONE]]
* [QA\#1047](https://forum.plantuml.net/1047) [[#98FB98#DONE]] ``skinparam style strictuml``: emits triangle rather than sharp arrow heads [[#98FB98#DONE]]
* [QA\#3482](https://forum.plantuml.net/3482), [QA\#206](https://forum.plantuml.net/206) [[#98FB98#DONE]] ``skinparam sequenceMessageAlign`` [[#98FB98#DONE]]

### [Activity Diagrams](activity-diagram-beta)

* [QA\#5201](https://forum.plantuml.net/5201) ``skinparam swimlaneWidth`` [[#AA1111#BUG]] See [QA\#12463](https://forum.plantuml.net/12463)
* [QA\#2681](https://forum.plantuml.net/2681) [[#98FB98#DONE]] Swimlane alias [[#98FB98#DONE]]
* [QA\#4470](https://forum.plantuml.net/4470) [[#98FB98#DONE]] Label of arrows of repeat loops (repeat while) [[#98FB98#DONE]]
* [QA\#6105](https://forum.plantuml.net/6105) [[#98FB98#DONE]] Activity diagram ``break`` [[#98FB98#DONE]]
* [QA\#301](https://forum.plantuml.net/301) [[#98FB98#DONE]] Activity Beta ``if (...) is/equals (...) then`` [[#98FB98#DONE]]
* [QA\#265](https://forum.plantuml.net/265) [[#98FB98#DONE]] Activity Beta ``kill`` [[#98FB98#DONE]]
* [QA\#3931](https://forum.plantuml.net/3931) [[#98FB98#DONE]] ``!pragma useVerticalIf on``: draw if/elseif/else structure vertically [[#98FB98#DONE]]
* [QA\#1626](https://forum.plantuml.net/1626) [[#98FB98#DONE]] Activity diagram GOTO [[#98FB98#DONE]] See [activity-diagram](activity-diagram-beta) and [activity-diagram-issues](activity-diagram-issues)
* [QA\#2792](https://forum.plantuml.net/2792) ``skinparam activityArrowFontSize``
* [QA\#3166](https://forum.plantuml.net/3166) ``skinparam activityArrowFontColor``
* [QA\#5346](https://forum.plantuml.net/5346) [[#98FB98#DONE]] Activity diagram joinspec [[#98FB98#DONE]]
* [QA\#2868](https://forum.plantuml.net/2868) Activity diagram multiple halting states
* [QA\#3505](https://forum.plantuml.net/3505) [[#98FB98#DONE]] Activity diagram end [[#98FB98#DONE]]
* [QA\#5826](https://forum.plantuml.net/5826) [[#98FB98#DONE]] Backward on loops
* [QA\#4906](https://forum.plantuml.net/4906) [[#98FB98#DONE]] Gradient color on activity diagram partition [[#98FB98#DONE]]
* [QA\#2398](https://forum.plantuml.net/2398) [[#98FB98#DONE]] Note on partition [[#98FB98#DONE]]
* [QA\#2793](https://forum.plantuml.net/2793) [[#98FB98#DONE]] Inline coloring of partition [[#98FB98#DONE]]
* [QA\#1290](https://forum.plantuml.net/1290) [[#98FB98#DONE]] ``skinparam conditionStyle``: inside (hexagon: default), foo1 (big diamond), diamond (tiny diamond) [[#98FB98#DONE]]
* [QA\#6010](https://forum.plantuml.net/6010) ``skinparam arrowMessageAlign center``
* [QA\#4411](https://forum.plantuml.net/4411) ``skinparam colorArrowSeparationSpace``: multiple parallel arrows in activity digrams
* [[#98FB98#DONE]] [QA\#3770](https://forum.plantuml.net/3770) Background color of ``alt/group`` -> to [Sequence Diagrams](sequence-diagram)

### [State Diagrams](state-diagram) [[#98FB98#DONE]]

* [QA\#1159](https://forum.plantuml.net/1159) [[#98FB98#DONE]] State diagram ``<<choice>>, <<fork>>, <<join>>, <<end>>`` [[#98FB98#DONE]]
* [QA\#3672](https://forum.plantuml.net/3672) [[#98FB98#DONE]] State Diagram ``<<choice>>`` [[#98FB98#DONE]]
* [QA\#10077](https://forum.plantuml.net/10077) [[#98FB98#DONE]] Colored connectors in state diagrams [[#98FB98#DONE]]
* [QA\#1159](https://forum.plantuml.net/1159) [[#98FB98#DONE]] Choice Pseudostate in State Diagrams [[#98FB98#DONE]]
* [QA\#1099](https://forum.plantuml.net/1099) [[#98FB98#DONE]] State diagram hide empty description [[#98FB98#DONE]]
* [QA\#4309](https://forum.plantuml.net/4309) [[#98FB98#DONE]] State diagram ``<<expansionInput>> and <<expansionOutput>>, <<inputPin>> and <<outputPin>>, <<entrypoint>> and <<exitpoint>> ``[[#98FB98#DONE]]
* [QA\#1812](https://forum.plantuml.net/1812) [[#98FB98#DONE]] State inline color [[#98FB98#DONE]]

### [SDL and ER/IE Diagrams](ie-diagram) [[#98FB98#DONE]]

* [QA\#1232](https://forum.plantuml.net/1232) [[#98FB98#DONE]] SDL shapes (some undocumented) [[#98FB98#DONE]]
* IE-diagram, [Pull\#31](https://github.com/plantuml/plantuml/pull/31) [[#98FB98#DONE]] ER (IE) diagrams [[#98FB98#DONE]] [IE-diagram page](ie-diagram)

### [SALT (UI) Diagrams](salt) [[#98FB98#DONE]]

[search?q=salt](https://forum.plantuml.net/search?q=salt), [tag/salt](https://forum.plantuml.net/tag/salt)

* [QA\#5849](https://forum.plantuml.net/5849) [[#98FB98#DONE]] Salt pseudo "sprite" [[#98FB98#DONE]]
* [QA\#5840](https://forum.plantuml.net/5840) [[#98FB98#DONE]] Salt titled groupbox [[#98FB98#DONE]]
* [QA\#1265](https://forum.plantuml.net/1265), [QA\#5400](https://forum.plantuml.net/5400) [[#98FB98#DONE]] Salt tree table (table-tree) [[#98FB98#DONE]]

### [Timing Diagrams](timing-diagram) [[#98FB98#DONE]]

* [QA\#5776](https://forum.plantuml.net/5776) [[#98FB98#DONE]] Timing diagram coloring [[#98FB98#DONE]]

### [Gantt Charts](gantt-diagram) [[#98FB98#DONE]]

* [QA\#5782](https://forum.plantuml.net/5782) [[#98FB98#DONE]] Arrow on Gantt Diagram [[#98FB98#DONE]]
* [QA\#5510](https://forum.plantuml.net/5510) [[#98FB98#DONE]] Gantt diagram dates [[#98FB98#DONE]]

### [BPMN Diagrams](bpmn) [[#98FB98#DONE]]

* [QA\#5647](https://forum.plantuml.net/5647) [[#98FB98#DONE]] BPMN (``@startbpm`` and ``@endbpm``) [[#98FB98#DONE]] Page [BPMN](bpmn) updated

### [MindMap Diagrams](mindmap-diagram)

### [WBS Diagrams](wbs-diagram)

Work Breakdown Structures, Organizational Breakdown Structures (organigrams)

### [Graphviz Diagrams (DOT)](dot)

* [QA\#4210](https://forum.plantuml.net/4210) When using Dot, PlantUML supports strict graph and digraph
* [QA\#1206](https://forum.plantuml.net/1206) Dot graph

### Not yet categorized


