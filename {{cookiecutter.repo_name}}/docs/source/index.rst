.. {{cookiecutter.project_name}} documentation master file

Welcome to {{cookiecutter.project_name}}'s documentation!
===========================================

.. image:: https://github.com/{{cookiecutter.repo_org}}/{{cookiecutter.repo_name}}/actions/workflows/test.yml/badge.svg
   :alt: Tests
   :target: https://github.com/allRisc/{{cookiecutter.repo_name}}/actions/workflows/test.yml
.. image:: https://img.shields.io/pypi/v/{{cookiecutter.package_name}}.svg
   :alt: PyPi Latest Release
   :target: https://pypi.org/project/{{cookiecutter.package_name}}/
.. image:: https://readthedocs.org/projects/{{cookiecutter.package_name.replace('_', '-')}}/badge
   :alt: Documentation Status
   :target: https://{{cookiecutter.package_name.replace('_', '-')}}.readthedocs.io/en/latest/index.html

.. autosummary::
   :toctree: _autosummary
   :template: module-template.rst
   :recursive:

   {{cookiecutter.package_name}}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   example
   license
   contributors

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
