## Documentation for the custom Bracketed Expression Engine (brackex)

This engine uses a non-standard syntax based on specific symbols to define character sets, quantifiers, groups, alternatives, and classes.

These expressions are known as **bracketed expressions** or **brackex** for short. The documentation below details the current syntax design.


## Standard Characters

In brackex, only a **select few** characters from the Unicode blocks `U+2200`, `U+2500`, and `U+3000` are used as special syntax elements. As a result, **most standard characters are interpreted literally** and do not require escaping.  

Additionally, the standard space character (`U+0020`) is **completely ignored by the syntax**, allowing you to freely insert spaces for better readability. If you need to **match an actual space**, use the **literal space character** `∙`.

You can also use `〃` as a remplacement for `"`. This avoid escaping double quotes in Java strings.

---

### **Example**  

#### **Pattern:**  
```
This∙is∙a∙star∙*∙and∙2∙+∙3∙=∙4
```
#### **Matches exactly:**  
```
This is a star * and 2 + 3 = 4
```
**Explanation:**  
- **The `∙` symbol explicitly represents a literal space**, ensuring the pattern matches spaces in the target text.  
- **Special symbols (`*`, `+`, `=`)** are treated as literals and do not require escaping.  


## Character sets

Character sets allow you to specify, for a given position in a string, a defined set of characters that are either allowed or disallowed.

### Simple Set

**Syntax:**  
```
「…」
```

**Example:**  
```
「abced0123」
```

**Description:**  
All characters enclosed within `「` and `」` form the **allowed set** for that position.

---

### Range

**Syntax:**  
```
「char1〜char2」
```

**Example:**  
```
「a〜c」
```

**Description:**  
The `〜` symbol defines a range. In this example, all characters from `a` to `c` (inclusive) are accepted.

---

### Negative Set

**Syntax:**  
```
「〤…」
```

**Example:**  
```
「〤a〜c」
```

**Description:**  
The prefix `〤` denotes a **negative set**, meaning that any character **except** those between `a` and `c` will be matched.

---

### Combining Elements

Character sets can combine explicit characters, ranges, and negative sets.

#### Example 1:
```
「〤abcedf0〜9」
```

**Description:**  
This **negative set** excludes characters `a`, `b`, `c`, `e`, `d`, `f`, and all digits from `0` to `9`. Any other character is accepted.

#### Example 2:
```
「a〜z〤fi〜k」
```

**Description:**  
This set allows **all lowercase letters from `a` to `z`** except `f`, `i`, `j`, and `k`, which are explicitly excluded.

---

### Summary

- Use `「...」` to define an **allowed set**.
- Use `「char1〜char2」` to define a **range**.
- Use `「〤...」` to define a **negative set** (excluding specified characters).
- You can **combine explicit characters, ranges, and exclusions** within a single set.


## Predefined classes

Predefined classes allow you to reference commonly used character sets using the symbol `〴` followed by an identifier. These provide shorthand representations for frequently used character groups.

Additionally, using **uppercase identifiers negates the class**, meaning it matches **everything except** the specified set.  


---

### **`〴w`** – Word Characters  
**Description:**  
Matches **word characters**, including **letters, digits, and underscore (`_`)**, similar to `\w` in traditional regex. 

### **`〴d`** – Digits  
**Description:**  
Matches any **digit (`0-9`)**, equivalent to `\d` in traditional regex.  

### **`〴s`** – Whitespace  
**Description:**  
Matches **whitespace characters**, including **spaces, tabs, and line breaks**, similar to `\s`.  

### **`〴le`** – Unicode Letters  
**Description:**  
Matches **any letter in Unicode**, covering **all alphabets and scripts worldwide**, including Latin (`A-Z`), Cyrillic, Greek, Chinese, Arabic, and more.  

### **`〴an`** – Unicode Alphanumeric Characters  
**Description:**  
Matches **any alphanumeric character in Unicode**, including **letters (`〴le`) and digits (`0-9`)** from all writing systems.  

### **`〴g`** – Double Quotes  
**Description:**  
Matches **any double-quote character in Unicode**, including:  
- **ASCII double quotes**: `"`  
- **Typographic quotes**: `“”`  

### **`〴.`** – Any Character  
**Description:**  
Matches **any character in Unicode**, similar to `.` in traditional regex.  


## Quantifiers

Quantifiers specify how many times a given pattern must occur. In **brackex**, the quantifier symbol `〇` **precedes** the pattern it applies to.

Unlike traditional regular expressions, **brackex quantifiers are [possessive](https://www.regular-expressions.info/possessive.html)**, meaning they do not allow backtracking.

### `〇?` (Optional)  
**Example:**
```
〇?a
```
**Description:**  
The pattern `a` is **optional**, meaning it may appear **0 or 1 time**.

### `〇*` (Zero or more)  
**Example:**
```
〇*a
```
**Description:**  
The pattern `a` may appear **zero or more times**.

### `〇+` (One or more)  
**Example:**
```
〇+a
```
**Description:**  
The pattern `a` must appear **at least once** (one or more times).


### `〇{n}pattern` (Exact count)  
**Example:**  
```
〇{2}a
```
**Description:**  
The pattern `a` must appear **exactly** `n` times (in this case, **2 times**).


### `〇{m-n}pattern` (Range with hyphen)  
**Example:**  
```
〇{1-3}a
```
**Description:**  
The pattern `a` must appear **between `m` and `n` times** (here, **between 1 and 3 times**).

### `〇{m,n}pattern` (Values with comma)  
**Example:**  
```
〇{2,4}a
```
**Description:**  
The pattern `a` must appear **either `m` or `n` times**.

---

### 3.3. Important Notes  

- In **brackex**, the **quantifier always comes before** the pattern it modifies.
- Quantifiers are [possessive](https://www.regular-expressions.info/possessive.html), meaning they do **not** allow backtracking.


## Groups

Groups allow you to combine patterns so that you can apply quantifiers collectively or capture a portion of the match.

### Syntax  
```
〘 … 〙
```
Enclosing a pattern within `〘 … 〙` creates a **group**, enabling **collective processing** of the enclosed pattern.

---

### Examples and Descriptions  

#### Example 1:  
```
a〘〇+b〙c
```
**Description:**  
The pattern `b` is **grouped and quantified** by `〇+`, meaning it must appear **one or more times**. The full pattern matches `a`, followed by **one or more occurrences of `b`**, followed by `c`.

---

#### Example 2:  
```
a 〇+〘bc〙z
```
**Description:**  
The grouped pattern `bc` is quantified by `〇+`, meaning the **sequence `bc` must appear one or more times**. The full pattern matches `a`, followed by **one or more occurrences of `bc`**, followed by `z`.

---

## Important Notes  

- **Grouping applies quantifiers to the entire enclosed pattern** rather than individual characters.  
- Groups can be used to **capture** specific parts of a match for further processing.  
- **Quantifiers precede the group** and apply to the entire enclosed pattern.  


## Logical alternatives

Logical alternatives allow you to specify multiple possible patterns at a given position. This is useful for defining flexible matching conditions.

### Syntax  
```
【 alternative1 ┇ alternative2 ┇ … 】
```
Each **alternative** inside the brackets is separated by `┇`, meaning **any one of the specified alternatives can match**.

---

### Examples and Descriptions  

#### Example 1  
```
a【<┇/┇\】c
```
**Description:**  
Between `a` and `c`, **one of the following must match**: `<`, `/`, or `\`.  
This means the pattern can match `a<c`, `a/c`, or `a\c`.

---

#### Example 2  
```
a【〇{1-2}<┇〇{1-2}/┇〇{1-2}\】c
```
**Description:**  
Each alternative (`<`, `/`, `\`) **must appear between 1 and 2 times**.  
This means the pattern can match:  

- `a<c`
- `a//c`

Each alternative is **quantified independently**.


## Capture

Capture allow you to assign a **name** to a pattern, enabling later reference and retrieval of its matched value. This is useful for extracting, reusing, or processing specific parts of a match.  

---

### **Syntax**  
```
〶$<name>=<pattern>
```
- `〶` indicates the start of a capture.  
- `<name>` assigns a **unique name** to the captured pattern.  
- `=` separates the name from the **pattern to be captured**.  

---

### **Example**  
```
〶$NAME=〇+〴w
```
**Description:**  
The capturenamed **`NAME`** matches and stores a **sequence of one or more word characters** (`〴w`).  

For example, given the input `"hello123"`, this capture group would store `"hello123"` under the identifier **`NAME`**.  

---

## **Key Notes**  
- **Captured values can be referenced later** within the same expression or during post-processing.  
- **Naming ensures clarity** and avoids reliance on positional capture groups found in traditional regex.  
- **Capture groups can be combined** with quantifiers, logical alternatives, and other patterns for advanced matching.  


## Up-to pattern

Since **repetitions in brackex are [possessive](https://www.regular-expressions.info/possessive.html)**, they **do not allow backtracking**. This can sometimes lead to unintended behavior when searching for patterns within a sequence.  

To solve this, **brackex introduces the "up-to" pattern**, which allows matching **everything up to a specific endpoint** while maintaining control over the characters being consumed.  

----

### Basic Syntax
```
〄>[PATTERN]
```
* ``〄>`` instructs the engine to **consume all characters** **until** the specified ``[PATTERN]`` is found.  
* ``[PATTERN]`` is the **stopping condition**—matching stops once this pattern is encountered.  

#### **Pattern:**  
```
a〄>1
```
#### **Input String:**  
```
anything until 1
```
#### **Match Result:**  
```
anything until
```
**Explanation:**  
* The sequence starts with **``a``**.  
* ``〄>`` consumes **everything** **until** it finds ``1``.  
* Matching **stops just before ``1``**, ensuring ``1`` itself is **not included** in the match.  

----

### Advanced Syntax

The basic syntax **accepts any character** until the stop pattern is reached. However, you can also **restrict which characters are consumed** before encountering the stop condition.  

```
〄+[PATTERN1] -> [PATTERN2]
```
* **``[PATTERN1]``**: Specifies the **characters allowed** to be consumed.  
* **``[PATTERN2]``**: Defines the **stop pattern**, matching stops when this pattern is found.  

#### **Pattern:**  
```
〶$NAME=〄+〴w ->〘zend〙
```
#### **Input String:**  
```
abcdzend
```
#### **Match Result:**  
* The capture group **``NAME``** stores ``"abcd"``.  

**Explanation:**  
* ``〄+〴w`` ensures that **only word characters (``〴w``, i.e., letters, digits, and underscores) are consumed**.  
* The pattern **stops at ``"zend"``**, meaning ``"abcd"`` is captured and stored under the group **``NAME``**.  
* ``"zend"`` is **not included** in the match but acts as a boundary.  


## **Key Notes**  
* **"Up-to" patterns provide flexible, efficient searching** for delimiters or boundaries.  
* **They can be refined to consume only specific types of characters**, ensuring more precise matching.  
* **Since quantifiers in brackex are [possessive](https://www.regular-expressions.info/possessive.html)**, "up-to" patterns prevent overconsumption by clearly defining stop conditions.  


## General considerations

### Use of Unicode U+3000 Separators

A key design choice in the brackex syntax is the use of separator characters from the Unicode block [U+3000 CJK Symbols and Punctuation](https://en.wikipedia.org/wiki/CJK_Symbols_and_Punctuation). Two characters from the ``U+2200`` block (``∙``) and the ``U+2500`` block (``┋``) are also employed.

Although this approach may occasionally require **copying and pasting specific symbols**, it greatly enhances readability by reducing the need to escape common ASCII characters and minimizing visual clutter.

Moreover, in practice, **we tend to read regex and brackex far more often than we write them**. This means that **optimizing for readability is more important than optimizing for ease of writing**. A syntax that is visually clear and easy to interpret reduces errors, improves maintainability, and enhances collaboration—making it a more efficient long-term choice despite a slightly higher initial input effort.

### Summary of Symbols and Delimiters

| Symbol/Delimiter    | Usage                                                       |
| ------------------- | ----------------------------------------------------------- |
| ``∙``               | Represents a literal space character                        |
| ``〃``               | Represents a standard *double quote* character ``"``        |
| ``〴``               | Introduces a predefined class                               |
| ``「 … 」``           | Delimits a set of characters or a range                     |
| ``〤``               | Prefix indicating a negative set                            |
| ``〜``               | Separates the start and end of a character range            |
| ``〇``               | Introduces a quantifier (optional, \*, +, {…})              |
| ``〄``               | Introduces a *up-to* pattern                                |
| ``〶``               | Marks the beginning of a named capture                      |
| ``〘 … 〙``           | Delimits a group                                            |
| ``【 … 】``           | Delimits a set of alternatives                              |
| ``┇``               | Separates alternatives within an alternative set            |



* **Extensions and Evolution:**  
  This documentation describes the syntax as currently implemented. Future adjustments or extensions may be introduced based on evolving requirements and user feedback.


