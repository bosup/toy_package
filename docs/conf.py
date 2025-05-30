import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = 'toy'
author = 'bosup'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon'
]

autosummary_generate = True
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
