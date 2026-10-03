import pytest
from src.models.connection.connection_handler import DbConnectionHandler
from .orders_repository import OrderRepository


db_connnection_handler = DbConnectionHandler()
db_connnection_handler.connect_to_db()
conn = db_connnection_handler.get_db_connection()

@pytest.mark.skip(reason="interage com o banco")
def test_insert_documents():
    order_repository = OrderRepository(conn)
    my_doc = {"ola":"mundo", "valor": 4}
    order_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interage com o banco")
def test_insert_list_documents():
    order_repository = OrderRepository(conn)
    my_doc = [{"ola":"casa"},{"ola":"mundo novamente"}]
    order_repository.insert_list_of_document(my_doc)
