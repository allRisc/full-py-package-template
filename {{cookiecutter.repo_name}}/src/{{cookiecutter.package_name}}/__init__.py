{% include "header.j2" %}

from __future__ import annotations

import re


#####################################################################################
# Version Information
#####################################################################################
from {{cookiecutter.package_name}}._info import __version__

version_info = [int(x) if x.isdigit() else x for x in re.split(r"\.|-", __version__)]
