from src.user_cases.registry_finder import FindOrder
from src.models.repositories.orders_repository import OrderRepository
from src.models.connection.connection_handler import db_connection_handler


def registry_finder_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrderRepository(conn)
    use_case = FindOrder(model)

    return use_case
