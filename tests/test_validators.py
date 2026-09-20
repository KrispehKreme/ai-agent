from scratch.validators import validate_email, validate_username


def test_validate_email_accepts_normal_address():
    assert validate_email("person@example.com") is True


def test_validate_email_rejects_missing_dot_in_domain():
    assert validate_email("person@localhost") is False


def test_validate_username_accepts_alnum():
    assert validate_username("abc123") is True


def test_validate_username_rejects_short():
    assert validate_username("ab") is False
