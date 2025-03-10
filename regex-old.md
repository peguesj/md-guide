## Display Regex Data

----
🚧 - *Under construction*

🆕 functionality still in testing stage...
These new features are still under construction 🚧

🚧 - *Under construction*
----

You can use PlantUML to visualize your [Regular expression (Regex)](https://en.wikipedia.org/wiki/Regular_expression).

To activate this feature, the diagram must:
* begin with ``@startregex`` keyword
* end with ``@endregex`` keyword. 

```plantuml
@startregex
title litteralText
abc
@endregex
```
```plantuml
@startregex
title specialLitteralText
\\\^\$\.\|\?\*\+\(\)\[\]\{\}
@endregex
```
```plantuml
@startregex
tite shorthandCharacterClasses
\d\w\s
@endregex
```
```plantuml
@startregex
title litteralCharacterSequence
\Qfoo\E
@endregex
```
```plantuml
@startregex
title range
[0-9]
@endregex
```
```plantuml
@startregex
title anyCharacter
.
@endregex
```
```plantuml
@startregex
title specialEscapes
\t\r\n\a\e\f
@endregex
```
```plantuml
@startregex
title octalEscapes
\0377\337
@endregex
```
```plantuml
@startregex
title unicodeEscapes
\uFFFF\x{FFFF}
@endregex
```
```plantuml
@startregex
title unicodeCategories
letter \p{L}\p{Letter} lower \p{Ll}\p{Lowercase_letter}
@endregex
```
```plantuml
@startregex
title unicodeScripts
latin \p{Latin}
@endregex
```
```plantuml
@startregex
title unicodeBlocks
\p{InGeometric_Shapes}
@endregex
```
↵
### Order
↵
```plantuml
@startregex
title alternation
a|b
@endregex
```
```plantuml
@startregex
title optional
ab?
@endregex
```
```plantuml
@startregex
title requiredRepetition
ab+
@endregex
```
```plantuml
@startregex
title optionalRepetition
ab*
@endregex
```
```plantuml
@startregex
title rangeRepetition
ab{1,2}
@endregex
```
```plantuml
@startregex
title minimumRepetition
ab{1}c{1,}
@endregex
```
```plantuml
@startregex
title repetitionEquivalance
a{0,1}b{1,} is the same as a?b+
@endregex
```
↵
### Miscellaneous
↵
```plantuml
@startregex
title stringAnchors
^foo$
@endregex
```
```plantuml
@startregex
title wordBoundries
\bword\b
@endregex
```
```plantuml
@startregex
title namedGroups
a(?<number>\d+)b
@endregex
```
```plantuml
@startregex
title comments
\d(?#any diget)
@endregex
```

Ref.:
* [Regex on GH@plantuml/plantuml](https://github.com/plantuml/plantuml/tree/master/src/net/sourceforge/plantuml/regex)
* [QA-17112](https://forum.plantuml.net/17112/regex-railroad-diagrams)
* [QA-17357](https://forum.plantuml.net/17357/documentation-of-hcl-and-regex)


