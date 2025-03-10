Contents
1 Sequence Diagram 1
1.1 1.2 1.3 1.4 1.5 1.6 Basic Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Declaring participant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Declaring participant on multiline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Use non-letters in participants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Message to Self . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Text alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6.1 Text of response message below the arrow . . . . . . . . . . . . . . . . . . . . . . . 5
1.7 Change arrow style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.8 Change arrow color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.9 Message sequence numbering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.10 Page Title, Header and Footer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.11 Splitting diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.12 Grouping message . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.13 Secondary group label . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.14 Notes on messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1.15 Some other notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
1.16 Changing notes shape [hnote, rnote] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.17 Note over all participants [across] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.18 Several notes aligned at the same level [/] . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
1.19 Creole and HTML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
1.20 Divider or separator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1.21 Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1.22 Delay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
1.23 Text wrapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
1.24 Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
1.25 Lifeline Activation and Destruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
1.26 Return . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
1.27 Participant creation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
1.28 Shortcut syntax for activation, deactivation, creation . . . . . . . . . . . . . . . . . . . . . 23
1.29 Incoming and outgoing messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
1.30 Short arrows for incoming and outgoing messages . . . . . . . . . . . . . . . . . . . . . . . 26
1.31 Anchors and Duration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
1.32 Stereotypes and Spots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
1.33 Position of the stereotypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
1.33.1 Top postion (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
1.33.2 Bottom postion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
1.34 More information on titles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
1.35 Participants encompass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
1.36 Removing Foot Boxes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
1.37 Skinparam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
1.38 Changing padding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
1.39 Appendix: Examples of all arrow type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
1.39.1 Normal arrow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
1.39.2 Itself arrow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
1.39.3 Incoming and outgoing messages (with ’[’, ’]’) . . . . . . . . . . . . . . . . . . . . . 37
1.39.4 Incoming messages (with ’[’) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
1.39.5 Outgoing messages (with ’]’) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
1.39.6 Short incoming and outgoing messages (with ’?’) . . . . . . . . . . . . . . . . . . . 40
1.39.7 Short incoming (with ’?’) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
1.39.8 Short outgoing (with ’?’) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
1.40 Specific SkinParameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
1.40.1 By default . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
1.40.2 LifelineStrategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
1.40.3 style strictuml . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
1.41 Hide unlinked participant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
PlantUML Language Reference Guide (1.2025.0) 591 / 606
CONTENTS CONTENTS
1.42 Color a group message . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.43 Mainframe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.44 Slanted or odd arrows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.45 Parallel messages (with teoz). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
45
45
47
2 Use Case Diagram 48
2.1 2.2 2.3 Usecases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Actors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Change Actor style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.1 Stick man (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.2 Awesome man . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.3 Hollow man . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4 Usecases description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.5 Use package . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.6 Basic example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.7 Extension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.8 Using notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.9 Stereotypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.10 Changing arrows direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.11 Splitting diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.12 Left to right direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.13 Skinparam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.14 Complete example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.15 Business Use Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.15.1 Business Usecase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.15.2 Business Actor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.16 Change arrow color and style (inline style) . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.17 Change element color and style (inline style) . . . . . . . . . . . . . . . . . . . . . . . . . 2.18 Display JSON Data on Usecase diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.18.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
48
49
49
49
50
50
51
52
52
53
53
54
55
56
56
57
58
58
58
59
59
60
60
3 Class Diagram 61
3.1 3.2 3.3 3.4 Declaring element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Relations between classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Label on relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Using non-letters in element names and relation labels . . . . . . . . . . . . . . . . . . . . 
3.4.1 Starting names with $. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.5 3.6 Adding methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Defining visibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.6.1 Visibility for methods or fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.6.2 Visibility for class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.7 Abstract and Static . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.8 Advanced class body . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.9 Notes and stereotypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.10 More on notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.11 Note on field (field, attribute, member) or method . . . . . . . . . . . . . . . . . . . . . . 
3.11.1 ￿ Constraint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.11.2 Note on field or method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.11.3 Note on method with the same name . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.12 Note on links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.13 Abstract class and interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.14 Hide attributes, methods... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.15 Hide classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.16 Remove classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.17 Hide, Remove or Restore tagged element or wildcard . . . . . . . . . . . . . . . . . . . . . 
3.18 Hide or Remove unlinked class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.19 Use generics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.20 Specific Spot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
3.21 Packages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
62
63
63
64
64
65
65
67
67
68
68
69
70
70
70
71
71
72
73
74
75
75
77
78
78
78
PlantUML Language Reference Guide (1.2025.0) 592 / 606
CONTENTS CONTENTS
3.22 Packages style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
3.23 Namespaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
3.24 Automatic package creation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
3.25 Lollipop interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.26 Changing arrows orientation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.27 Association classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.28 Association on same class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.29 Skinparam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.30 Skinned Stereotypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
3.31 Color gradient . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.32 Help on layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.33 Splitting large files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
3.34 Extends and implements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.35 Bracketed relations (linking or arrow) style . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.35.1 Line style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.35.2 Line color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
3.35.3 Line thickness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
3.35.4 Mix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
3.36 Change relation (linking or arrow) color and style (inline style) . . . . . . . . . . . . . . . 91
3.37 Change class color and style (inline style) . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.38 Arrows from/to class members . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
3.39 Grouping inheritance arrow heads . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
3.39.1 GroupInheritance 1 (no grouping) . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
3.39.2 GroupInheritance 2 (grouping from 2) . . . . . . . . . . . . . . . . . . . . . . . . . 95
3.39.3 GroupInheritance 3 (grouping only from 3) . . . . . . . . . . . . . . . . . . . . . . 95
3.39.4 GroupInheritance 4 (grouping only from 4) . . . . . . . . . . . . . . . . . . . . . . 96
3.40 Display JSON Data on Class or Object diagram . . . . . . . . . . . . . . . . . . . . . . . . 96
3.40.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
3.41 Packages and Namespaces Enhancement . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
3.42 Qualified associations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
3.42.1 Minimal example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
3.42.2 Another example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
3.43 Change diagram orientation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
3.43.1 Top to bottom (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
3.43.2 With Graphviz (layout engine by default). . . . . . . . . . . . . . . . . . . . . . . 99
3.43.3 With Smetana (internal layout engine). . . . . . . . . . . . . . . . . . . . . . . . . 100
3.43.4 Left to right . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.43.5 With Graphviz (layout engine by default). . . . . . . . . . . . . . . . . . . . . . . 101
3.43.6 With Smetana (internal layout engine). . . . . . . . . . . . . . . . . . . . . . . . . 103
4 Object Diagram 105
4.1 Definition of objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
4.2 Relations between objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
4.3 Associations objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
4.4 Adding fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
4.5 Common features with class diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
4.6 Map table or associative array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
4.7 Program (or project) evaluation and review technique (PERT) with map . . . . . . . . . . 110
4.8 Display JSON Data on Class or Object diagram . . . . . . . . . . . . . . . . . . . . . . . . 111
4.8.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
5 Activity Diagram (legacy) 112
5.1 5.2 5.3 5.4 5.5 5.6 5.7 Simple Action . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Label on arrows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Changing arrow direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Branches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
More on Branches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
Synchronization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
Long action description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
PlantUML Language Reference Guide (1.2025.0) 593 / 606
CONTENTS CONTENTS
5.8 5.9 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
Partition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
5.10 Skinparam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
5.11 Octagon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
5.12 Complete example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
6 Activity Diagram (New Syntax) 122
6.0.1 Benefits of the New Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
6.0.2 Transition to the New Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
6.1 6.2 6.3 Simple action . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
Start/Stop/End . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
Conditional . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
6.3.1 Several tests (horizontal mode) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
6.3.2 Several tests (vertical mode) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
6.4 6.5 6.6 Switch and case [switch, case, endswitch] . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
Conditional with stop on an action [kill, detach] . . . . . . . . . . . . . . . . . . . . . . . . 127
Repeat loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
6.6.1 Simple repeat loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
6.6.2 Repeat loop with repeat action and backward action . . . . . . . . . . . . . . . . . 128
6.7 6.8 6.9 Break on a repeat loop [break] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
Goto and Label Processing [label, goto] . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
While loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
6.9.1 Simple while loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
6.9.2 While loop with backward action . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
6.9.3 Infinite while loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
6.10 Parallel processing [fork, fork again, end fork, end merge] . . . . . . . . . . . . . . . . . . 133
6.10.1 Simple fork. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
6.10.2 fork with end merge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
6.10.3 Label on end fork (or UML joinspec): . . . . . . . . . . . . . . . . . . . . . . . . . 134
6.10.4 Other example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
6.11 Split processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
6.11.1 Split . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
6.11.2 Input split (multi-start) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
6.11.3 Output split (multi-end) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
6.12 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
6.13 Colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
6.14 Lines without arrows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
6.15 Arrows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
6.16 Connector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
6.17 Color on connector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
6.18 Grouping or partition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
6.18.1 Group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
6.18.2 Partition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
6.18.3 Group, Partition, Package, Rectangle or Card . . . . . . . . . . . . . . . . . . . . . 146
6.19 Swimlanes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
6.20 Detach or kill [detach, kill] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
6.21 SDL (Specification and Description Language) . . . . . . . . . . . . . . . . . . . . . . . . 151
6.21.1 Table of SDL Shape Name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.21.2 SDL using final separator (Deprecated form) . . . . . . . . . . . . . . . . . . . . . 151
6.21.3 SDL using Normal separator and Stereotype (Current oﬀiial form) . . . . . . . . . 153
6.22 Complete example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.23 Condition Style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
6.23.1 Inside style (by default) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
6.23.2 Diamond style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.23.3 InsideDiamond (or Foo1) style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
6.24 Condition End Style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
6.24.1 Diamond style (by default) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
6.24.2 Horizontal line (hline) style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
PlantUML Language Reference Guide (1.2025.0) 594 / 606
CONTENTS CONTENTS
6.25 Using (global) style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
6.25.1 Without style (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
6.25.2 With style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
7 Component Diagram 164
7.1 Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
7.1.1 Naming exceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
7.2 Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
7.3 Basic example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
7.4 Using notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
7.5 Grouping Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
7.6 Changing arrows direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
7.7 Use UML2 notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
7.8 Use UML1 notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
7.9 Use rectangle notation (remove UML notation) . . . . . . . . . . . . . . . . . . . . . . . . 171
7.10 Long description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
7.11 Individual colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
7.12 Using Sprite in Stereotype . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
7.13 Skinparam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
7.14 Specific SkinParameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
7.14.1 componentStyle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
7.15 Hide or Remove unlinked component . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
7.16 Hide, Remove or Restore tagged component or wildcard . . . . . . . . . . . . . . . . . . . 176
7.17 Display JSON Data on Component diagram . . . . . . . . . . . . . . . . . . . . . . . . . . 178
7.17.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
7.18 Port [port, portIn, portOut] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
7.18.1 Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
7.18.2 PortIn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
7.18.3 PortOut . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
7.18.4 Mixing PortIn & PortOut . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
8 Deployment Diagram 182
8.1 8.2 Declaring element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
Declaring element (using short form) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
8.2.1 Actor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
8.2.2 Component . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
8.2.3 Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
8.2.4 Usecase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
8.3 8.4 Linking or arrow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
Bracketed arrow style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
8.4.1 Line style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
8.4.2 Line color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
8.4.3 Line thickness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
8.4.4 Mix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
8.5 8.6 8.7 8.8 Change arrow color and style (inline style) . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
Change element color and style (inline style) . . . . . . . . . . . . . . . . . . . . . . . . . 191
Nestable elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
Packages and nested elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
8.8.1 Example with one level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
8.8.2 Other example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
8.8.3 Full nesting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
8.9 Alias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
8.9.1 Simple alias with as. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
8.9.2 Examples of long alias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
8.10 Round corner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
8.11 Specific SkinParameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
8.11.1 roundCorner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
8.12 Appendix: All type of arrow line . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
8.13 Appendix: All type of arrow head or ’0’ arrow . . . . . . . . . . . . . . . . . . . . . . . . . 203
PlantUML Language Reference Guide (1.2025.0) 595 / 606
CONTENTS CONTENTS
8.13.1 Type of arrow head . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
8.13.2 Type of ’0’ arrow or circle arrow . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
8.14 Appendix: Test of inline style on all element . . . . . . . . . . . . . . . . . . . . . . . . . . 205
8.14.1 Simple element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
8.14.2 Nested element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
8.14.3 Without sub-element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
8.14.4 With sub-element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
8.15 Appendix: Test of style on all element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
8.15.1 Simple element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
8.15.2 Global style (on componentDiagram) . . . . . . . . . . . . . . . . . . . . . . . . . . 208
8.15.3 Style for each element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
8.15.4 Nested element (without level) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
8.15.5 Global style (on componentDiagram) . . . . . . . . . . . . . . . . . . . . . . . . . . 213
8.15.6 Style for each nested element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
8.15.7 Nested element (with one level) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
8.15.8 Global style (on componentDiagram) . . . . . . . . . . . . . . . . . . . . . . . . . . 216
8.15.9 Style for each nested element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
8.16 Appendix: Test of stereotype with style on all element . . . . . . . . . . . . . . . . . . . . 219
8.16.1 Simple element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
8.17 Display JSON Data on Deployment diagram . . . . . . . . . . . . . . . . . . . . . . . . . . 221
8.17.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
8.18 Mixing Deployment (Usecase, Component, Deployment) element within a Class or Object
diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
8.18.1 Mixing all elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
8.19 Port [port, portIn, portOut] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
8.19.1 Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
8.19.2 PortIn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
8.19.3 PortOut . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
8.19.4 Mixing PortIn & PortOut . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
8.20 Change diagram orientation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
8.20.1 Top to bottom (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
8.20.2 With Graphviz (layout engine by default). . . . . . . . . . . . . . . . . . . . . . . 226
8.20.3 With Smetana (internal layout engine). . . . . . . . . . . . . . . . . . . . . . . . . 227
8.20.4 Left to right . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
8.20.5 With Graphviz (layout engine by default). . . . . . . . . . . . . . . . . . . . . . . 228
8.20.6 With Smetana (internal layout engine). . . . . . . . . . . . . . . . . . . . . . . . . 229
9 State Diagram 231
9.1 9.2 9.3 Simple State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
Change state rendering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
Composite state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
9.3.1 Internal sub-state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
9.3.2 Sub-state to sub-state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
9.4 9.5 9.6 9.7 Long name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
History [[H], [H*]] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
Fork [fork, join] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
Concurrent state [–, ||] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
9.7.1 Horizontal separator--
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
9.7.2 Vertical separator ||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
9.8 Conditional [choice] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
9.9 Stereotypes full example [start, choice, fork, join, end, history, history*] . . . . . . . . . . 239
9.9.1 Start, choice, fork, join, end . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
9.9.2 History, history* . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
9.9.3 Minimal example with all stereotypes . . . . . . . . . . . . . . . . . . . . . . . . . 241
9.10 Point [entryPoint, exitPoint] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
9.11 Pin [inputPin, outputPin] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
9.12 Expansion [expansionInput, expansionOutput] . . . . . . . . . . . . . . . . . . . . . . . . . 243
9.13 Arrow direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
PlantUML Language Reference Guide (1.2025.0) 596 / 606
CONTENTS CONTENTS
9.14 Change line color and style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
9.15 Note . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
9.16 Note on link . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
9.17 More in notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
9.18 Inline color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
9.19 Skinparam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
9.19.1 Test of all specific skinparam to State Diagrams . . . . . . . . . . . . . . . . . . . 249
9.20 Changing style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
9.21 Change state color and style (inline style) . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
9.22 Alias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
9.23 Display JSON Data on State diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
9.23.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
9.24 State description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
9.25 Style for Nested State Body . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
10 Timing Diagram 256
10.1 Declaring element or participant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
10.2 Binary and Clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
10.3 Adding message . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
10.4 Relative time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
10.5 Anchor Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
10.6 Participant oriented . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
10.7 Setting scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
10.8 Initial state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
10.9 Intricated state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
10.9.1 Intricated or undefined robust state . . . . . . . . . . . . . . . . . . . . . . . . . . 261
10.9.2 Intricated or undefined binary state . . . . . . . . . . . . . . . . . . . . . . . . . . 262
10.10Hidden state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
10.11Hide time axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
10.12Using Time and Date . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
10.13Change Date Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
10.14Manage time axis labels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
10.14.1 Label on each tick (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
10.14.2 Manual label (only when the state changes). . . . . . . . . . . . . . . . . . . . . . 266
10.15Adding constraint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
10.16Highlighted period . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
10.17Using notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
10.18Adding texts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
10.19Complete example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
10.20Digital Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
10.21Adding color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
10.22Using (global) style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
10.22.1 Without style (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
10.22.2 With style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
10.23Applying Colors to specific lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
10.24Compact mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
10.24.1 By default . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
10.24.2 Global mode with mode compact. . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
10.24.3 Local mode with only compact on element . . . . . . . . . . . . . . . . . . . . . . . 276
10.25Scaling analog signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
10.25.1 Without scaling: 0-max (by default). . . . . . . . . . . . . . . . . . . . . . . . . . 277
10.25.2 With scaling: min-max . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
10.26Customise analog signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
10.26.1 Without any customisation (by default). . . . . . . . . . . . . . . . . . . . . . . . 278
10.26.2 With customisation (on scale, ticks and height) . . . . . . . . . . . . . . . . . . . . 279
10.27Order state of robust signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
10.27.1 Without order (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
10.27.2 With order . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
PlantUML Language Reference Guide (1.2025.0) 597 / 606
CONTENTS CONTENTS
10.27.3 With order and label . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
10.28Defining a timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
10.28.1 By Clock (@clk). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
10.28.2 By Signal (@S). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
10.28.3 By Time (@time). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
10.29Annotate signal with comment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
11 Display JSON Data 285
11.1 Complex example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
11.2 Highlight parts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
11.3 Using different styles for highlight . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
11.4 JSON basic element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287
11.4.1 Synthesis of all JSON basic element . . . . . . . . . . . . . . . . . . . . . . . . . . 287
11.5 JSON array or table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
11.5.1 Array type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
11.5.2 Minimal array or table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
11.5.3 Number array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
11.5.4 String array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
11.5.5 Boolean array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
11.6 JSON numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
11.7 JSON strings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
11.7.1 JSON Unicode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
11.7.2 JSON two-character escape sequence . . . . . . . . . . . . . . . . . . . . . . . . . . 290
11.8 Minimal JSON examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
11.9 Empty table or list . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292
11.10Using (global) style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292
11.10.1 Without style (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292
11.10.2 With style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
11.11Display JSON Data on Class or Object diagram . . . . . . . . . . . . . . . . . . . . . . . . 294
11.11.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
11.11.2 Complex example: with all JSON basic element . . . . . . . . . . . . . . . . . . . . 294
11.12Display JSON Data on Deployment (Usecase, Component, Deployment) diagram . . . . . 295
11.12.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
11.13Display JSON Data on State diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
11.13.1 Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
11.14Creole on JSON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
12 Display YAML Data 299
12.1 Complex example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299
12.2 Specific key (with symbols or unicode) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
12.3 Highlight parts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
12.3.1 Normal style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
12.3.2 Customised style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
12.4 Using different styles for highlight . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
12.5 Using (global) style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
12.5.1 Without style (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
12.5.2 With style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
12.6 Creole on YAML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
13 Network Diagram with nwdiag 306
13.1 Simple diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
13.1.1 Define a network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
13.1.2 Define some elements or servers on a network . . . . . . . . . . . . . . . . . . . . . 306
13.1.3 Full example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
13.2 Define multiple addresses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307
13.3 Grouping nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308
13.3.1 Define group inside network definitions . . . . . . . . . . . . . . . . . . . . . . . . . 308
13.3.2 Define group outside of network definitions . . . . . . . . . . . . . . . . . . . . . . 309
13.3.3 Define several groups on same network . . . . . . . . . . . . . . . . . . . . . . . . . 309
PlantUML Language Reference Guide (1.2025.0) 598 / 606
CONTENTS CONTENTS
13.3.4 Example with 2 group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
13.3.5 Example with 3 groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310
13.4 Extended Syntax (for network or group) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
13.4.1 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
13.4.2 Group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
13.5 Using Sprites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313
13.6 Using OpenIconic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
13.7 Same nodes on more than two networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
13.8 Peer networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
13.9 Peer networks and group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
13.9.1 Without group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
13.9.2 Group on first . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
13.9.3 Group on second . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 318
13.9.4 Group on third . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
13.10Add title, caption, header, footer or legend on network diagram . . . . . . . . . . . . . . . 320
13.11With or without shadow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
13.11.1 With shadow (by default) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
13.11.2 Without shadow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
13.12Change width of the networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
13.12.1 First example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
13.12.2 Second example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324
13.13Other internal networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
13.14Using (global) style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
13.14.1 Without style (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
13.14.2 With style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
13.15Appendix: Test of all shapes on Network diagram (nwdiag) . . . . . . . . . . . . . . . . . 332
14 Salt (Wireframe) 335
14.1 Basic widgets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 335
14.2 Text area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 335
14.3 Open, close droplist . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336
14.4 Using grid [| and #, !, -, +] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
14.5 Group box [^] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
14.6 Using separator [.., ==, ~~, –] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
14.7 Tree widget [T] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338
14.8 Tree table [T] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338
14.9 Enclosing brackets [{, }] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
14.10Adding tabs [/] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
14.11Using menu [*] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
14.12Advanced table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
14.13Scroll Bars [S, SI, S-] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
14.14Colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344
14.15Creole on Salt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344
14.16Pseudo sprite [«, »] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346
14.17OpenIconic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346
14.18Add title, header, footer, caption or legend . . . . . . . . . . . . . . . . . . . . . . . . . . 347
14.19Zoom, DPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
14.19.1 Whitout zoom (by default) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
14.19.2 Scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
14.19.3 DPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
14.20Include Salt ”on activity diagram” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349
14.21Include salt ”on while condition of activity diagram” . . . . . . . . . . . . . . . . . . . . . 351
14.22Include salt ”on repeat while condition of activity diagram” . . . . . . . . . . . . . . . . . 352
14.23Skinparam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
14.24Style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354
15 ArchiMate Diagram 355
15.1 Archimate keyword . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355
15.2 Defining Junctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355
PlantUML Language Reference Guide (1.2025.0) 599 / 606
CONTENTS CONTENTS
15.3 Example 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 356
15.4 Example 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 357
15.5 List possible sprites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 358
15.6 ArchiMate Macros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 358
15.6.1 Archimate Macros and Library . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 358
15.6.2 Archimate elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 358
15.6.3 Archimate relationships . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 359
15.6.4 Appendice: Examples of all Archimate RelationTypes . . . . . . . . . . . . . . . . 360
16 Gantt Chart 364
16.1 Declaring tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 364
16.1.1 Workload . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 364
16.1.2 Start . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
16.1.3 End . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
16.1.4 Start/End . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366
16.2 One-line declaration (with the and conjunction) . . . . . . . . . . . . . . . . . . . . . . . . 366
16.3 Adding constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366
16.4 Short names or alias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367
16.5 Tasks with same name . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367
16.6 Customize colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368
16.7 Completion status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368
16.7.1 Adding completion depending percentage . . . . . . . . . . . . . . . . . . . . . . . 368
16.7.2 Change colour of completion (by style) . . . . . . . . . . . . . . . . . . . . . . . . . 368
16.7.3 Change colour of undone part of Task (by style) . . . . . . . . . . . . . . . . . . . 369
16.8 Milestone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370
16.8.1 Relative milestone (use of constraints) . . . . . . . . . . . . . . . . . . . . . . . . . 370
16.8.2 Absolute milestone (use of fixed date) . . . . . . . . . . . . . . . . . . . . . . . . . 370
16.8.3 Milestone of maximum end of tasks . . . . . . . . . . . . . . . . . . . . . . . . . . 370
16.9 Hyperlinks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
16.10Calendar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
16.11Coloring days . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
16.12Changing scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372
16.12.1 Daily (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372
16.12.2 Weekly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372
16.12.3 Monthly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373
16.12.4 Quarterly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373
16.12.5 Yearly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
16.12.6 Date range with between . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
16.12.7 Without date range . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
16.12.8 With date range . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375
16.13Zoom (example for all scale) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375
16.13.1 Zoom on daily (default) scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375
16.13.2 Zoom on weekly scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376
16.13.3 Zoom on monthly scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377
16.13.4 Zoom on quarterly scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 378
16.13.5 Zoom on yearly scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 378
16.14Weekscale with Weeknumbers or Calendar Date . . . . . . . . . . . . . . . . . . . . . . . . 379
16.14.1 With Weeknumbers (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . 379
16.14.2 With Weeknumbers (starting from 1). . . . . . . . . . . . . . . . . . . . . . . . . 379
16.14.3 With Calendar Date . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380
16.15Close day . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380
16.16Definition of a week depending of closed days . . . . . . . . . . . . . . . . . . . . . . . . . 381
16.17Working days . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 381
16.18Simplified task succession . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382
16.19Working with resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382
16.20Hide resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383
16.20.1 Without any hiding (by default) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383
16.20.2 Hide resources names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383
PlantUML Language Reference Guide (1.2025.0) 600 / 606
CONTENTS CONTENTS
16.20.3 Hide resources footbox . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 384
16.20.4 Hide the both (resources names and resources footbox) . . . . . . . . . . . . . . . 384
16.21Horizontal Separator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 384
16.22Vertical Separator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 385
16.23Complex example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 385
16.24Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 385
16.25Using style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
16.25.1 Without style (by default) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
16.25.2 With style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
16.25.3 With style (full example) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 388
16.25.4 Clean style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389
16.26Add notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390
16.27Pause tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
16.28Change link colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
16.29Tasks or Milestones on the same line . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 394
16.30Highlight today . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 394
16.31Task between two milestones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
16.32Grammar and verbal form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
16.33Add title, header, footer, caption or legend . . . . . . . . . . . . . . . . . . . . . . . . . . 395
16.34Add color on legend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396
16.35Removing Foot Boxes (example for all scale) . . . . . . . . . . . . . . . . . . . . . . . . . 396
16.36Language of the calendar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398
16.36.1 English (en, by default). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398
16.36.2 Deutsch (de) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 399
16.36.3 Japanese (ja) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 399
16.36.4 Chinese (zh) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 400
16.36.5 Korean (ko) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 400
16.37Delete Tasks or Milestones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 400
16.38Start a project, a task or a milestone a number of days before or after today . . . . . . . . 401
16.39Change Label position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
16.39.1 The labels are near elements (by default). . . . . . . . . . . . . . . . . . . . . . . . 401
16.39.2 Label on first column . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402
16.39.3 Label on last column . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403
17 MindMap 405
17.1 OrgMode syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 405
17.2 Markdown syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406
17.3 Arithmetic notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406
17.4 Multilines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
17.5 Multiroot Mindmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 408
17.6 Colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
17.6.1 With inline color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
17.6.2 With style color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 410
17.7 Removing box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412
17.8 Changing diagram direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 413
17.9 Change (whole) diagram orientation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 413
17.9.1 Left to right direction (by default). . . . . . . . . . . . . . . . . . . . . . . . . . . 414
17.9.2 Top to bottom direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 414
17.9.3 Right to left direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 414
17.9.4 Bottom to top direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 415
17.10Complete example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 415
17.11Changing style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 416
17.11.1 node, depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 416
17.11.2 boxless . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417
17.12Word Wrap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418
17.13Creole on Mindmap diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 419
18 Work Breakdown Structure (WBS) 422
18.1 OrgMode syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422
PlantUML Language Reference Guide (1.2025.0) 601 / 606
CONTENTS CONTENTS
18.2 Change direction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
18.3 Arithmetic notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
18.4 Multilines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 424
18.5 Removing box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 424
18.5.1 Boxless on Arithmetic notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
18.5.2 Several boxless node . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
18.5.3 All boxless node . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
18.5.4 Boxless on OrgMode syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426
18.5.5 Several boxless node . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426
18.5.6 All boxless node . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426
18.6 Colors (with inline or style color) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 427
18.7 Using style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 428
18.8 Word Wrap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
18.9 Add arrows between WBS elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 431
18.10Creole on WBS diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432
19 Maths 434
19.1 Standalone diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
19.2 How is this working? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
20 Information Engineering Diagrams 436
20.1 Information Engineering Relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436
20.2 Entities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436
20.3 Complete Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
21 Common Commands in PlantUML 440
21.0.1 Global Elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
21.0.2 Creole Syntax Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
21.0.3 Style Control Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
21.1 Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
21.1.1 Simple comment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
21.1.2 Block comment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
21.1.3 Full example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441
21.2 Zoom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441
21.3 Title . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442
21.4 Caption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443
21.5 Footer and header . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443
21.6 Legend the diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 444
21.7 Appendix: Examples on all diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 444
21.7.1 Activity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 444
21.7.2 Archimate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 445
21.7.3 Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 446
21.7.4 Component, Deployment, Use-Case . . . . . . . . . . . . . . . . . . . . . . . . . . . 446
21.7.5 Gantt project planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 447
21.7.6 Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 447
21.7.7 MindMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 448
21.7.8 Network (nwdiag) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 449
21.7.9 Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 449
21.7.10 State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 450
21.7.11 Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451
21.7.12 Work Breakdown Structure (WBS) . . . . . . . . . . . . . . . . . . . . . . . . . . . 451
21.7.13 Wireframe (SALT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 452
21.8 Appendix: Examples on all diagram with style . . . . . . . . . . . . . . . . . . . . . . . . 453
21.8.1 Activity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
21.8.2 Archimate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
21.8.3 Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 456
21.8.4 Component, Deployment, Use-Case . . . . . . . . . . . . . . . . . . . . . . . . . . . 458
21.8.5 Gantt project planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
21.8.6 Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461
PlantUML Language Reference Guide (1.2025.0) 602 / 606
CONTENTS CONTENTS
21.8.7 MindMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 462
21.8.8 Network (nwdiag) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 463
21.8.9 Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 465
21.8.10 State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 466
21.8.11 Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
21.8.12 Work Breakdown Structure (WBS) . . . . . . . . . . . . . . . . . . . . . . . . . . . 469
21.8.13 Wireframe (SALT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 470
21.9 Mainframe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 471
21.10Appendix: Examples of Mainframe on all diagram . . . . . . . . . . . . . . . . . . . . . . 472
21.10.1 Activity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 472
21.10.2 Archimate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 472
21.10.3 Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 473
21.10.4 Component, Deployment, Use-Case . . . . . . . . . . . . . . . . . . . . . . . . . . . 473
21.10.5 Gantt project planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 473
21.10.6 Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474
21.10.7 MindMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474
21.10.8 Network (nwdiag) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474
21.10.9 Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 475
21.10.10State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 475
21.10.11Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 475
21.10.12Work Breakdown Structure (WBS) . . . . . . . . . . . . . . . . . . . . . . . . . . . 476
21.10.13Wireframe (SALT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 476
21.11Appendix: Examples of title, header, footer, caption, legend and mainframe on all diagram 477
21.11.1 Activity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 477
21.11.2 Archimate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 477
21.11.3 Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478
21.11.4 Component, Deployment, Use-Case . . . . . . . . . . . . . . . . . . . . . . . . . . . 479
21.11.5 Gantt project planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479
21.11.6 Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
21.11.7 MindMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481
21.11.8 Network (nwdiag) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481
21.11.9 Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482
21.11.10State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 483
21.11.11Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 483
21.11.12Work Breakdown Structure (WBS) . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
21.11.13Wireframe (SALT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 485
22 Creole 487
22.1 Emphasized text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487
22.2 Lists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487
22.3 Escape character . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 488
22.4 Headings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 488
22.5 Emoji . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489
22.5.1 Unicode block 26 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489
22.6 Horizontal lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490
22.7 Links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491
22.8 Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491
22.9 Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492
22.9.1 Create a table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492
22.9.2 Align fields using Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493
22.9.3 Add color on rows or cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
22.9.4 Add color on border and text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
22.9.5 No border or same color as the background . . . . . . . . . . . . . . . . . . . . . . 495
22.9.6 Bold header or not . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
22.10Tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496
22.11Special characters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 498
22.12Legacy HTML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 499
22.12.1 Common HTML element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500
PlantUML Language Reference Guide (1.2025.0) 603 / 606
CONTENTS CONTENTS
22.12.2 Subscript and Superscript element [sub, sup] . . . . . . . . . . . . . . . . . . . . . 501
22.13OpenIconic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 501
22.14Appendix: Examples of ”Creole List” on all diagrams . . . . . . . . . . . . . . . . . . . . 502
22.14.1 Activity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502
22.14.2 Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 503
22.14.3 Component, Deployment, Use-Case . . . . . . . . . . . . . . . . . . . . . . . . . . . 504
22.14.4 Gantt project planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505
22.14.5 Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505
22.14.6 MindMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 506
22.14.7 Network (nwdiag) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 506
22.14.8 Note . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
22.14.9 Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
22.14.10State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 508
22.14.11WBS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509
22.15Appendix: Examples of ”Creole horizontal lines” on all diagrams . . . . . . . . . . . . . . 510
22.15.1 Activity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 510
22.15.2 Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511
22.15.3 Component, Deployment, Use-Case . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
22.15.4 Gantt project planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 513
22.15.5 Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 513
22.15.6 MindMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 514
22.15.7 Network (nwdiag) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 515
22.15.8 Note . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 515
22.15.9 Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 516
22.15.10State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 517
22.15.11WBS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 518
22.16Style equivalent (between Creole and HTML) . . . . . . . . . . . . . . . . . . . . . . . . . 519
23 Defining and using sprites 521
23.1 Inline SVG sprite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 521
23.2 Changing colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 523
23.3 Encoding Sprite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 523
23.4 Importing Sprite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 524
23.5 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 524
23.6 StdLib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 525
23.7 Listing Sprites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 525
24 Skinparam command 527
24.1 Usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 527
24.2 Nested . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 527
24.3 Black and White . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 527
24.4 Shadowing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 528
24.5 Reverse colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 528
24.6 Colors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 529
24.7 Font color, name and size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 530
24.8 Text Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 530
24.9 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531
24.10List of all skinparam parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 535
24.10.1 Command Line: -language command . . . . . . . . . . . . . . . . . . . . . . . . . . 535
24.10.2 Command: help skinparams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 535
24.10.3 Command: skinparameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 535
24.10.4 All Skin Parameters on the Ashley’s PlantUML Doc . . . . . . . . . . . . . . . . . 538
25 Preprocessing 539
25.1 Variable definition [=, ?=] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 539
25.2 Boolean expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 540
25.2.1 Boolean representation [0 is false] . . . . . . . . . . . . . . . . . . . . . . . . . . . . 540
25.2.2 Boolean operation and operator [&&, ||, ()] . . . . . . . . . . . . . . . . . . . . . . 540
25.2.3 Boolean builtin functions [%false(), %true(), %not(<exp>), %boolval(<exp>)] . . 540
PlantUML Language Reference Guide (1.2025.0) 604 / 606
CONTENTS CONTENTS
25.3 Conditions [!if, !else, !elseif, !endif] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 540
25.4 While loop [!while, !endwhile] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 541
25.4.1 While loop (on Activity diagram) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 541
25.4.2 While loop (on Mindmap diagram) . . . . . . . . . . . . . . . . . . . . . . . . . . . 542
25.4.3 While loop (on Component/Deployment diagram) . . . . . . . . . . . . . . . . . . 543
25.5 Procedure [!procedure, !endprocedure] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 543
25.6 Return function [!function, !endfunction] . . . . . . . . . . . . . . . . . . . . . . . . . . . . 544
25.7 Default argument value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 545
25.8 Unquoted procedure or function [!unquoted] . . . . . . . . . . . . . . . . . . . . . . . . . . 546
25.9 Keywords arguments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 547
25.10Including files or URL [!include, !include_many, !include_once] . . . . . . . . . . . . . . . 547
25.11Including Subpart [!startsub, !endsub, !includesub] . . . . . . . . . . . . . . . . . . . . . . 548
25.12Builtin functions [%] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 548
25.13Logging [!log] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 549
25.14Memory dump [!dump_memory] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 550
25.15Assertion [!assert] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 550
25.16Building custom library [!import, !include] . . . . . . . . . . . . . . . . . . . . . . . . . . . 551
25.17Search path . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 551
25.18Argument concatenation [##] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 551
25.19Dynamic invocation [%invoke_procedure(), %call_user_func()] . . . . . . . . . . . . . 552
25.20Evaluation of addition depending of data types [+] . . . . . . . . . . . . . . . . . . . . . . 553
25.21Preprocessing JSON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 553
25.22Including theme [!theme] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 553
25.23Migration notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 554
25.24%splitstr builtin function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 554
25.25%splitstr_regex builtin function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 555
25.26%get_all_theme builtin function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 556
25.27%get_all_stdlib builtin function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 557
25.27.1 Compact version (only standard library name) . . . . . . . . . . . . . . . . . . . . 557
25.27.2 Detailed version (with version and source) . . . . . . . . . . . . . . . . . . . . . . . 557
25.28%random builtin function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 559
25.29%boolval builtin function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 559
26 Unicode 560
26.1 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 560
26.2 Charset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 562
26.3 Using Unicode Character on PlantUML . . . . . . . . . . . . . . . . . . . . . . . . . . . . 562
27 PlantUML Standard Library 563
27.0.1 Standard Library Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 563
27.0.2 Contribution from the Community . . . . . . . . . . . . . . . . . . . . . . . . . . . 563
27.1 List of Standard Library . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 563
27.2 ArchiMate [archimate] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 565
27.2.1 List possible sprites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 566
27.3 Amazon Labs AWS Library [awslib] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 567
27.4 Azure library [azure] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 568
27.5 C4 Library [C4] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 569
27.6 Cloud Insight [cloudinsight] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 569
27.7 Cloudogu [cloudogu] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 570
27.8 EDGY: An Open Source tool for collaborative Enterprise Design [edgy] . . . . . . . . . . 571
27.8.1 Basic Elements and Interconnections . . . . . . . . . . . . . . . . . . . . . . . . . . 571
27.8.2 Elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 572
27.8.3 Relationships . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 573
27.8.4 Facets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 574
27.8.5 Identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 574
27.8.6 Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 574
27.8.7 Experience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 575
27.8.8 Intersections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 575
27.8.9 Alternative visual styling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 576
PlantUML Language Reference Guide (1.2025.0) 605 / 606
CONTENTS CONTENTS
27.9 Elastic library [elastic] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 577
27.10Google Material Icons [material] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 579
27.11Kubernetes [kubernetes] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 580
27.12Logos [logos] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 581
27.13Oﬀice [oﬀice] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 583
27.14Open Security Architecture (OSA) [osa] . . . . . . . . . . . . . . . . . . . . . . . . . . . . 585
27.15Tupadr3 library [tupadr3] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 588
27.16AWS library [aws] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 589