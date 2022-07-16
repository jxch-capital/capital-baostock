from werkzeug.utils import import_string
import werkzeug

werkzeug.import_string = import_string
from flask_cache import Cache
from flask import request, current_app

cache = Cache(with_jinja2_ext=False)


def cache_with_param(timeout=10000, key_prefix='view/%s', unless=None):
    def key_prefix_func():
        with current_app.app_context():
            if '%s' in key_prefix:
                cache_key = key_prefix % str(dict(request.values.items()))
            else:
                cache_key = key_prefix
        return cache_key

    return cache.cached(timeout=timeout, key_prefix=key_prefix_func, unless=unless)
