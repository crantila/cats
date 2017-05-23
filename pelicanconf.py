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
SLUGIFY_SOURCE = 'basename'


# Pagination Settings
# ===================
DEFAULT_ORPHANS = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


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
ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''
# ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{date:%H}:{date:%M}'
# ARTICLE_SAVE_AS = '{url_root}/index.html'.format(url_root=ARTICLE_URL)
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
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
DIRECT_TEMPLATES = ['compress_images', 'index']
# IMAGE_WIDTHS... only defined in publishconf
