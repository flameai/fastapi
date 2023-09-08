from typing import Optional

from fastapi import FastAPI
from uvicorn import run as uvicorn_run
from uvicorn.config import LOGGING_CONFIG

from common.fastapi.settings import (
    APP_PORT,
    APP_HOST,
    APP_WORKERS,
)
from common.fastapi.registry import Registry
from common.fastapi.config import Config


class App(FastAPI):
    """
    Класс приложения с настройками общими для всех проектов.
    При инициализации произойдет регистрация всех компонентов
    в приложении
    """

    def __init__(self, *a, **kw) -> None:

        super().__init__(*a, **kw)

        if self.Config.components_classes:
            for component_class in set(self.components_classes):
                component_instance = component_class()
                component_instance.register(self)

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
