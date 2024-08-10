import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="ml_examples",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    env_switcher="ml_examples_env",
    load_dotenv=True,
    load_dotenv=False,
)


"""
# How to use this application settings

```
from config import settings
```

### Accessing values:

```
settings.get("SECRET_KEY", default="abcd1234")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings.["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export ML_EXAMPLES_KEY=value
export ML_EXAMPLES__KEY="@int 42"
export ML_EXAMPLES__KEY="@jinja {{ this.db.uri }}"
export ML_EXAMPLES_DB__uri="sqlite:///dev.db"
```

### Switching environments
```
ML_EXAMPLES_ENV=production ml_examples run
```

Read the docs: https://dynaconf.com
"""
