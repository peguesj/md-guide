## Deployment (Component, Use-case, and Deployment) Diagram issues (deployment-diagram-issues)

This page lists issues on:
* [deployment-diagram](deployment-diagram);
* [component-diagram](component-diagram);
* [use-case-diagram](use-case-diagram).


## Issues with hexagon 

* [QA-13027/link-arrow-does-not-lead-to-the-hexagon](https://forum.plantuml.net/13027/)
```plantuml
@startuml
hexagon H1 {
node n1
}
[C]

C --> H1: doesn't lead\n to hexagon H1
@enduml
```

* [QA-12835/accept-hexagon-element-without-overflow-deployment-diagram](https://forum.plantuml.net/12835)
```plantuml
@startuml
hexagon h {
node #pink "VeryLOOOOOOOOOOOOOOOOOOOg\nVeryLOOOOOOOOOOOOOOOOOOOg\nVeryLOOOOOOOOOOOOOOOOOOOg\nVeryLOOOOOOOOOOOOOOOOOOOg\nVeryLOOOOOOOOOOOOOOOOOOOg"
}
footer Observed on    : 1.2021.01beta3\n(current version: %version())
@enduml
```

* [QA-13021/accept-hexagon-with-smetana-deployment-diagram](https://forum.plantuml.net/13021/accept-hexagon-with-smetana-deployment-diagram)
```plantuml
@startuml
!pragma layout smetana
hexagon h [
more
and
more
combinatorial
]
@enduml
```

* [QA-13261/accept-hexagon-on-style-deployment-diagram](https://forum.plantuml.net/13261/accept-hexagon-on-style-deployment-diagram) [fixed on V1.2022.01+]
```plantuml
@startuml
<style>
hexagon {
  BackGroundColor palegreen
  LineThickness 2
  LineColor red
}
</style>
hexagon hexagon
hexagon h_OK {
}
hexagon h_KO {
node n
}
@enduml
```


## Line thickness issue (from ~V1.2022.2) [fixed on 1.2022.6betaX]

```plantuml
@startuml
title Bracketed line thickness
node foo
foo --> bar                 : ∅
foo -[thickness=1]-> bar1   : [1]
foo -[thickness=2]-> bar2   : [2]
foo -[thickness=4]-> bar3   : [4]
foo -[thickness=8]-> bar4   : [8]
foo -[thickness=16]-> bar5  : [16]
@enduml
```

*[Adapted from [QA-4949](https://forum.plantuml.net/4949)]*


## The issues below are fixed

The issues below are fixed with:
* [QA-15386](https://forum.plantuml.net/15386/allow-new-styling-for-nested-package)


## Style on no empty nested element

* [QA-14189](https://forum.plantuml.net/14189/using-skinparam-fontproperties-groups-component-diagrams)
* [QA-14179](https://forum.plantuml.net/14179/style-manage-style-dashed-dotted-nested-element-deployment)
```plantuml
@startuml
<style>
node {
  BackGroundColor palegreen
  LineThickness 2
  LineColor red
}
package {
  BackGroundColor palegreen
  LineThickness 2
  LineColor red
}
</style>
package package
package package_empty_nested {
}
package package_nested {
node n
}
node node
node node_empty_nested {
}
node node_nested {
node m
}
footer \nObserved on    : 1.2021.9beta2\n(current version: %version())
@enduml
```

```plantuml
@startuml
<style>
artifact {
  BackGroundColor #ee1100
  LineThickness 1
  LineColor black
}
card {
  BackGroundColor #ff3311
  LineThickness 1
  LineColor black
}
cloud {
  BackGroundColor #ff4422
  LineThickness 1
  LineColor black
}
component {
  BackGroundColor #ff6644
  LineThickness 1
  LineColor black
}
database {
  BackGroundColor #ff9933
  LineThickness 1
  LineColor black
}
file {
  BackGroundColor #feae2d
  LineThickness 1
  LineColor black
}
folder {
  BackGroundColor #ccbb33
  LineThickness 1
  LineColor black
}
frame {
  BackGroundColor #d0c310
  LineThickness 1
  LineColor black
}
hexagon {
  BackGroundColor #aacc22
  LineThickness 1
  LineColor black
}
node {
  BackGroundColor #22ccaa
  LineThickness 1
  LineColor black
}
package {
  BackGroundColor #12bdb9
  LineThickness 1
  LineColor black
}
queue {
  BackGroundColor #11aabb
  LineThickness 1
  LineColor black
}
rectangle {
  BackGroundColor #4444dd
  LineThickness 1
  LineColor black
}
stack {
  BackGroundColor #3311bb
  LineThickness 1
  LineColor black
}
storage {
  BackGroundColor #3b0cbd
  LineThickness 1
  LineColor black
}
</style>
artifact e1 as "artifact" {
file f1
}
card e2 as "card" {
file f2
}
cloud e3 as "cloud" {
file f3
}
component e4 as "component" {
file f4
}
database e5 as "database" {
file f5
}
file e6 as "file" {
file f6
}
folder e7 as "folder" {
file f7
}
frame e8 as "frame" {
file f8
}
hexagon e9 as "hexagon" {
file f9
}
node e10 as "node" {
file f10
}
package e11 as "package" {
file f11
}
queue e12 as "queue" {
file f12
}
rectangle e13 as "rectangle" {
file f13
}
stack e14 as "stack" {
file f14
}
storage e15 as "storage" {
file f15
}
@enduml
```


