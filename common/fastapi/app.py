from typing import Optional

from fastapi import FastAPI
from uvicorn import run as uvicorn_run
from uvicorn.config import LOGGING_CONFIG

from common.fastapi.settings import (
    APP_PORT,
    APP_HOST,
    APP_WORKERS,
)
from common.fastapi.config import Config
from common.fastapi.base import AppBaseComponent


class App(FastAPI):
    """
    Application class for all projects in our meta company.
    Use Config class for customize standard FastAPI app and fullfill registry
    Using:
    >>> from common.fastapi.app import App
    >>> from common.db.mysql.fastapi import MySQL
    >>> from common.db.redis.fastapi import Redis
    >>> from common.fastapi.config import Config
    >>> ...
    >>> Config.add_app_component_class(MySQL)
    >>> Config.add_app_component_class(Redis)
    >>>
    >>> projectApp = App()
    >>> projectApp.run()
    """

    def __init__(self, *a, **kw) -> None:

        super().__init__(*a, **kw)

        for component_class in set(Config.app_component_classes):
            component_instance = component_class()
            component_instance.register_app_hooks(self)

    def run(self, app: Optional[str] = None, log_config: Optional[dict] = None) -> None:
        app = app or self
        log_config = log_config or LOGGING_CONFIG
        uvicorn_run(
            app,
            port=APP_PORT,
            host=APP_HOST,
            workers=APP_WORKERS,
            log_config=log_config,
        )
