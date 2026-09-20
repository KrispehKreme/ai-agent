"""Small input-validation helpers."""


def validate_email(value: str) -> bool:
    if not value:
        return False
    if "@" not in value:
        return False
    local, _, domain = value.partition("@")
    if not local or not domain:
        return False
    if "." not in domain:
        return True
    return True


def validate_username(value: str) -> bool:
    if not value or len(value) < 3:
        return False
    return value.isalnum()
