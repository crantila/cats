#!/usr/bin/env python3

# This Pelican plugin generates the responses for API calls.

import json
import logging
import pathlib
import subprocess

from pelican import signals

LOGGER = logging.getLogger(__name__)


def make_article_links(images_url, image_widths, photo):
    """
    Make the photo links for one article.
    """
    post = {'webp': [], 'jpeg': [], 'img': ''}
    photo_root = photo[:-4]  # remove ".jpg"

    webp_url = images_url + '/{image}-{w}.webp'
    jpeg_url = images_url + '/{image}-{w}.jpg'

    post['webp'] = {w: webp_url.format(image=photo_root, w=w) for w in image_widths}
    post['jpeg'] = {w: jpeg_url.format(image=photo_root, w=w) for w in image_widths}
    post['img'] = images_url + '/' + photo

    return post


def make_api(generator):
    """
    """
    output_path = generator.output_path
    api_url = generator.settings.get('API_URL', '')
    image_widths = generator.settings.get('IMAGE_WIDTHS', [])
    images_url = generator.settings.get('IMAGES_URL', '')

    articles = [make_article_links(images_url, image_widths, a.photo) for a in generator.articles]

    # group into "pages"
    per_page = generator.settings.get('DEFAULT_PAGINATION', 10)
    paginated = []
    while len(articles):
        paginated.append(articles[:per_page])
        del articles[:per_page]

    # make sure the API root directory exists
    root_dir = pathlib.Path('{out}{api}/page'.format(out=output_path, api=api_url))
    if not root_dir.exists():
        # TODO: this, in a less lazy way
        subprocess.check_call(['mkdir', '-p', str(root_dir)])
    elif not root_dir.is_dir():
        # TODO: this, in a less lazy way
        raise RuntimeError('dude, wtf?!')

    # output all the stuff
    for i, page in enumerate(paginated):
        file_path = root_dir.joinpath('{i}.json'.format(i=i + 1))
        with file_path.open('w') as the_file:
            the_file.write(json.dumps(page))


def register():
    """
    Connect the Pelican signals.
    """
    signals.article_generator_finalized.connect(make_api)
