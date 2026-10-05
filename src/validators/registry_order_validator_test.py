import pytest
from .registry_order_validator import registry_order_validator


def test_validator_order():
    body = {
        "data": {
            "name": "joaozinho",
            "address": "rua do limao",
            "cupom": False,
            "items": [
                {
                    "item": "Refrigerante",
                    "quantidade": 2
                },
                {
                    "item": "pizza",
                    "quantidade": 3
                }
            ]
        }
    }

    registry_order_validator(body)




def test_validator_order_error():
    body = {
        "data": {
            "name": "joaozinho",
            "cupom": False,
            "items": [
                {
                    "item": "Refrigerante",
                    "quantidade": 2
                },
                {
                    "item": "pizza",
                    "quantidade": 3
                }
            ]
        }
    }

    with pytest.raises(Exception):
        registry_order_validator(body)
