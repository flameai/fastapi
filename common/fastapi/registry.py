from typing import Any
from enum import Enum
from fastapi import Depends

from common.fastapi.exceptions import NotExistingNoSQLDatabaseSettings, NotExistingRelationalDatabaseSettings

class ComponentCategoryEnum(Enum):
    RelationalDB = "RelationalDB"
    NoSQLDB = "NoSQLDB"
    QueueBroker = "QueueBroker"


class Registry:
    """
    Сингтон для хранения ресурсов нужных компонентов (Сессий БД, объекта доступа к NoSQL, к очереди)
    Используем подобие поттерна ServiceLocator
    """
    REGISTRY = {
        'components_by_category': {
            key: None for key in ComponentCategoryEnum
        }
    }


def get_component_by_category(component_category: ComponentCategoryEnum) -> Any:
    """
    Вернет функцию получения компонента нужной категории
    с вызовом учетом исключения в случае его отсутствия
    """

    # Моржовый оператор вашему вниманию ( := )
    if component := Registry.REGISTRY['components_by_category'][component_category] is None:
        exception = get_exception_for_component_category(component_category)
        raise exception

    return component


exceptions_mapping = {
    ComponentCategoryEnum.RelationalDB: NotExistingRelationalDatabaseSettings,
    ComponentCategoryEnum.NoSQLDB: NotExistingNoSQLDatabaseSettings
}


def get_exception_for_component_category(component_category: ComponentCategoryEnum):
    return exceptions_mapping[component_category] if component_category in exceptions_mapping else Exception(
        f"Cant get component {component_category.value} from application.")
