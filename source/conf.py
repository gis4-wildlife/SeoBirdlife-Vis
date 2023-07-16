# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'SeoBirdlife - Vizualization "Migra" Project'
copyright = '2023, GIS4 Wildlife Movement Analytics'
author = 'GIS4 Wildlife | bryan@gis4-wildlife.com'

# The full version, including alpha/beta/rc tags
release = 'v1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.builders.linkcheck',
    'sphinx_togglebutton',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'myst_nb',
    # 'jupyter_sphinx',
    # 'sphinx_tabs.tabs',
    "sphinx_inline_tabs",
   # 'sphinx_last_updated_by_git'
]

# Suffid=x to files m2r
source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_logo = '_static/seo-migra.png'
html_title = "SeoBirdlife - GIS4 Wildlife"

# navigation bar elements on left
html_sidebars = {
    "**": ["navbar-logo.html", "search-field.html", "sbt-sidebar-nav.html"]
}

# True, otherwise collapse the content of all page
sphinx_tabs_disable_tab_closing = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/wt.css'
]

html_theme_options = {
    # "external_links": [],
    "toc_title": "",
    "home_page_in_toc": True,
    "navbar_end": ["navbar-icon-links"],
    "repository_url": "https://github.com/gis4-wildlife/SeoBirdlife-Vis",
    "repository_branch": "main",
    "path_to_docs": "source/",
    # "twitter_url": "https://twitter.com/pythongis",
    # "google_analytics_id": "",
    "use_edit_page_button": False,
    "use_repository_button": False,
    "launch_buttons": {
        "binderhub_url": "https://notebooks.gesis.org/binder",
        "thebe": False,
        "notebook_interface": "jupyterlab",
        "collapse_navigation": False,
        # Google Colab does not provide an easy way for specifying/building/activating the conda environment
        # in a similar manner as Binder. Hence, let's not keep it. The easiest way seems to be:
        # https://github.com/jaimergp/condacolab
        # But it requires actions from the user nontheless, so atm it's a no-go.
        #"colab_url": "https://colab.research.google.com"
    },
}

# Allow errors
# execution_allow_errors = True

# Do not execute cells
# jupyter_execute_notebooks = "off"
