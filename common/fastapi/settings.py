from dotenv import load_dotenv

from common.environ.settings_class import EnvironSettings

load_dotenv()


class FastAPIAppSettings(EnvironSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    APP_WORKERS: int = None
    APP_PROTO: str = "http"


fastapi_app_settings = FastAPIAppSettings()

APP_HOST = fastapi_app_settings.APP_HOST
APP_PORT = fastapi_app_settings.APP_PORT
APP_WORKERS = fastapi_app_settings.APP_WORKERS
APP_PROTO = fastapi_app_settings.APP_PROTO
