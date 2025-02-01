# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MyProject'
copyright = '2025, MyAuthor'
author = 'MyAuthor'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Adjust the path if needed

extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    "sphinx.ext.imgmath",
    "sphinx.ext.mathjax"
]

latex_engine = "pdflatex"  # Or 'xelatex', 'lualatex'

latex_elements = {
    "papersize": "a4paper",
    'extrapackages': r'\usepackage{fancyhdr}',
    'fontpkg': r'''
        \usepackage{palatino}
    ''',
    'printindex': '',
    'classoptions': ',oneside',
    'extraclassoptions': 'openany',
    "pointsize": "14pt",
    "preamble": r"""
        \usepackage{palatino} 
	\usepackage{amsmath,amssymb}
	 
        \usepackage{fvextra}  % Better verbatim environments
    """
    
}

# TEX Configuration
# Enable MathJax for LaTeX equations with dollar signs ($...$)
mathjax_config = {
    "tex": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]]
    }
}

pygments_style = "sphinx"  # Syntax highlighting style
