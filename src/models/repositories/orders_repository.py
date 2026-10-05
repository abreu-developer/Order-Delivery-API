from bson.objectid import ObjectId

from .interfaces.orders_repository_interface import OrderRepositoryInterface


class OrderRepository(OrderRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_document(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response

    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"address":{"$exists":True}},{"_id": 0, "cupom":0})
        return response

    def select_many(self, doc_filter: dict) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter,
            {"_id": 0, "cupom":0}#opçao de retorno
            )
        return data

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data

    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("6ac18b86fbc5d7306c04d512")},#filtros
            {"$set": {"itens.refri.quant": 25}}#ediçao
        )

    def edit_many_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            {"itens.refri":{"$exists": True}},#filtros
            {"$set": {"itens.refri.quant": 250}}#ediçao
        )

    def edit_registry_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("6ac18b86fbc5d7306c04d512")},#filtros
            {"$inc": {"itens.refri.quant": 25}}#ediçao
        )

    def delete_registies(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId("6ac18ad8fbc5d7306c04d513")})

    def delete_many_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many({"itens.refri":{"$exists": True}})

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId("6ac18b86fbc5d7306c04d512")})