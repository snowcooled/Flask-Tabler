import re

from flask import Flask
from flask_tabler import Tabler
import flask_tabler
import requests

import pytest


@pytest.fixture
def app():
    app = Flask(__name__)
    Tabler(app)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def bsv():
    tabler_version = re.search(r'(\d+\.\d+\.\d+)',
                                  str(flask_tabler.__version__)).group(1)
    return tabler_version


def test_tabler_version_matches(app, client, bsv):
    tabler_vre = re.compile(r'Tabler v(\d+\.\d+\.\d+).*')

    # find local version
    local_version = tabler_vre.search(
        str(client.get('/static/tabler/css/tabler.css').data)
    ).group(1)

    # find cdn version
    cdn = app.extensions['tabler']['cdns']['tabler']
    with app.app_context():
        cdn_url = 'https:' + cdn.get_resource_url('css/tabler.css')
    cdn_version = tabler_vre.search(requests.get(cdn_url).text).group(1)

    # get package version

    assert local_version == bsv
    assert cdn_version == bsv
