## Multiline Management in PlantUML source

### Introduction

This document is intended to serve as a formal specification to address prevalent issues identified in the current implementation of PlantUML, specifically focusing on multiline management. The initiative is a direct follow-up to the discussions and feedback provided in [Issue #1671 on the PlantUML GitHub repository](https://github.com/plantuml/plantuml/issues/1671#issuecomment-1927870607).

### Background

Historically, the development and implementation of multiline management within PlantUML have proceeded without a comprehensive strategic framework or detailed specification. Changes and enhancements have been implemented in an ad hoc manner, based on immediate requirements and community feedback.

### Objective

The primary goal of this specification is to consolidate these efforts, formalizing the approach to multiline management in PlantUML. By doing so, we aim to enhance the tool's usability, reliability, and overall consistency in handling multiline text blocks across various diagram types.

### Call for Contributions

To achieve the objectives outlined in this specification, we invite contributions, insights, and feedback from the PlantUML user community. Your expertise and experiences are invaluable to refining and evolving the multiline management capabilities of PlantUML.


## Current state

* Description of how PlantUML currently handles `backslash-n` for line breaks and multiline text blocks.
* Concrete examples of how users must currently insert line breaks in various elements (like notes, titles, etc.).


## Open questions


### Ending to-be-continued lines with commas

Should we allow to have this ?

```
@startuml
class CImaging {
    +void Init(const ToolConfig& config,
        PolarizedIllumSource& illum_src,
        C3DStructure& structure3d,
        CVectorialProjection& projection );
}
@enduml
```

instead of (which is working today):

```
@startuml
class CImaging {
    +void Init(const ToolConfig& config,\n\
        PolarizedIllumSource& illum_src,\n\
        C3DStructure& structure3d,\n\
        CVectorialProjection& projection );
}
@enduml
```


## Limitations

* Identification and explanation of the limitations of the current approach, including readability issues, editing difficulties, and constraints when integrating with other tools or languages.
* Examples of scenarios where these limitations can hinder the effectiveness or clarity of diagrams.


## Proposed Evolutions

What we do not like and that should be removed:

* `\ `
* `\ n`

What do we like:

* [triple quote strings](https://www.geeksforgeeks.org/triple-quotes-in-python/) (like in Java and Python) *[See also [JEP 378: Text Blocks](https://openjdk.org/jeps/378)]*
* [ending to-be-continued lines with commas](https://docs.python.org/3.10/whatsnew/3.10.html#parenthesized-context-managers)
* the `%newline()` [preprocessing function](https://plantuml.com/en/preprocessing#291cabbe982ff775)


What to write here:

* Detailed proposals for improving multiline management in PlantUML, focusing on consistency, flexibility, and integration.
* Suggestions for improved syntax or new features that could allow for more intuitive management of line breaks and multiline text blocks.
* Discussion on the potential impact of these evolutions on user experience and backward compatibility.


## Related issues or issues in the same topic

- [QA-11343](https://forum.plantuml.net/11343/activity-diagram-multi-line-and-n-management)
- [QA-12480](https://forum.plantuml.net/12480/new-line-in-table-built-with-variables-broken-from-1-2020-20)
- [QA-14510](https://forum.plantuml.net/14510/class-diagram-how-place-the-function-parameters-multiline)
- [QA-10597](https://forum.plantuml.net/10597/preprocessorv2-multiline-function-invocation)
- ...


## _[Historical topic]_ Wiki-Creole

### Creole - How is manage line break on `creole`?

> ``\\`` (wiki-style) for line breaks.
>
> Creole:
>
> ``This is the first line,\\and this is the second.``
>
> Recommended XHTML:
>
> ``This is the first line,<br />``
>
> ``and this is the second.``

*Ref.:*
- [Creole1.0](http://www.wikicreole.org/wiki/Creole1.0)
- [Line breaks in wiki engines](http://www.wikicreole.org/wiki/ParagraphsAndLineBreaksReasoning)


### Creole - Why linebreaks are evil? 

_Ref.:_ [Why linebreaks are evil?](http://www.wikicreole.org/wiki/Talk.ChangeLinebreakMarkupProposal)


## _[Historical Background]_ "Multi-line string literal" on most popular programming languages

Go to:
- [https://www.programming-idioms.org/idiom/48/multi-line-string-literal](https://www.programming-idioms.org/idiom/48/multi-line-string-literal)

Then press `g` key to show a grid with all "Multi-line string literal" on each languages.


