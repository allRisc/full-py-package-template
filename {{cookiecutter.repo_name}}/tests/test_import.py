{% include "header.j2" %}

import {{cookiecutter.package_name}}


def test_import():
    print({{cookiecutter.package_name}}.version_info)
