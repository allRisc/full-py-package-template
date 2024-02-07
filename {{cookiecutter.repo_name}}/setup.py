{% include "header.j2" %}

from setuptools import setup

import importlib.util
import pathlib

_proj_root = pathlib.Path(__file__).parent
_info_spec = importlib.util.spec_from_file_location(
                                   "{{cookiecutter.package_name}}._info",
                                   _proj_root.joinpath("src", "{{cookiecutter.package_name}}", "_info.py")
                               )
_info = importlib.util.module_from_spec(_info_spec)
_info_spec.loader.exec_module(_info)

if __name__ == "__main__":
  setup(
    version=_info.__version__
  )