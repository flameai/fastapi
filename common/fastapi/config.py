from typing import Any
from enum import Enum

from common.fastapi.exceptions import NotExistingNoSQLDatabaseSettings, NotExistingRelationalDatabaseSettings


class ComponentCategoryGetterEnum(Enum):
    RelationalDB = "RelationalDB"
    NoSQLDB = "NoSQLDB"
    QueueBroker = "QueueBroker"


class AppConfig:
    # Используем Registry для IoC целей.
    component_category_getters = {key: None for key in ComponentCategoryGetterEnum}


def get_component(component: ComponentCategoryGetterEnum) -> Any:
    """
    Вернет функцию получения компонента, либо исключение, если таковой не настроен в приложении
    """

    def _get_component(_component):
        return _component

    if AppConfig.component_category_getters[component] is None:
        exception = get_exception_for_component(component)
        raise exception

    return _get_component


exceptions_mapping = {
    ComponentCategoryGetterEnum.RelationalDB: NotExistingRelationalDatabaseSettings,
    ComponentCategoryGetterEnum.NoSQLDB: NotExistingNoSQLDatabaseSettings
}


def get_exception_for_component(component: ComponentCategoryGetterEnum):
    return exceptions_mapping[component] if component in exceptions_mapping else Exception(
        f"Cant get component {component} from application.")
