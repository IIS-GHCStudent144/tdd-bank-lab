def transfer_funds(from_account, to_account, amount):
    """
    Transfer amount from from_account to to_account.

    Each account is a dict: {"id": int, "balance": float, "owner": str}

    Returns a transaction dict on success.
    Raises ValueError for invalid inputs.
    """
    if not isinstance(from_account, dict) or not isinstance(to_account, dict):
        raise ValueError("Accounts must be dictionaries")

    required_keys = {"id", "balance", "owner"}
    if not required_keys.issubset(from_account.keys()) or not required_keys.issubset(to_account.keys()):
        raise ValueError("Accounts must include id, balance, and owner")

    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Transfer amount must be greater than zero")

    amount = float(amount)
    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero")

    if from_account is to_account or from_account.get("id") == to_account.get("id"):
        raise ValueError("Source and destination accounts must be different")

    if from_account.get("balance", 0) < amount:
        raise ValueError("Source account has insufficient funds")

    from_account["balance"] = float(from_account["balance"]) - amount
    to_account["balance"] = float(to_account["balance"]) + amount

    return {
        "from_id": from_account["id"],
        "to_id": to_account["id"],
        "amount": amount,
        "from_balance_after": from_account["balance"],
        "to_balance_after": to_account["balance"],
    }