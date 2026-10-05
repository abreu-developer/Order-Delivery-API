import pytest

from src.models.connection.connection_handler import DbConnectionHandler

from .orders_repository import OrderRepository


db_connection_handler = DbConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="interage com o banco")
def test_insert_documents():
    order_repository = OrderRepository(conn)
    my_doc = {
        "ola": "mundo",
        "valor": 4
    }
    order_repository.insert_document(my_doc)


@pytest.mark.skip(reason="interage com o banco")
def test_insert_list_documents():
    order_repository = OrderRepository(conn)
    my_doc = [
        {"ola": "casa"},
        {"ola": "mundo novamente"}
    ]

    order_repository.insert_list_of_document(my_doc)


@pytest.mark.skip(reason="interage com o banco")
def test_select_many():
    order_repository = OrderRepository(conn)
    doc_filter = {
        "cupom": True
    }
    response = order_repository.select_many(doc_filter)

    for doc in response:
        print(doc)


@pytest.mark.skip(reason="interage com o banco")
def test_select_one():
    order_repository = OrderRepository(conn)
    doc_filter = {
        "client": "joao"
    }
    response = order_repository.select_one(doc_filter)

    print()
    print(response)


@pytest.mark.skip(reason="interage com o banco")
def test_select_many_with_properties():
    order_repository = OrderRepository(conn)
    doc_filter = {
        "cupom": True
    }
    response = order_repository.select_many_with_properties(doc_filter)

    for doc in response:
        print(doc)


@pytest.mark.skip(reason="interage com o banco")
def test_select_with_properties_exists():
    order_repository = OrderRepository(conn)
    response = order_repository.select_if_property_exists()

    for doc in response:
        print(doc)


@pytest.mark.skip(reason="interage com o banco")
def test_select_many_multiple_filters():
    order_repository = OrderRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.refri": {"$exists": True}
    }
    response = order_repository.select_many(doc_filter)

    for doc in response:
        print(doc)


@pytest.mark.skip(reason="interage com o banco")
def test_select_by_object_id():
    order_repository = OrderRepository(conn)
    object_id = "6ac18b86fbc5d7306c04d512"
    response = order_repository.select_by_object_id(object_id)

    print(response)

@pytest.mark.skip(reason="interage com o banco")
def test_edit_registry():
    order_repository = OrderRepository(conn)
    order_repository.edit_registry()


@pytest.mark.skip(reason="interage com o banco")
def test_edit_registry_increment():
    order_repository = OrderRepository(conn)
    order_repository.edit_registry_increment()
