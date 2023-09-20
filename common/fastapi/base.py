from typing import Optional

from fastapi import FastAPI

from common.fastapi.registry import ComponentCategoryEnum


class SingletonMeta(type):
    instances = {}

    def __call__(self, *a, **kw):
        if self.__class__ not in self.instances:
            self.instances[self.__class__] = super().__call__(*a, **kw)

        return self.instances[self.__class__]


class AppBaseComponent(metaclass=SingletonMeta):
    CATEGORY: ComponentCategoryEnum = None

    """
    Component with startup and shutdown implemented hooks.
    Pay attention we use DIP principle here from SOLID.
    Let's make code bit less bounded by using startup
    and shutdown interfaces.
    """

    def register_app_hooks(self, app: FastAPI) -> None:
        app.on_event("startup")(self.startup)
        app.on_event("shutdown")(self.shutdown)

    async def startup(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass
