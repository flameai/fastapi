from collections import defaultdict
from common.fastapi.config import ComponentCategoryGetterEnum


class NotExistingRelationalDatabaseSettings(Exception):
    pass


class NotExistingNoSQLDatabaseSettings(Exception):
    pass


mapping = {
    ComponentCategoryGetterEnum.RelationalDB: NotExistingRelationalDatabaseSettings,
    ComponentCategoryGetterEnum.NoSQLDB: NotExistingNoSQLDatabaseSettings
}


def get_exception_for_component(component: ComponentCategoryGetterEnum):
    return mapping[component] if component in mapping else Exception(
        f"Cant get component {component} from application.")
