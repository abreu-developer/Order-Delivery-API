from .orders_repository import OrderRepository


class CollectionMock:
    def __init__(self) -> None:
        self.insert_attributes = {}
        self.find_attributes = {}
        self.update_attributes = {}
        self.delete_attributes = {}

    def insert_one(self, input_data: any):
        self.insert_attributes["dict"] = input_data

    def insert_many(self, input_data: any):
        self.insert_attributes["list"] = input_data

    def find(self, *args):
        self.find_attributes["args"] = args

    def find_one(self, *args):
        self.find_attributes["args"] = args

    def update_one(self, *args):
        self.update_attributes["args"] = args

    def update_many(self, *args):
        self.update_attributes["args"] = args

    def delete_one(self, *args):
        self.delete_attributes["args"] = args

    def delete_many(self, *args):
        self.delete_attributes["args"] = args


class DbCollectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_attributes = {}
        self.collection = collection

    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection


def test_insert_document():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    doc = {"alguma": "coisa"}
    repo.insert_document(doc)

    assert collection.insert_attributes["dict"] == doc


def test_insert_list_of_document():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    docs = [
        {"alguma": "coisa"},
        {"outra": "coisa"}
    ]

    repo.insert_list_of_document(docs)

    assert collection.insert_attributes["list"] == docs


def test_select_many():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    doc_filter = {
        "cupom": True
    }

    repo.select_many(doc_filter)

    assert collection.find_attributes["args"][0] == doc_filter


def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    doc_filter = {
        "cupom": True
    }

    repo.select_many_with_properties(doc_filter)

    assert collection.find_attributes["args"][0] == doc_filter
    assert collection.find_attributes["args"][1] == {
        "_id": 0,
        "cupom": 0
    }


def test_select_one():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    doc_filter = {
        "client": "joao"
    }

    repo.select_one(doc_filter)

    assert collection.find_attributes["args"][0] == doc_filter


def test_select_if_property_exists():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    repo.select_if_property_exists()

    assert collection.find_attributes["args"][0] == {
        "address": {"$exists": True}
    }

    assert collection.find_attributes["args"][1] == {
        "_id": 0,
        "cupom": 0
    }


def test_select_by_object_id():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    object_id = "6ac18b86fbc5d7306c04d512"

    repo.select_by_object_id(object_id)

    assert str(
        collection.find_attributes["args"][0]["_id"]
    ) == object_id


def test_edit_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    repo.edit_registry()

    assert str(
        collection.update_attributes["args"][0]["_id"]
    ) == "6ac18b86fbc5d7306c04d512"

    assert collection.update_attributes["args"][1] == {
        "$set": {
            "itens.refri.quant": 25
        }
    }


def test_edit_many_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    repo.edit_many_registry()

    assert collection.update_attributes["args"][0] == {
        "itens.refri": {
            "$exists": True
        }
    }

    assert collection.update_attributes["args"][1] == {
        "$set": {
            "itens.refri.quant": 250
        }
    }


def test_edit_registry_increment():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    repo.edit_registry_increment()

    assert str(
        collection.update_attributes["args"][0]["_id"]
    ) == "6ac18b86fbc5d7306c04d512"

    assert collection.update_attributes["args"][1] == {
        "$inc": {
            "itens.refri.quant": 25
        }
    }


def test_delete_registies():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    repo.delete_registies()

    assert str(
        collection.delete_attributes["args"][0]["_id"]
    ) == "6ac18ad8fbc5d7306c04d513"


def test_delete_many_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    repo.delete_many_registry()

    assert collection.delete_attributes["args"][0] == {
        "itens.refri": {
            "$exists": True
        }
    }


def test_delete_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrderRepository(db_connection)

    repo.delete_registry()

    assert str(
        collection.delete_attributes["args"][0]["_id"]
    ) == "6ac18b86fbc5d7306c04d512"