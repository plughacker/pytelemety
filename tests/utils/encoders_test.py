import json
from datetime import date, datetime
from uuid import UUID

import pytest

from pytelemetry.utils.encoders import CustomEncoder


class ClassTeste:
    variable_teste = 123


def function_test():
    ...


@pytest.fixture
def encoder():
    return CustomEncoder()


@pytest.mark.parametrize(
    'options',
    [
        (
            UUID('123e4567-e89b-12d3-a456-426614174000'),
            '123e4567-e89b-12d3-a456-426614174000',
        ),
        (date(2023, 10, 18), '2023-10-18'),
        (datetime(2023, 10, 18, 12, 30, 45), '2023-10-18T12:30:45Z'),
        (function_test, function_test.__name__),
        (ClassTeste(), ClassTeste().__class__.__name__),
        (ValueError('a is not a number'), 'a is not a number'),
    ],
)
def test_uuid_encoder(encoder: CustomEncoder, options):
    value, exepecte_value = options
    assert encoder.default(value) == exepecte_value


def test_encode():
    obj = {
        'UUID': UUID('123e4567-e89b-12d3-a456-426614174000'),
        'date': date(2023, 10, 18),
        'datetime': datetime(2023, 10, 18, 12, 30, 45),
        'function_test': function_test,
        'ClassTeste': ClassTeste(),
        'ValueError': ValueError('a is not a number'),
    }
    try:
        assert json.dumps(obj, cls=CustomEncoder)
    except Exception as error:
        assert False, error
