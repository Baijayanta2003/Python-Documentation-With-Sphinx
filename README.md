## Python-Documentation-With-Sphinx
In this I will guide you step by step how to *make* documentation for your python codes and how to produce them in different formats like html or pdf or tex files.

## Here are the steps:

1.First set up a virtual environment by typing the following command in your terminal :

```bash
python -m venv myenv

```
You can give the name for the directory anything instead of myenv. This will create a directiory where your virtual environment will be.

After installing type in command prompt or terminal
```bash
pwd

```
You will see a directory address printed on the window.

This is the directory where you have installed the virtual environment.**(Remember IT)**

2.Now activate the virtual environment using:

```bash
 source myenv/bin/activate
```

`After activation, you should see (myenv) in your command prompt`.

3.Once the virtual environment is activated, you can install packages using `pip`:
```bash
pip install <package_name>
```
install all the packages you need.

4.To deactivate the virtual environment type
```bash
deactivate
```
viola you have successfully installed used and exited the virtual environment.


5.Now get back to work.

Activate the virtual environment myenv by step `2`.

Then navigate to the directory (In my case I have a folder named `Sphinx_Tutorial` where my python scripts are located) 

where the python scripts are located for which you want to make the documentation for .

Alternatively you can navigate to that directory first and 

then activate the virtual environment using this command

```bash
source directory_link/myenv/bin/activate
```

`directory_link` is the directory where you have installed the environment.

6.Install the `Sphinx` with this command:

```bash
pip install sphinx

```
7.My working directory looks like this:
```python
Sphinx_Tutorial/

```
8.Add the files you want to document.
My case Files are `add.py`,`subtract.py`,`multiply.py`.
After this my directory structure is:

```python
Sphinx_Tutorial/
├── add.py
├── multiply.py
└── subtract.py

```

9.Make a new directory using

```bash
mkdir docs
```
10.Change Directory using 
```bash
cd docs
```
11.Type the following command:
```bash
sphinx-quickstart
```
After enter it will show something like this:
```python
Welcome to the Sphinx 7.4.7 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

```
`Type y`

12.It will look like this:
```python
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name:

```
13.Type The name of the project you wanna give,In my case it is `Documenting Python Code with Sphinux`.
After that it will look something like this:
```python
The project name will occur in several places in the built documentation.
> Project name: Documenting Python Code with Sphinux
> Author name(s):
```
14.Type The Author name,Do the next commands and then it will look like this:
 ```python
> Author name(s): Baijaynta Bhattacharyya
> Project release []: '0.0.1'

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: English

Creating file /Sphinx_Tutorial/docs/source/conf.py.
Creating file /Sphinx_Tutorial/docs/source/index.rst.
Creating file /Sphinx_Tutorial/docs/Makefile.
Creating file /Sphinx_Tutorial/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /Users/baijayantabhattacharyya/Sphinux_Tutorial/docs/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```
15.Now the directory looks like:
```python
Sphinx_Tutorial/
├── add.py
├── docs
│   ├── Makefile
│   ├── build
│   ├── make.bat
│   └── source
│       ├── _static
│       ├── _templates
│       ├── conf.py
│       └── index.rst
├── multiply.py
└── subtract.py
```
16.Now type 
```bash
cd source/ 
```
```bash
vi conf.py
```
17.This will look like this:
```python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Documenting Python Code with Sphinux'
copyright = '2025, Baijaynta Bhattacharyya'
author = 'Baijaynta Bhattacharyya'
release = "'0.0.1'"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
                               
```
18.Press `a` or `i` to edit.
In this cut the `extensions = []` and paste:

```bash 
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
```
and also after the line:
```python
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

```
type:
```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Adjust the path if needed

```
19.Finally it will look like this:
```python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Adjust the path if needed

project = 'Documenting Python Code with Sphinux'
copyright = '2025, Baijaynta Bhattacharyya'
author = 'Baijaynta Bhattacharyya'
release = "'0.0.1'"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
templates_path = ['_templates']
exclude_patterns = []

language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
````
Press `esc` and `:wq` to save.

Type 
```bash
cd ..
```
and then

```bash
sphinx-apidoc -o source/ ../ --force

```
20.This command will generate `.rst` files in the `source` folder, one for each Python module, including an index file `(modules.rst)` that lists all the modules.

Now we are nearly done.
Type:

```bash
cd source
```
type 
```bash
vi index.rst
```
And this will look like
```python
.. Documenting Python Code with Sphinux documentation master file, created by
   sphinx-quickstart on Mon Jan 27 15:39:35 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documenting Python Code with Sphinux documentation
==================================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   

```
Press `a` or `i` to edit.
Type `modules` at the end like this:
```bash
.. toctree::
   :maxdepth: 2
   :caption: Contents:


   modules

```
And Press `esc` and `:wq` to save.
Next:
```bash
cd ..
```
```bash
make html

````
21.The following text will appear:
```python
Running Sphinx v7.4.7
loading translations [English]... not available for built-in messages
/myenv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
writing output... 
building [html]: targets for 1 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] index
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
copying assets... 
copying static files... done
copying extra files... done
copying assets: done
writing output... [100%] index
generating indices... genindex py-modindex done
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded.

The HTML pages are in build/html.
```
##You Have created The html file documentation of your python files
22.To view the `html` file type
```bash
cd build/html
```
And Type:
```bash

open index.html
```
23.You will see a html file opening in your default browser.
Final Indexing is:
```python
├── .DS_Store
├── add.py
├── docs
│   ├── .DS_Store
│   ├── Makefile
│   ├── build
│   │   ├── .DS_Store
│   │   ├── doctrees
│   │   │   ├── add.doctree
│   │   │   ├── environment.pickle
│   │   │   ├── index.doctree
│   │   │   ├── modules.doctree
│   │   │   ├── multiply.doctree
│   │   │   └── subtract.doctree
│   │   └── html
│   │       ├── .buildinfo
│   │       ├── _sources
│   │       │   ├── add.rst.txt
│   │       │   ├── index.rst.txt
│   │       │   ├── modules.rst.txt
│   │       │   ├── multiply.rst.txt
│   │       │   └── subtract.rst.txt
│   │       ├── _static
│   │       │   ├── alabaster.css
│   │       │   ├── basic.css
│   │       │   ├── check-solid.svg
│   │       │   ├── clipboard.min.js
│   │       │   ├── copy-button.svg
│   │       │   ├── copybutton.css
│   │       │   ├── copybutton.js
│   │       │   ├── copybutton_funcs.js
│   │       │   ├── custom.css
│   │       │   ├── dist
│   │       │   │   ├── assets
│   │       │   │   │   ├── fa-brands-400.eot
│   │       │   │   │   ├── fa-brands-400.svg
│   │       │   │   │   ├── fa-brands-400.ttf
│   │       │   │   │   ├── fa-brands-400.woff
│   │       │   │   │   ├── fa-brands-400.woff2
│   │       │   │   │   ├── fa-regular-400.eot
│   │       │   │   │   ├── fa-regular-400.svg
│   │       │   │   │   ├── fa-regular-400.ttf
│   │       │   │   │   ├── fa-regular-400.woff
│   │       │   │   │   ├── fa-regular-400.woff2
│   │       │   │   │   ├── fa-solid-900.eot
│   │       │   │   │   ├── fa-solid-900.svg
│   │       │   │   │   ├── fa-solid-900.ttf
│   │       │   │   │   ├── fa-solid-900.woff
│   │       │   │   │   └── fa-solid-900.woff2
│   │       │   │   ├── blocking.js
│   │       │   │   ├── blocking.js.map
│   │       │   │   ├── fontawesome.css
│   │       │   │   ├── fontawesome.css.map
│   │       │   │   ├── fontawesome.js
│   │       │   │   ├── theme.css
│   │       │   │   ├── theme.css.map
│   │       │   │   ├── theme.js
│   │       │   │   ├── theme.js.map
│   │       │   │   ├── vendor.js
│   │       │   │   ├── vendor.js.LICENSE.txt
│   │       │   │   └── vendor.js.map
│   │       │   ├── doctools.js
│   │       │   ├── documentation_options.js
│   │       │   ├── file.png
│   │       │   ├── img
│   │       │   │   ├── screenshot.png
│   │       │   │   ├── wagtail-logo-circle.svg
│   │       │   │   └── wagtail-logo.svg
│   │       │   ├── language_data.js
│   │       │   ├── minus.png
│   │       │   ├── plus.png
│   │       │   ├── pygments.css
│   │       │   ├── searchtools.js
│   │       │   └── sphinx_highlight.js
│   │       ├── add.html
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── modules.html
│   │       ├── multiply.html
│   │       ├── objects.inv
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       ├── searchindex.js
│   │       └── subtract.html
│   ├── make.bat
│   └── source
│       ├── .DS_Store
│       ├── _static
│       ├── _templates
│       ├── add.rst
│       ├── conf.py
│       ├── index.rst
│       ├── modules.rst
│       ├── multiply.rst
│       └── subtract.rst
├── multiply.py
└── subtract.py
```
24.You can change theme of your html file in the `conf.py` file in the `source folder`.I use the theme `wagtail` which can be installed by:
```bash
$ pip install sphinx-wagtail-theme
```
Install it in your Virtual Environment.

Also add This in `conf.py` folder.


```bash
extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'
```
Also if `you want to display the codes what have been written inside the code ` then just edit the `conf.py` file and add the following:

```
'sphinx.ext.viewcode',
```
in the `extensions` list.
It will finally look like this:
```bash
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon','sphinx.ext.viewcode']
```
You can also add `'sphinx.ext.mathjax'` in the extensions list to support latex math equations in the `html` file.But to do that in the `latex file` do the following:
Edit the conf.py and add in the `extensions` list
```python
    "sphinx.ext.imgmath",  # For LaTeX PDF rendering


latex_engine = "pdflatex"  # Or 'xelatex', 'lualatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
}
```

If you want to make a pdf or latex file you first have to install the `latex` support.

# Latex Or Pdf Support:

First run the following command in the terminal while activating the virtual environment:

- for linux users type:
```bash
sudo apt-get install texlive-full
```
- for macos users type:
```bash
brew install --cask mactex

```
- for Windows users Download and install MiKTeX or TeX Live.
# Now
Run this command in the `docs` folder:
```bash

make latexpdf

```
The PDF will be located in `/docs/build/latex/.`

If you want to make tex file just type:

```bash
make latex
```
-Navigate to the directory

```bash
cd docs/build/latex/
```
-Run:
```bash
pdflatex project_name.tex
```
where you have a `tex` file in the direcory naming after your project name.

### Here is a Bash script which will help you to do this all together.I prefer this one.
```bash

reading sources... 
looking for now-outdated files... none found
copying TeX support files... copying TeX support files...
done
processing myproject.tex... index modules add subtract 
resolving references...
done
writing... done
build succeeded.

The LaTeX files are in build/latex.
Run 'make' in that directory to run these through (pdf)latex
(use `make latexpdf' here to do that automatically).
latexmk -pdf -dvi- -ps-  'myproject.tex'
Rc files read:
  latexmkrc
Latexmk: This is Latexmk, John Collins, 31 Jan. 2024. Version 4.83.
Latexmk: Nothing to do for 'myproject.tex'.
Latexmk: All targets (myproject.pdf) are up-to-date

(myenv) Baijayantas-Mac-mini:~/TEST/TEST1/docs$ vi source/conf.py
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1/docs$ cd ..
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ ls
BASH.sh		add.py		docs		subtract.py
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ rm -rf docs 
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ ls
BASH.sh		add.py		subtract.py
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ vi BASH.sh 
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ clear

(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ ls
BASH.sh		add.py		subtract.py
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ chmod +x ./BASH.sh
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ ./BASH.sh         
Welcome to the Sphinx 7.4.7 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: 
The project name will occur in several places in the built documentation.
> Project name: > Author name(s): > Project release []: 
If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: 
Creating file /Users/baijayantabhattacharyya/TEST/TEST1/docs/source/conf.py.
Creating file /Users/baijayantabhattacharyya/TEST/TEST1/docs/source/index.rst.
Creating file /Users/baijayantabhattacharyya/TEST/TEST1/docs/Makefile.
Creating file /Users/baijayantabhattacharyya/TEST/TEST1/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /Users/baijayantabhattacharyya/TEST/TEST1/docs/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

Running Sphinx v7.4.7
loading translations [en]... done
/Users/baijayantabhattacharyya/myenv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
making output directory... done
building [mo]: targets for 0 po files that are out of date
writing output... 
building [html]: targets for 4 source files that are out of date
updating environment: [new config] 4 added, 0 changed, 0 removed
reading sources... [100%] subtract
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
copying assets... 
copying static files... done
copying extra files... done
copying assets: done
writing output... [100%] subtract
generating indices... genindex py-modindex done
highlighting module code... [100%] subtract
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded.

The HTML pages are in build/html.
Running Sphinx v7.4.7
loading translations [en]... done
/Users/baijayantabhattacharyya/myenv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
making output directory... done
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
writing output... 
building [latex]: all documents
updating environment: 0 added, 0 changed, 0 removed
reading sources... 
looking for now-outdated files... none found
copying TeX support files... copying TeX support files...
done
processing myproject.tex... index modules add subtract 
resolving references...
done
writing... done
build succeeded.

The LaTeX files are in build/latex.
Run 'make' in that directory to run these through (pdf)latex
(use `make latexpdf' here to do that automatically).
latexmk -pdf -dvi- -ps-  'myproject.tex'
Rc files read:
  latexmkrc
Latexmk: This is Latexmk, John Collins, 31 Jan. 2024. Version 4.83.
No existing .aux file, so I'll make a simple one, and require run of *latex.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Category 'other':
  Rerun of 'pdflatex' forced or previously required:
    Reason or flag: 'Initial setup'

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex   -recorder  "myproject.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.26 (TeX Live 2024) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./myproject.tex
LaTeX2e <2023-11-01> patch level 1
L3 programming layer <2024-02-20>
(./sphinxmanual.cls
Document Class: sphinxmanual 2019/12/01 v2.3.0 Document class (Sphinx manual)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/report.cls
Document Class: report 2023/05/17 v1.4n Standard LaTeX document class
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/size10.clo)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/cmap/cmap.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/fontenc.sty<<t1.cmap>>)
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel/babel.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel/txtbabel.def)
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel-english/english.ldf))
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel/locale/en/babel-english.t
ex) (/usr/local/texlive/2024/texmf-dist/tex/latex/tex-gyre/tgtermes.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/kvoptions/kvoptions.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/tex-gyre/tgheros.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/fncychap/fncychap.sty)
(./sphinx.sty (/usr/local/texlive/2024/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(./sphinxoptionshyperref.sty) (./sphinxoptionsgeometry.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/textcomp.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/float/float.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/wrapfig/wrapfig.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/capt-of/capt-of.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/tools/multicol.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))
(./sphinxlatexgraphics.sty) (./sphinxpackageboxes.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/pict2e/pict2e.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/pict2e/pict2e.cfg)
(/usr/local/texlive/2024/texmf-dist/tex/latex/pict2e/p2e-pdftex.def))
(/usr/local/texlive/2024/texmf-dist/tex/latex/ellipse/ellipse.sty))
(./sphinxlatexadmonitions.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/framed/framed.sty))
(./sphinxlatexliterals.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/fancyvrb/fancyvrb.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/alltt.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/upquote/upquote.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/needspace/needspace.sty))
(./sphinxlatexshadowbox.sty) (./sphinxlatexcontainers.sty)
(./sphinxhighlight.sty) (./sphinxlatextables.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/tabulary/tabulary.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/tools/array.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/tools/longtable.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/varwidth/varwidth.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/colortbl/colortbl.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/booktabs/booktabs.sty))
(./sphinxlatexnumfig.sty) (./sphinxlatexlists.sty) (./sphinxpackagefootnote.sty
) (./sphinxlatexindbibtoc.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/makeidx.sty))
(./sphinxlatexstylepage.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/parskip/parskip.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/parskip/parskip-2001-04-09.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/fancyhdr/fancyhdr.sty))
(./sphinxlatexstyleheadings.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/titlesec/titlesec.sty))
(./sphinxlatexstyletext.sty) (./sphinxlatexobjects.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/auxhook/auxhook.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
ty)) (/usr/local/texlive/2024/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/local/texlive/2024/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/local/texlive/2024/texmf-dist/tex/latex/url/url.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/atbegshi-ltx.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/atveryend-ltx.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty

(/usr/local/texlive/2024/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
))) (/usr/local/texlive/2024/texmf-dist/tex/latex/oberdiek/hypcap.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty))
(./sphinxmessages.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/palatino.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/fvextra/fvextra.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/lineno/lineno.sty))
Writing index file myproject.idx
(/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/t1ppl.fd)
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)

LaTeX Warning: Unused global option(s):
    [14pt].

(./myproject.aux)
(/usr/local/texlive/2024/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/local/texlive/2024/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontawesome5/fontawesome5.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3kernel/expl3.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3packages/l3keys2e/l3keys2e.sty)
 (/usr/local/texlive/2024/texmf-dist/tex/latex/l3packages/xparse/xparse.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontawesome5/fontawesome5-generic
-helper.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontawesome5/fontawesome5-mapping
.def)))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/t1phv.fd)<<ot1.cmap>><<oml
.cmap>><<oms.cmap>><<omx.cmap>>
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/usr/local/t
exlive/2024/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/local/texlive/20
24/texmf-dist/fonts/enc/dvips/base/8r.enc}]
No file myproject.toc.
[1] (/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/t1pcr.fd) [1]
Chapter 1.
[2]

LaTeX Warning: Reference `add:module-add' on page 3 undefined on input line 156
.


LaTeX Warning: Reference `subtract:module-subtract' on page 3 undefined on inpu
t line 159.

[3] (./myproject.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `myproject.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )</usr/local/texlive/2024/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb
></usr/local/texlive/2024/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb><
/usr/local/texlive/2024/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb></
usr/local/texlive/2024/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb></usr/loca
l/texlive/2024/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb></usr/local/texliv
e/2024/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb></usr/local/texlive/2024/
texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb></usr/local/texlive/2024/texmf-d
ist/fonts/type1/urw/palatino/uplb8a.pfb></usr/local/texlive/2024/texmf-dist/fon
ts/type1/urw/palatino/uplr8a.pfb></usr/local/texlive/2024/texmf-dist/fonts/type
1/urw/palatino/uplri8a.pfb>
Output written on myproject.pdf (5 pages, 92090 bytes).
Transcript written on myproject.log.
Latexmk: Getting log file 'myproject.log'
Latexmk: Examining 'myproject.fls'
Latexmk: Examining 'myproject.log'
Latexmk: Index file 'myproject.idx' was written
Latexmk: Missing input file 'myproject.toc' (or dependence on it) from following:
  No file myproject.toc.
Latexmk: References changed.
Latexmk: References changed.
Latexmk: Log file says output to 'myproject.pdf'
Latexmk: applying rule 'makeindex myproject.idx'...
Rule 'makeindex myproject.idx':  Reasons for rerun
Category 'other':
  Rerun of 'makeindex myproject.idx' forced or previously required:
    Reason or flag: 'Initial set up of rule'

------------
Run number 1 of rule 'makeindex myproject.idx'
------------
------------
Running 'makeindex -s python.ist  -o "myproject.ind" "myproject.idx"'
------------
This is makeindex, version 2.17 [TeX Live 2024] (kpathsea + Thai support).
Scanning style file ./python.ist.......done (7 attributes redefined, 0 ignored).
Scanning input file myproject.idx....done (6 entries accepted, 0 rejected).
Sorting entries....done (16 comparisons).
Generating output file myproject.ind....done (24 lines written, 0 warnings).
Output written in myproject.ind.
Transcript written in myproject.ilg.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  myproject.aux
  myproject.ind
  myproject.out
  myproject.toc

------------
Run number 2 of rule 'pdflatex'
------------
------------
Running 'pdflatex   -recorder  "myproject.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.26 (TeX Live 2024) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./myproject.tex
LaTeX2e <2023-11-01> patch level 1
L3 programming layer <2024-02-20>
(./sphinxmanual.cls
Document Class: sphinxmanual 2019/12/01 v2.3.0 Document class (Sphinx manual)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/report.cls
Document Class: report 2023/05/17 v1.4n Standard LaTeX document class
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/size10.clo)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/cmap/cmap.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/fontenc.sty<<t1.cmap>>)
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel/babel.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel/txtbabel.def)
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel-english/english.ldf))
(/usr/local/texlive/2024/texmf-dist/tex/generic/babel/locale/en/babel-english.t
ex) (/usr/local/texlive/2024/texmf-dist/tex/latex/tex-gyre/tgtermes.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/kvoptions/kvoptions.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/tex-gyre/tgheros.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/fncychap/fncychap.sty)
(./sphinx.sty (/usr/local/texlive/2024/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(./sphinxoptionshyperref.sty) (./sphinxoptionsgeometry.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/textcomp.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/float/float.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/wrapfig/wrapfig.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/capt-of/capt-of.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/tools/multicol.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))
(./sphinxlatexgraphics.sty) (./sphinxpackageboxes.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/pict2e/pict2e.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/pict2e/pict2e.cfg)
(/usr/local/texlive/2024/texmf-dist/tex/latex/pict2e/p2e-pdftex.def))
(/usr/local/texlive/2024/texmf-dist/tex/latex/ellipse/ellipse.sty))
(./sphinxlatexadmonitions.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/framed/framed.sty))
(./sphinxlatexliterals.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/fancyvrb/fancyvrb.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/alltt.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/upquote/upquote.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/needspace/needspace.sty))
(./sphinxlatexshadowbox.sty) (./sphinxlatexcontainers.sty)
(./sphinxhighlight.sty) (./sphinxlatextables.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/tabulary/tabulary.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/tools/array.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/tools/longtable.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/varwidth/varwidth.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/colortbl/colortbl.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/booktabs/booktabs.sty))
(./sphinxlatexnumfig.sty) (./sphinxlatexlists.sty) (./sphinxpackagefootnote.sty
) (./sphinxlatexindbibtoc.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/makeidx.sty))
(./sphinxlatexstylepage.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/parskip/parskip.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/parskip/parskip-2001-04-09.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/fancyhdr/fancyhdr.sty))
(./sphinxlatexstyleheadings.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/titlesec/titlesec.sty))
(./sphinxlatexstyletext.sty) (./sphinxlatexobjects.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/auxhook/auxhook.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
ty)) (/usr/local/texlive/2024/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/local/texlive/2024/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/local/texlive/2024/texmf-dist/tex/latex/url/url.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/atbegshi-ltx.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/atveryend-ltx.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty

(/usr/local/texlive/2024/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
))) (/usr/local/texlive/2024/texmf-dist/tex/latex/oberdiek/hypcap.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty))
(./sphinxmessages.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/palatino.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/fvextra/fvextra.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/lineno/lineno.sty))
Writing index file myproject.idx
(/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/t1ppl.fd)
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)

LaTeX Warning: Unused global option(s):
    [14pt].

(./myproject.aux)
(/usr/local/texlive/2024/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/local/texlive/2024/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontawesome5/fontawesome5.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3kernel/expl3.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3packages/l3keys2e/l3keys2e.sty)
 (/usr/local/texlive/2024/texmf-dist/tex/latex/l3packages/xparse/xparse.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontawesome5/fontawesome5-generic
-helper.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontawesome5/fontawesome5-mapping
.def)))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./myproject.out) (./myproject.out)
(/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/t1phv.fd)<<ot1.cmap>><<oml
.cmap>><<oms.cmap>><<omx.cmap>>
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/usr/local/t
exlive/2024/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/local/texlive/20
24/texmf-dist/fonts/enc/dvips/base/8r.enc}] (./myproject.toc) [1]
(/usr/local/texlive/2024/texmf-dist/tex/latex/psnfss/t1pcr.fd) [1]
Chapter 1.
[2] [3] (./myproject.aux) )</usr/local/texlive/2024/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmmi10.pfb></usr/local/texlive/2024/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmr10.pfb></usr/local/texlive/2024/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb></usr/local/texlive/2024/texmf-dist/fonts/type1/urw/cour
ier/ucrb8a.pfb></usr/local/texlive/2024/texmf-dist/fonts/type1/urw/courier/ucrr
8a.pfb></usr/local/texlive/2024/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>
</usr/local/texlive/2024/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb></usr/l
ocal/texlive/2024/texmf-dist/fonts/type1/urw/palatino/uplb8a.pfb></usr/local/te
xlive/2024/texmf-dist/fonts/type1/urw/palatino/uplr8a.pfb></usr/local/texlive/2
024/texmf-dist/fonts/type1/urw/palatino/uplri8a.pfb>
Output written on myproject.pdf (5 pages, 97524 bytes).
Transcript written on myproject.log.
Latexmk: Getting log file 'myproject.log'
Latexmk: Examining 'myproject.fls'
Latexmk: Examining 'myproject.log'
Latexmk: Index file 'myproject.idx' was written
Latexmk: Log file says output to 'myproject.pdf'
Latexmk: All targets (myproject.pdf) are up-to-date

Documentation successfully generated!
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ rm -rf docs 
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ ls
BASH.sh		add.py		subtract.py
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ vi BASH.sh 
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ ./BASH.sh         
Welcome to the Sphinx 7.4.7 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: * Please enter either 'y' or 'n'.
> Separate source and build directories (y/n) [n]: * Please enter either 'y' or 'n'.
> Separate source and build directories (y/n) [n]: * Please enter either 'y' or 'n'.
> Separate source and build directories (y/n) [n]: 
The project name will occur in several places in the built documentation.
> Project name: > Author name(s): 
[Interrupted.]
./BASH.sh: line 15: cd: source: No such file or directory
make: *** No rule to make target `html'.  Stop.
make: *** No rule to make target `latexpdf'.  Stop.
Documentation successfully generated!
The file /Users/baijayantabhattacharyya/TEST/TEST1/build/html/index.html does not exist.
The file /Users/baijayantabhattacharyya/TEST/TEST1/build/latex/MyProject.pdf does not exist.
(myenv) Baijayantas-Mac-mini:~/TEST/TEST1$ vi BASH.sh

 24 latex_engine = "pdflatex"  # Or 'xelatex', 'lualatex'
 25 latex_elements = {"papersize": "a4paper",
 26 'printindex': '',
 27 'classoptions': ',oneside',
 28     'extraclassoptions': 'openany',
 29      "pointsize": "14pt",
 30     "preamble": r"""
 31 \usepackage{palatino}  
 32 \usepackage{fvextra}  % Better verbatim environments
 33 """
 34 }
 35 
 36 pygments_style = "sphinx"  # Syntax highlighting style
 37 EOF
 38 cd ..
 39 
 40 #Create the rst files
 41 sphinx-apidoc -o source/ ../ --force
 42 cd source
 43 cat<<EOF>> index.rst
 44    modules
 45 EOF
 46 cd ..
 47 make html 
 48 make latexpdf
 49 echo "Documentation successfully generated!"
 50 open build/html/index.html
 51 open build/latex/MyProject.pdf
~                                                                                                   
-- INSERT --

```



















