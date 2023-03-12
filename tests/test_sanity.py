def test_can_import_package():
    import flask_tabler


def test_can_initialize_app_and_extesion():
    from flask import Flask
    from flask_tabler import Tabler

    app = Flask(__name__)
    Tabler(app)
