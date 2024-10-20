# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add the root of your Django project to the Python path
sys.path.insert(0, os.path.abspath('../'))  # Adjust the path if necessary

# Refers to plate/settings.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'plate.settings'

import django
django.setup()  # This ensures that Django settings are correctly loaded

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'doc captsone'
copyright = '2024, ano'
author = 'ano'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
