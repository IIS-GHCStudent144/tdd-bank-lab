import pytest

from bank import transfer_funds


@pytest.fixture
def source_account():
    return {"id": 1001, "balance": 250.0, "owner": "Alice Johnson"}


@pytest.fixture
def destination_account():
    return {"id": 1002, "balance": 120.0, "owner": "Bob Smith"}


def test_transfer_funds_returns_transaction_details_for_valid_transfer(
    source_account, destination_account
):
    transaction = transfer_funds(source_account, destination_account, 75.0)

    assert transaction == {
        "from_id": 1001,
        "to_id": 1002,
        "amount": 75.0,
        "from_balance_after": 175.0,
        "to_balance_after": 195.0,
    }
    assert source_account["balance"] == 175.0
    assert destination_account["balance"] == 195.0


@pytest.mark.parametrize("invalid_amount", [0, -10.5])
def test_transfer_amount_must_be_greater_than_zero(source_account, destination_account, invalid_amount):
    with pytest.raises(ValueError, match="greater than zero"):
        transfer_funds(source_account, destination_account, invalid_amount)


def test_transfer_requires_sufficient_funds(source_account, destination_account):
    with pytest.raises(ValueError, match="sufficient funds"):
        transfer_funds(source_account, destination_account, 300.0)


def test_transfer_requires_distinct_source_and_destination_accounts(source_account):
    with pytest.raises(ValueError, match="different"):
        transfer_funds(source_account, source_account, 50.0)
