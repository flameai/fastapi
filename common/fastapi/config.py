from typing import Type
from common.fastapi.base import AppBaseComponent


def init_config():
    Config.init()


class Config:
    """
    Класс-синглтон для настройки нашего приложения
    """

    is_initialized = False
    components_classes = []

    @classmethod
    def init(cls):
        if cls.is_initialized:
            return
        for component_class in set(cls.components_classes):
            component_class()

    @classmethod
    def add_component_class(cls, component_class: Type[AppBaseComponent]):
        cls.components_classes.append(component_class)
