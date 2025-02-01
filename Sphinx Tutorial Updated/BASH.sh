#!/bin/bash  

# Define project variables
PROJECT_NAME="MyProject"  # Put your project name
AUTHOR_NAME="MyAuthor"    # Put your Author names
VERSION="0.0.1"           # Put the version
LANGUAGE="en"             # Put the language

# Create Documentation Directories
if [ -d docs ]; then
    rm -rf docs
fi

mkdir docs

cd docs

# Initialize the Sphinx-Project
sphinx-quickstart <<EOT
y
$PROJECT_NAME
$AUTHOR_NAME
$VERSION
$LANGUAGE
EOT

# Navigate to source directory
cd source

# Append additional configurations to conf.py
cat <<EOF >> conf.py
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
# Enable MathJax for LaTeX equations with dollar signs (\$...\$)
mathjax_config = {
    "tex": {
        "inlineMath": [["\$", "\$"], ["\\\\(", "\\\\)"]],
        "displayMath": [["\$\$", "\$\$"], ["\\\\[", "\\\\]"]]
    }
}

pygments_style = "sphinx"  # Syntax highlighting style
EOF

# Go back to docs directory
cd ..

# Create the rst files
sphinx-apidoc -o source/ ../ --force 

# Modify index.rst to include modules
echo '   modules' >> source/index.rst

# Build documentation in multiple formats
make html 
make latex
make latexpdf

echo "Documentation successfully generated!"
open build/html/index.html
open build/latex/$PROJECT_NAME.pdf
