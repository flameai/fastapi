from typing import Optional

from uvicorn import run as uvicorn_run
from uvicorn.config import LOGGING_CONFIG

from common.fastapi.base import ComponentProvidedApp
from common.fastapi.settings import (
    APP_PORT,
    APP_HOST,
    APP_WORKERS,
)

class App(ComponentProvidedApp):
    """
    Класс приложения с настройками, общими для всех проектов
    """
    def run(self, app: Optional[str] = None, log_config: Optional[dict] = None):
        app = app or self
        log_config = log_config or LOGGING_CONFIG
        uvicorn_run(app, port=APP_PORT, host=APP_HOST, workers=APP_WORKERS, log_config=log_config)
