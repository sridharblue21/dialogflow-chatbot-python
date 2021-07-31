from functools import lru_cache
from . import config

#for caching .env file
@lru_cache()
def get_settings():
    return config.Settings()