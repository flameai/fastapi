from functools import partial


class AppBaseComponent:
    """
    Компонент приложения. При инстанцировании приложения
    будет зарегистрирован в registry.
    Демонстрация Композиции ООП и использования паттерна Registry
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
