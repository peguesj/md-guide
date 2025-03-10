## Backslash deprecation and introduction of new functions  

Starting with version **V1.2025.1**, PlantUML is undergoing changes to enhance language consistency and ensure long-term maintainability. As part of this evolution, certain escape sequences that rely on the backslash (`\\`) will be deprecated in favor of clearer, more descriptive functions. This document outlines these changes and how to adapt your diagrams accordingly.  

In the near future, the backslash (`\\`) will be treated as a regular character, just like any other, and will no longer play a special role in escape sequences.  

If your diagrams currently rely on the deprecated backslash-based sequences, upcoming versions of PlantUML will display warnings to encourage transitioning to the new functions. These warnings are intended to assist in a smooth migration process and ensure your diagrams remain functional.  


## Deprecation of backslash escape sequences  

The following backslash escape sequences, commonly used in PlantUML diagrams, will be **deprecated** in future releases:  

| Escape sequence | Replacement function       | Description                                      |
| --------------- | -------------------------- | ------------------------------------------------ |
| ``\n``          | ``%n()`` or ``%newline()`` | Inserts a **line break**.                        |
| ``\l``          | ``%left_align()``          | Aligns text to the **left** in labels or notes.  |
| ``\r``          | ``%right_align()``         | Aligns text to the **right** in labels or notes. |
| ``\t``          | ``%tab()``                 | Inserts a **tabulation** character.              |
| ``\\``          | ``%backslash()``           | Inserts a literal **backslash** character.       |


> The functions ``%n()`` and ``%newline()`` are strictly equivalent, so you can choose the one you prefer based on your personal style.


## Why these changes?  

**Consistency**: Backslashes are currently overloaded with multiple meanings depending on the context. Treating backslashes as regular characters removes this ambiguity, making the language more intuitive.  

**Simplicity**: Removing the special behavior of the backslash simplifies the PlantUML syntax, making it easier to understand and use, especially for new users.  

**Readability**: The new, descriptive functions like `%newline()` and `%tab()` explicitly indicate their purpose, improving the clarity and maintainability of PlantUML scripts.  

**Future-proofing**: By removing overloaded backslash escape sequences, we reduce ambiguity in the language, paving the way for a cleaner and more robust syntax.  

**Flexibility**: The new functions provide a more descriptive and self-explanatory approach, making it easier to extend and adapt PlantUML in future versions.  

**Cross-Compatibility**: Many programming languages use the backslash as an escape character, which can create issues when mixing PlantUML scripts with these languages. Treating the backslash as a regular character in PlantUML helps avoid conflicts and makes it easier to integrate with other tools and workflows.  

### Motivation and future developments

These changes are also part of a broader initiative to refactor PlantUML's Java codebase and prepare for new features. One of the primary goals is to introduce robust [multiline support](https://github.com/plantuml/plantuml/issues/1985), addressing long-standing issues with line breaks in various diagram elements. This enhancement will significantly improve the flexibility and readability of complex diagrams.

Additionally, PlantUML is expanding its horizons beyond its current Creole-based syntax. The development team is working on implementing support for alternative markup languages, with a particular focus on Markdown integration. This move towards syntax diversity will make PlantUML more accessible to users familiar with other documentation formats and enhance its interoperability with existing tools and workflows.


## How to update your diagrams  

To prepare for this transition, replace the old escape sequences with their corresponding functions:  

**Before :**

```
Alice -> Bob : Hello\nHow are you?
note left: This is a\ntest
```

**After :**

```
Alice -> Bob : Hello%n()How are you?
note left: This is a%n()test
```


## Introducing the `%breakline()` function  

As part of the effort to make PlantUML's syntax clearer and more robust, a new function `%breakline()` has been introduced.  

The `%breakline()` function explicitly creates a **new line** in the **source code**, meaning it behaves as if you had pressed "Enter" to start a new line in your PlantUML script. This is different from `%n()` or `%newline()`, which only affect how text is rendered in the output diagram.  

You should use `%breakline()` when you need to split long pieces of code or dynamically generate source lines in your PlantUML scripts. It is particularly useful in preprocessor functions or macros that return multi-line outputs.  

For example:  
```plantuml
@startuml
!function $message()
  !return "Alice -> Bob : Hello" + %breakline() + "Bob -> Alice : Hi!"
!endfunction

$message()
@enduml
```

In this example, `%breakline()` splits the PlantUML source code into multiple lines, resulting in a diagram where the interactions are processed correctly as separate instructions.  

### How is `%breakline()` different from `%n()` or `%newline()`?  

- `%n()` or `%newline()`: These functions create line breaks in **rendered text**. For example, they are used to format labels, notes, or text displayed in diagrams.  
- `%breakline()`: This function creates a line break in the **PlantUML source code**, affecting how the script is interpreted.  

#### Comparison example  

Here is a side-by-side comparison:  

```
@startuml
' Using %n() to insert a line break in text
Alice -> Bob : Hello%n()How are you?

' Using %breakline() to split source code into two lines
Alice -> Bob : Hello %breakline()Bob -> Alice : Hi!
@enduml
```


- In the first example, `%n()` affects how the message is rendered in the diagram.  
- In the second example, `%breakline()` affects how the script is interpreted, splitting it into two separate interactions. This second example is quite artificial; `%breakline()` is more commonly used in preprocessor functions.

### Why introduce `%breakline()`?  

Previously, certain functionalities relied on escape sequences like `\\n` or ambiguous behaviors when working with line breaks in source code.

The introduction of `%breakline()` provides a clean, explicit, and predictable way to handle source-level line breaks, reducing confusion and ensuring consistency in future versions of PlantUML.  


## Timeline and plan for backslash deprecation


| Version                | Release status | Backslash escape ``\``                    | ``%newline()``, ``%n()``, ... | ``%breakline()`` | Notes                                                                                    |
| ---------------------- | -------------- | ----------------------------------------- | ----------------------------- | ---------------- | ---------------------------------------------------------------------------------------- |
| V1.2025.0 and before   | 🚀             | ✅ Supported                               | ❌ Not officially supported    | ❌ Not available  | Backslash escape sequences work; new functions are not available.                        |
| V1.2025.1 to V1.2025.2 | 🚀             | ✅ Supported                               | ✅ Supported                   | ✅ Supported      | Both backslash escape sequences and the new functions work. Facilitates migration.       |
| V1.2025.xx ?           | 🚧             | ⚠️ Supported but with warnings            | ✅ Supported                   | ✅ Supported      | Backslash escape sequences work but show a warning encouraging the use of new functions. |
| V1.2025.xx ?           | 🚧             | ❌ Not supported (treated as literal text) | ✅ Supported                   | ✅ Supported      | Backslash escape sequences are no longer recognized and are displayed as-is.             |

**Legend for Release Status**:
* 🚀 **Released**: Already available.  
* 🚧 **Upcoming**: Planned and not available yet.


### Why allow gradual migration?  

Supporting both the old backslash escape sequences and the new functions for a transition period ensures:  

* **Ease of migration**: Users can adapt their diagrams incrementally, without needing to update everything at once.  
* **Backward compatibility**: Existing diagrams will continue to work temporarily, minimizing disruptions for users.  
* **Smooth transition**: The warnings introduced in version V1.2025.2 provide clear guidance, helping users identify and update outdated syntax at their own pace.  
* **Error prevention**: By offering both syntaxes for a time, users can experiment with the new functions in a controlled manner, reducing the risk of introducing errors during updates.  


## Next steps or Opening towards other evolutions

Here are some links for next evolutions:
- [New Proposal](https://github.com/plantuml/plantuml/blob/master/PROPOSAL.md)
- [_Don't hesitate to give your feedback on_ GH-1985](https://github.com/plantuml/plantuml/issues/1985)


