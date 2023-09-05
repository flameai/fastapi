from typing import Collection, Type, Sequence
from functools import partial
from enum import Enum

from fastapi import FastAPI


class ComponentCategoryGetterEnum(Enum):
    RelationalDB = "RelationalDB"
    NoSQLDB = "NoSQLDB"
    QueueBroker = "QueueBroker"


class AppBaseComponent:
    """
    Компонент приложения. При инстанцировании приложения
    будет зарегистрирован и композирован в нем.
    Демонстрация Композиции ООП
    """

    def register(self, app) -> None:
        raise NotImplementedError


class AppEventProvidedComponent(AppBaseComponent):
    """
    Компонент приложения, имплементирующий методы перед стартом и остановкой приложения.
    Для демонстрации наследования и полиморфирования ООП
    """

    def register(self, app) -> None:
        app.on_event("startup")(partial(self.startup, app))
        app.on_event("shutdown")(partial(self.shutdown, app))

    async def startup(self, app) -> None:
        raise NotImplementedError

    async def shutdown(self, app) -> None:
        raise NotImplementedError


class ComponentProvidedApp(FastAPI):
    """
    Приложение со списком компонентов, используемых в нем.
    Демонстрация Композиции и использования ковариантных типов
    """

    component_classes: Collection[Type[AppBaseComponent]] = None

    def __init__(self, *a, **kw) -> None:

        super().__init__(*a, **kw)
        self.component_classes = set(self.component_classes) or []
        for component_class in self.component_classes:
            component_instance = component_class()
            component_instance.register(self)
