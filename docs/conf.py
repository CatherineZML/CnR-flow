# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import os
import sys
#import proj_rst_vars
#import sphinx_nextflow
import sphinx_rtd_theme

import imp
sys.path.insert(0, os.path.abspath('.'))

proj_rst_vars = imp.load_source('proj_rst_vars', 
     os.path.abspath(os.path.join('proj_rst_vars.py'))
)
sphinx_nextflow = imp.load_source('sphinx_nextflow', 
     os.path.abspath(os.path.join('sphinx_nextflow.py'))
)


# -- Path setup --------------------------------------------------------------

# -- Project information -----------------------------------------------------
with open(os.path.join('..', 'nextflow.config'), 'r') as config_file:
    for line in config_file:
        if 'author =' in line:
            author = line.split('author =')[1].strip().strip('"').strip("'")
        elif 'version =' in line:
            version = line.split('version =')[1].strip().strip('"').strip("'")
        elif 'name =' in line:
            project = line.split('name =')[1].strip().strip('"').strip("'")

#project = 'CUT&RUN-Flow'
copyright = '2022, Daniel Stribling'

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    #'sphinx.ext.imgconverter',
    ]

# add_module_names
autosectionlabel_maxdepth = 3
#autosectionlabel_prefix_document = True
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'setup.py', 
                    'proj_rst_vars.rst', 
                    'source/specification.rst',
                    'source/citations.rst',
                    'index_contents.rst',
                    'docs_readme_format.rst',
                   ]


intersphinx_mapping = {
                       #'python': ('https://docs.python.org/3', None),
                       #'matplotlib': ('https://readthedocs.org/projects/matplotlib/latest/', None)
                      }


# -- Nextflow-specific Configuration -----------------------------------------

primary_domain = None
manpages_url = 'https://www.nextflow.io/docs/latest/{path}.html' 
extensions.append('sphinx_nextflow')

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Latex/PDF output options:
latex_toplevel_sectioning = 'chapter'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

# Fix to RTD table wrapping: https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
#html_context = {
#    'css_files': [
#        '_static/theme_overrides.css',  # override wide tables in RTD theme
#        ],
#     }

# Define custom variables
rst_epilog = proj_rst_vars.rst_epilog

