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
```bash
Sphinx_Tutorial/

```
8.Add the files you want to document.
My case Files are `add.py`,`subtract.py`,`multiply.py`.
After this my directory structure is:

```bash
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
```
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
```
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name:

```
13.Type The name of the project you wanna give,In my case it is `Documenting Python Code with Sphinux`.
After that it will look something like this:
```
The project name will occur in several places in the built documentation.
> Project name: Documenting Python Code with Sphinux
> Author name(s):
```
14.Type The Author name,Do the next commands and then it will look like this:
 ```
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
```bash
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
```bash
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
```bash
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

```
type:
```
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Adjust the path if needed

```
19.Finally it will look like this:
```bash
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
```bash
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
```bash
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
```bash
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




















