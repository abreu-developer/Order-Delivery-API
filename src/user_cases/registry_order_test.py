
from unittest.mock import Mock

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from .registry_order import RegistryOrder


class TestRegistryOrder:

    def test_registry_order(self):
        # Arrange
        orders_repository = Mock()
        registry_order = RegistryOrder(orders_repository)

        http_request = HttpRequest(
            body={
                "data": {
                    "name": "João Vitor",
                    "address": "Rua A",
                    "cupom": True,
                    "items": [
                        {
                            "item": "Notebook",
                            "quantidade": 2
                        }
                    ]
                }
            }
        )

        # Act
        response = registry_order.registry(http_request)

        # Assert
        assert isinstance(response, HttpResponse)
        assert response.status_code == 201
        assert response.body["data"]["type"] == "order"
        assert response.body["data"]["count"] == 1
        assert response.body["data"]["registry"] is True

        orders_repository.insert_document.assert_called_once()

    def test_registry_order_with_invalid_body(self):
        # Arrange
        orders_repository = Mock()
        registry_order = RegistryOrder(orders_repository)

        http_request = HttpRequest(
            body={}
        )

        # Act
        response = registry_order.registry(http_request)

        # Assert
        assert response.status_code == 422
        assert "errors" in response.body

        orders_repository.insert_document.assert_not_called()

    def test_registry_order_insert_document(self):
        # Arrange
        orders_repository = Mock()
        registry_order = RegistryOrder(orders_repository)

        http_request = HttpRequest(
            body={
                "data": {
                    "name": "João Vitor",
                    "address": "Rua A",
                    "cupom": False,
                    "items": [
                        {
                            "item": "Mouse",
                            "quantidade": 1
                        }
                    ]
                }
            }
        )

        # Act
        registry_order.registry(http_request)

        # Assert
        orders_repository.insert_document.assert_called_once()

        new_order = orders_repository.insert_document.call_args[0][0]

        assert new_order["name"] == "João Vitor"
        assert new_order["address"] == "Rua A"
        assert new_order["cupom"] is False
        assert new_order["items"][0]["item"] == "Mouse"
        assert new_order["items"][0]["quantidade"] == 1
        assert "created_at" in new_order
