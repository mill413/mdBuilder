# mdBuilder

![PyPI - Version](https://img.shields.io/pypi/v/mdBuilder)

## NOTICE

This library is just a **TOY PROJECT**!

DON'T use it in production environment!

## Installation

```python
pip install mdBuilder
```

## Usage

### Basic Syntax

#### 1. Headings

Markdown:

```markdown
# Heading level 1
## Heading level 2
### Heading level 3  
#### Heading level 4  
##### Heading level 5  
###### Heading level 6
```

Python:

```Python
Heading(1, "Heading level 1")
Heading(2, "Heading level 2")
Heading(3, "Heading level 3")
Heading(4, "Heading level 4")
Heading(5, "Heading level 5")
Heading(6, "Heading level 6")
```

#### 2. Paragraphs

Markdown:

```markdown
I really like using Markdown.

I think I'll use it to format all of my documents from now on. 
```

Python:

```Python
Paragraph("I really like using Markdown.")
Paragraph("I think I'll use it to format all of my documents from now on.")
```

#### 3. Emphasis

##### 3.1 Bold

Markdown:

```markdown
I just love **bold text**.
Love**is**bold
```

Python:

```Python
Paragraph("I just love ", Bold("bold text"), ".")
Paragraph("Love", Bold("is"), "bold")
```

##### 3.2 Italic

Markdown:

```markdown
Italicized text is the *cat's meow*.
A*cat*meow
```

Python:

```Python
Paragraph("Italicized text is the ", Italic("cat's meow"), ".")
Paragraph("A", Italic("cat"), "meow")
```

##### 3.3 Bold and Italic

Markdown:

```markdown
This text is ***really important***.
This is really***very***important text.
```

Python:

```Python
Paragraph("This text is ", BoldItalic("really important"), ".")
Paragraph("This is really", BoldItalic("very"), "important text.")
```

#### 4. Blockquotes

Markdown:

```markdown
> Dorothy followed her through many of the beautiful rooms in her castle.
```

Python:

```Python
Blockquote("Dorothy followed her through many of the beautiful rooms in her castle.")
```

##### 4.1 Blockquotes with Multiple Paragraphs

Markdown:

```markdown
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

Python:

```Python
Blockquote(
    "Dorothy followed her through many of the beautiful rooms in her castle.", 
    "The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.")
```

##### 4.2 Nested Blockquotes

Markdown:

```markdown
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

Python:

```Python
Blockquote(
    "Dorothy followed her through many of the beautiful rooms in her castle.", 
    Blockquote("The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood."))
```

##### 4.3 Blockquotes with Other Elements

Markdown:

```markdown
> #### The quarterly results look great!
>
> * Revenue was off the chart.
> * Profits were higher than ever.
>
>  *Everything* is going according to **plan**.
```

Python:

```Python
Blockquote(
    Heading(4, "The quarterly results look great!"),
    UnorderedList(
        "Revenue was off the chart.",
        "Profits were higher than ever."
    ),
    Paragraph(Italic("Everything"), " is going according to ", Bold("plan"), ".")
)
```

#### 5. Lists

##### 5.1 Ordered Lists

Markdown:

```markdown
1. First item
2. Second item
3. Third item
4. Fourth item 

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item 
```

Python:

```Python
OrderedList(
    "First item",
    "Second item",
    "Third item",
    "Fourth item"
)

OrderedList(
    "First item",
    "Second item",
    ["Third item",
    OrderedList(
        "Indented item",
        "Indented item")],
    "Fourth item"
)
```

##### 5.2 Unordered Lists

Markdown:

```markdown
* First item
* Second item
* Third item
* Fourth item 

* First item
* Second item
* Third item
    * Indented item
    * Indented item
* Fourth item 
```

Python:

```Python
UnorderedList(
    "First item",
    "Second item",
    "Third item",
    "Fourth item"
)

UnorderedList(
    "First item",
    "Second item",
    ["Third item",
    UnorderedList(
        "Indented item",
        "Indented item")],
    "Fourth item"
)
```

##### 5.3 Adding Elements in Lists

###### 5.3.1 Paragraphs

Markdown:

```markdown
* This is the first list item.
* Here's the second list item.

    I need to add another paragraph below the second list item.

* And here's the third list item.
```

Python:

```Python
UnorderedList(
    "This is the first list item.",
    ["Here's the second list item.",
    Paragraph("I need to add another paragraph below the second list item.")],
    "And here's the third list item."
)
```

###### 5.3.2 Blockquotes

Markdown:

```markdown
* This is the first list item.
* Here's the second list item.

    > A blockquote would look great below the second list item.

* And here's the third list item.
```

Python:

```Python
UnorderedList(
    "This is the first list item.",
    ["Here's the second list item.",
    Blockquote("A blockquote would look great below the second list item.")],
    "And here's the third list item."
)
```

###### 5.3.3 Images

Markdown:

```markdown
1. Open the file containing the Linux mascot.
2. Marvel at its beauty.

    ![Tux, the Linux mascot](/assets/images/tux.png)

3. Close the file.
```

Python:

```Python
OrderedList(
    "Open the file containing the Linux mascot.",
    ["Marvel at its beauty.",
    Image(path_or_url="/assets/images/tux.png", alt_text="Tux, the Linux mascot")],
    "Close the file."
)
```

###### 5.3.4 Lists

Markdown:

```markdown
1. First item
2. Second item
3. Third item
    * Indented item
    * Indented item
4. Fourth item
```

Python:

```Python
OrderedList(
    "First item",
    "Second item",
    ["Third item",
    UnorderedList(
        "Indented item",
        "Indented item"
    )],
    "Fourth item"
)
```

#### 6. Code

Markdown:

```markdown
At the command prompt, type `nano`.
```

Python:

```Python
Paragraph("At the command prompt, type ", Code("nano"), ".")
```

#### 7. Horizontal Rules

Markdown:

```markdown
---
```

Python:

```Python
HorizontalRule()
```

#### 8. Links

Markdown:

```markdown
My favorite search engine is [Duck Duck Go](https://duckduckgo.com).
```

Python:

```Python
Paragraph("My favorite search engine is ",
          Link(url="https://duckduckgo.com", text_or_image="Duck Duck Go"),
          ".")
```

##### 8.1 Adding Titles

Markdown:

```markdown
My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").
```

Python:

```Python
Paragraph("My favorite search engine is ",
          Link(url="https://duckduckgo.com", 
               text_or_image="Duck Duck Go", 
               title="The best search engine for privacy"),
          ".")
```

##### 8.2 URLs and Email Addresses

Markdown:

```markdown
<https://www.markdownguide.org>
<fake@example.com>
```

Python:

```Python
Link(url="https://www.markdownguide.org")
Link(url="fake@example.com")
```

##### 8.3 Formatting Links

Markdown:

```markdown
I love supporting the [**EFF**](https://eff.org).
This is the [*Markdown Guide*](https://www.markdownguide.org).
See the section on [`code`](#code).
```

Python:

```Python
Paragraph("I love supporting the ", 
          Link(url="https://eff.org", text_or_image=Bold("EFF")), 
          ".")
Paragraph("This is the ", 
          Link(url="https://www.markdownguide.org", text_or_image=Italic("Markdown Guide")), 
          ".")
Paragraph("See the section on ", 
          Link(url="#code", text_or_image="code"), 
          ".")
```

#### 9. Images

Markdown:

```markdown
![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")

```

Python:

```Python
Image(path_or_url="/assets/images/san-juan-mountains.jpg", alt_text="The San Juan Mountains are beautiful!", title="San Juan Mountains")
```

##### 9.1 Linking Images

Markdown:

```markdown
[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


```

Python:

```Python
Link(
    url="https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv", 
    text_or_image=Image(
        path_or_url="/assets/images/shiprock.jpg", 
        alt_text="ImAn old rock in the desertage", 
        title="Shiprock, New Mexico by Beau Rogers")
)
```

### Extened Syntax

#### 1. Tables

Markdown:

```markdown
| Syntax | Description |
| --- | --- |
| Header | Title |
| Paragraph | Text |
```

Python:

```Python
Table(
    headers=["Syntax", "Description"],
    content=[
        ["Header", "Title"],
        ["Paragraph". "Text"]
    ]
)
```

##### 1.1 Alignment

Markdown:

```markdown
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

Python:

```Python
Table(
    header=["Syntax", "Description", "Test Text"],
    content=[
        ["Header", "Title", "Here's this"],
        ["Paragraph". "Text", "And more"]
    ],
    alignment=[
        Alignment.LEFT,
        Alignment.CENTER,
        Alignment.RIGHT
    ]
)
```

#### 2. Fenced Code Blocks

Markdown:

`````markdown
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
`````

Python:

```Python
FencedCodeBlock(
    "{\n"+
    "  \"firstName\": \"John\"\n"+
    "  \"lastName\": \"Smith\"\n"+
    "  \"age\": 25\n"+
    "}"
)
```

##### 2.1 Syntax Highlighting

Markdown:

`````markdown
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
`````

Python:

```Python
FencedCodeBlock(
    "{\n"+
    "  \"firstName\": \"John\"\n"+
    "  \"lastName\": \"Smith\"\n"+
    "  \"age\": 25\n"+
    "}",
    syntax="json"
)
```

#### 3. Strikethrough

Markdown:

```markdown
~~The world is flat.~~ We now know that the world is round.
```

Python:

```Python
Paragraph(
    Strikethrough("The world is flat."),
     " We now know that the world is round.")
```

#### 4. Task Lists

Markdown:

```markdown
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

Python:

```Python
TaskList(
    ("Write the press release", "x"),
    "Update the website",
    "Contact the media"
)
```

## TODO

- [ ] HTML
- [ ] Heading IDs
- [ ] Definition Lists
- [ ] Highlight
- [ ] Subscript
- [ ] Superscript

## Reference

The markdown string format refers to <https://www.markdownguide.org/>

## LICENSE

This project is published under [MIT License](https://github.com/mill413/mdBuilder/blob/main/LICENSE).
