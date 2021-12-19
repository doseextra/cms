from dynaconf import settings
from os import environ
from flask import request


def init_app(app):
    @app.context_processor
    def inject_globals():
      return {
        'app_name': settings.get('APP_NAME') or '[DEV_MOD]',
        'app_url': environ.get('APP_URL') if environ.get('APP_ENV') == 'production' else request.url_root,
        'app_env': environ.get('APP_ENV'),
        'app_version': environ.get('APP_VERSION')
    }
