from typing import Type

class Config:
    """
    Config class for our application. Include all components for rest, gRPC, workers etc.
    """
    app_component_classes: list[Type['AppBaseComponent']] = []

    @classmethod
    def add_app_component_class(cls, component_class: Type['AppBaseComponent']):
        cls.app_component_classes.append(component_class)
