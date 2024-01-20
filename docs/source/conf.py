# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'adv_cpp_notes'
copyright = '2024, cergan'
author = 'cergan'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['m2r2']

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "coskunergan", # Username
    "github_repo": "adv_cpp_notes", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "docs/source/", # Path in the checkout to the docs root
}

 
