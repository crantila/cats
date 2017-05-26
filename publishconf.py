#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

PUBLISH = True

SITEURL = 'https://meow.antila.ca'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True


# Theme (Custom Settings)
# =======================
IMAGE_WIDTHS = ['300', '400', '500', '600', '700', '800', '900', '1000']
IMAGES_URL = '{siteurl}/images'.format(siteurl=SITEURL)
