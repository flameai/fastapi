from typing import Any
from enum import Enum

from common.fastapi.exceptions import get_exception_for_component


class ComponentCategoryGetterEnum(Enum):
    RelationalDB = "RelationalDB"
    NoSQLDB = "NoSQLDB"
    QueueBroker = "QueueBroker"


class AppConfig:
    # Используем Registry для IoC целей.
    component_category_getters = {key: None for key in ComponentCategoryGetterEnum}


def get_component(component: ComponentCategoryGetterEnum) -> Any:
    """
    Вернет компонент, либо исключение, если таковой не настроен в приложении
    """
    if AppConfig[component] is None:
        exception = get_exception_for_component(component)
        raise exception

    return AppConfig[component]
