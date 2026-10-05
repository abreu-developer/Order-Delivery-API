from src.user_cases.registry_order import RegistryOrder
from src.models.repositories.orders_repository import OrderRepository
from src.models.connection.connection_handler import db_connection_handler


def registry_order_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrderRepository(conn)
    use_case = RegistryOrder(model)

    return use_case
