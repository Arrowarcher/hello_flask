#!/usr/bin/env python3
from flask.cli import ScriptInfo

from application import create_app, db

app = create_app("config/dev_cfg.py")



if __name__ == "__main__":
    app.run()
