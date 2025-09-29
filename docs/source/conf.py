project = "soen-433-a1"
author = "elion"
release = ""                 # or "0.1.0" if you want a version shown
html_title = "soen-433-a1 documentation"

extensions = [
    "myst_parser",           # enable Markdown support
    # add more later if you want (e.g., "sphinx.ext.autodoc", "sphinx.ext.napoleon")
]

# optional but nice: make .md work explicitly and enable a few MyST extras
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
myst_enable_extensions = ["colon_fence", "deflist", "attrs"]

templates_path = ["_templates"]
exclude_patterns = []
html_theme = "furo"
html_static_path = ["_static"]
