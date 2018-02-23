from flask_nemo.chunker import level_grouper

def scheme_grouper(text, getreffs):
    level = len(text.citation)
    groupby = 5
    types = [citation.name for citation in text.citation]

    if types == ["book", "poem", "line"]:
        level, groupby = 2, 1
    elif types == ["book", "line"]:
        level, groupby = 2, 30
    elif types == ["book", "chapter"]:
        level, groupby = 2, 1
    elif types == ["book"]:
        level, groupby = 1, 1
    elif types == ["line"]:
        level, groupby = 1, 30
    elif types == ["chapter", "section"]:
        level, groupby = 2, 2
    elif "line" in types:
        groupby = 30
    return level_grouper(text, getreffs, level, groupby)

nemo_config = {
    "chunker": {
        "default": scheme_grouper
    },
    "css": [
        "/code/static/assets/nemo.secondary/css/theme-ext.css"
    ],
    "transform": {
        "default": "/code/static/assets/xslt/epidocShort.xsl"
    },
    "templates": {
        "passage_footer": "./config/templates/passage_footer_custom.html"
    }
}
