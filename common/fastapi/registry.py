from typing import Any
from enum import Enum
from common.fastapi.exceptions import NotExistingNoSQLDatabaseSettings, NotExistingRelationalDatabaseSettings
from common.fastapi.config import Config
from sqlalchemy.orm import Session


class ComponentCategoryEnum(Enum):
    RelationalDB = "RelationalDB"
    NoSQLDB = "NoSQLDB"
    QueueBroker = "QueueBroker"


class ComponentRegistry:
    """
    Registry for component getters.
    """

    EXCEPTION_MAPPING = {
        ComponentCategoryEnum.RelationalDB: NotExistingRelationalDatabaseSettings,
        ComponentCategoryEnum.NoSQLDB: NotExistingNoSQLDatabaseSettings
    }

    components_by_category: dict = {
        key: None for key in ComponentCategoryEnum
    }

    all_components = []

    is_registered = False

    @classmethod
    def register_all_components_in_registry(cls) -> None:
        if cls.is_registered:
            return
        for component_class in Config.app_component_classes:
            component_instance = component_class()
            cls.all_components.append(component_instance)
            cls.components_by_category[component_class.CATEGORY] = component_instance
        cls.is_registered = True

    @classmethod
    def get_exception_for_component_category(cls, component_category: ComponentCategoryEnum):
        return cls.EXCEPTION_MAPPING[component_category] if component_category in cls.EXCEPTION_MAPPING else Exception(
            f"Cant get component {component_category.value} from application.")

    @classmethod
    def get_component_by_category_or_exception(cls, component_category: ComponentCategoryEnum) -> Any:
        """
        Returns component. For example DB Session, Redis pool, Rabbit Queue etc
        """

        cls.register_all_components_in_registry()

        # By the way Morse operator
        if (component := cls.components_by_category[component_category]) is None:
            exception = cls.get_exception_for_component_category(component_category)
            raise exception

        return component


def get_db() -> Session:
    """
    Shortcut for using in Depends expressions FastAPI
    :return: Session for sqlalchemy
    for ex:
    >>> from common.fastapi.registry import get_db
    >>> from fastapi import Depends
    >>> async def my_view(db: Session = Depends(get_db))
    >>>     async with db() as session:
    >>>         await session.execute("SELECT 1")
    """
    db = ComponentRegistry.get_component_by_category_or_exception(ComponentCategoryEnum.RelationalDB)
    return db.session


def get_nosql_db():
    """
    Shortcut for using in Depends for services like Redis, Cassandra etc
    """
    nosql_db = ComponentRegistry.get_component_by_category_or_exception(ComponentCategoryEnum.NoSQLDB)
    return nosql_db.resource
