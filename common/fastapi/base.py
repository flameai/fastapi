from typing import Collection, Type
from functools import partial

from fastapi import FastAPI


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
        if not self.component_classes:
            return  # Ранний выход, однако, джентльмены! ))
        for component_class in self.component_classes:
            component_instance = component_class()
            component_instance.register(self)
