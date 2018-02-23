# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_nemo import Nemo
from capitains_nautilus.flask_ext import FlaskNautilus
from capitains_nautilus.cts.resolver import NautilusCTSResolver
from werkzeug.contrib.cache import FileSystemCache
from flask_caching import Cache
import os
from config import nemo_config

d = "/opt/data"
app = Flask("Nautilus")
nautilus_cache = FileSystemCache("/opt/cache")
http_cache = Cache(config={'CACHE_TYPE': "simple"})
nautilus_resolver = NautilusCTSResolver(
    [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))],
    cache=nautilus_cache
)
nautilus = FlaskNautilus(
    app=app,
    prefix="/api",
    name="nautilus",
    resolver=nautilus_resolver,
    flask_caching=http_cache
)

# We set up Nemo
nemo = Nemo(
    app=app,
    name="nemo",
    base_url="",
    cache=http_cache,
    resolver=nautilus_resolver,
    **nemo_config
)

http_cache.init_app(app)

app.debug = True
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
