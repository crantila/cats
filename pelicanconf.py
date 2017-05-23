#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Christopher Antila'
SITENAME = 'Meow'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10

# Disable the feeds
# =================
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Change the URLs
# ===============
ARCHIVES_SAVE_AS = ''
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{date:%H}:{date:%M}'
ARTICLE_SAVE_AS = '{url_root}/index.html'.format(url_root=ARTICLE_URL)
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
PAGE_SAVE_AS = ''


# Theme (Pelican Settings)
# ========================
THEME_STATIC_DIR = 'static'
TYPOGRIFY = True
# TEMPLATE_PAGES = {
# }


# Theme (Custom Settings)
# =======================
THEME = 'theme'
