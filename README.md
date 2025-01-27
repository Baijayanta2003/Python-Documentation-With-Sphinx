## Python-Documentation-With-Sphinx
In this I will guide you step by step how to *make* documentation for your python codes and make them in different format and make html or pdf or tex files.

## Here are the steps:

1.First install a virtual environment using the command in your terminal command

```bash
python -m venv myenv

```
You can write thing instead of myenv. This can create a directiory where your virtual environment will be.

After installing write in command prompt or terminal
```bash
pwd

```
You will see a directory address printed on window.
This is the directory you have installed the virtual environment.

2.Activate the virtual environment.

```bash
 source myenv/bin/activate
```

After that you will see a line `After activation, you should see (myenv) in your command prompt`.

3.Once the virtual environment is activated, you can install packages using `pip`:
```bash
pip install <package_name>
```
install all the packages you need.

4.To deactiavte the virtual environment type
```bash
deactivate
```
viola you have successfully installed used and exited the virtual environment.

5.Now get back to work.

Activate the virtual environment myenv by step `2`.

Then navigate to the directory (In my case I have a folder named `Sphinux_Tutorial` where my python scripts are located) 
where the python scripts are there that you want to make the documentation.

Alternatively you can navigate to that directory first and then activate the virtual environment using this command
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
Sphinux_Tutorial/

```
8.Add the files you want to document.
My case Files are `add.py`,`subtract.py`,`multiply.py`.
After this my directory structure is:

```bash
Sphinux_Tutorial/
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
Type The name of the project you wanna give,In my case it is `Documenting Python Code with Sphinux`.
After that it will look something like this:
```
The project name will occur in several places in the built documentation.
> Project name: Documenting Python Code with Sphinux
> Author name(s):
```
Type The Author name,Do the next commands and then it will look like this:
 ```
> Author name(s): Baijaynta Bhattacharyya
> Project release []: '0.0.1'

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: English

Creating file /Sphinux_Tutorial/docs/source/conf.py.
Creating file /Sphinux_Tutorial/docs/source/index.rst.
Creating file /Sphinux_Tutorial/docs/Makefile.
Creating file /Sphinux_Tutorial/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /Users/baijayantabhattacharyya/Sphinux_Tutorial/docs/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```
Now the directory looks like:
```bash
Sphinux_Tutorial/
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
Now type 
```bash
cd source/ 
```
```bash
vi conf.py
```
This will look like this:
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
Press `esc` `a` to edit.
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
Finally it will look like this:
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
This command will generate `.rst` files in the `source` folder, one for each Python module, including an index file `(modules.rst)` that lists all the modules.

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
Press `esc` `a ` to edit.
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
The following text will appear:
```bash
Running Sphinx v7.4.7
loading translations [English]... not available for built-in messages
/Users/baijayantabhattacharyya/myenv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
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
To view the `html` file type
```bash
cd build/html
```
And Type:
```bash

open index.html
```
You will see a html file opening in your default browser.
Final Indexing is:
```bash
├── add.py
├── docs
│   ├── Makefile
│   ├── build
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
│   │       │   ├── custom.css
│   │       │   ├── doctools.js
│   │       │   ├── documentation_options.js
│   │       │   ├── file.png
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
You can change theme in the `conf.py` file in the `source folder`.I defaultly use themee `nature`.























