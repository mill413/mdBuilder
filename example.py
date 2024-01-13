from mdElement import (Bold, Italic, BoldItalic, Code, Strikethrough,
                       Heading, Blockquote, Paragraph, HorizontalRule,
                       FencedCodeBlock, Table, Alignment, Link, Image,
                       OrderedList, UnorderedList,TaskList)
from mdBuilder.MdBuilder import MdBuilder


examples = (
    "Example Simple Text",
    Bold("Example Bold"),
    Italic("Example Italic"),
    BoldItalic("Example Bold and Italic"),
    Code("Example Code"),
    Strikethrough("Example Strikethrough"),
    Heading(1, "Example Heading 1"), Heading(
        2, BoldItalic("Example Heading 2 with Bold and Italic")),
    Blockquote("Example Blockquote",
               Blockquote(Bold("Example Nested Blockquote with Bold"),
                          Heading(1, "Example Nested Heading in Blockquote"))),
    Paragraph("Example Paragraph ", Italic(
        "Example Pagraph with Italic"), " Below is Example HorizontalRule"),
    HorizontalRule(),
    FencedCodeBlock("print(\"Example FencedCodeBlock\")", "python"),
    Table(header=["Header1", Bold("Header2 with Bold"), "Header3"],
          content=[
              ["Left", "Right", "Center"],
              [Bold("Bold"), Italic("Italic"), BoldItalic("Bold and Italic")],
              [Code("Code"), Link(url="mill413.github.io",
                                  text_or_image="Link"), "|"]
    ],
        alignment=[Alignment.LEFT, Alignment.RIGHT, Alignment.CENTER]),
    Link(url="mill413.github.io", text_or_image="Example Link", title="Link Title"),
    Link(url="mill413.github.io", text_or_image=Bold(
        "Example Link with Bold"), title="Link Title with Bold"),
    Link(url="mill413.github.io", text_or_image=Image(
        path_or_url="https://api.kdcc.cn", alt_text="Example Image Link", title="Image Link Title"), title="Link Title"),
    Image(
        path_or_url="https://api.kdcc.cn", alt_text="Example Image", title="Image Title"),
    OrderedList(
        "Example Ordered List",
        ["Example Elements in Ordered List",
         Paragraph("Paragraph"),
         Blockquote("Blockquote"),
         Image(
             path_or_url="https://api.kdcc.cn", alt_text="Image", title="Image Title"),
         OrderedList("Nested Ordered List starting with 2", start_index=2),
         UnorderedList("Nested Unordered List")
        ]
    ),
    UnorderedList(
        "Example Unordered List",
        ["Example Elements in Unordered List",
         Paragraph("Paragraph"),
         Blockquote("Blockquote"),
         Image(
             path_or_url="https://api.kdcc.cn", alt_text="Image", title="Image Title"),
         OrderedList("Nested Ordered List starting with 2", start_index=2),
         UnorderedList("Nested Unordered List")
         ]
    ),
    TaskList(
        "task1",
        ("task2", "x")
    )
)

for e in examples:
    print(e)

mw = MdBuilder(*examples)
mw.write_to_file("./example.md")
