from typing import Optional

from fastapi.routing import APIRouter
from uvicorn import run as uvicorn_run
from uvicorn.config import LOGGING_CONFIG

from common.fastapi.base import ComponentProvidedApp
from common.fastapi.settings import (
    APP_PORT,
    APP_HOST,
    APP_WORKERS,
)
from common.fastapi.base import ComponentCategoryGetterEnum


class App(ComponentProvidedApp):
    """
    Класс приложения с настройками, общими для всех проектов
    """
    # Используем Registry для IoC целей.
    config = {key: None for key in ComponentCategoryGetterEnum}

    def register_router(self, router: APIRouter) -> None:
        """
        Зарегистрирует роутер в приложении и проверит все вью в нем на соответствие компонентам сервиса
        """


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
