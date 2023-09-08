from fastapi import Depends
from common.fastapi.config import init_config


class BaseView:
    """
    Базовый класс наших вьюх.
    Прежде чем объявлять классы вьюх, инициализируем все компоненты
    а также покажем, что нам не чужд подход Dependency Injection ))
    """
    _: None = Depends(init_config)
