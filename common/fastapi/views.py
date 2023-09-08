from fastapi import Depends
from common.fastapi.config import init_config


class BaseView:
    """
    Базовый класс наших вьюх.
    Прежде чем объявлять классы вьюх, инициализируем все компоненты
    """
    _: None = Depends(init_config)
