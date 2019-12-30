from app.email_utils import (
    get_email_name,
    get_email_part,
    get_email_local_part,
    get_email_domain_part,
)


def test_get_email_name():
    assert get_email_name("First Last <ab@cd.com>") == "First Last"
    assert get_email_name("First Last<ab@cd.com>") == "First Last"
    assert get_email_name("  First Last   <ab@cd.com>") == "First Last"
    assert get_email_name("ab@cd.com") == ""


def test_get_email_part():
    assert get_email_part("First Last <ab@cd.com>") == "ab@cd.com"
    assert get_email_part("First Last<ab@cd.com>") == "ab@cd.com"
    assert get_email_part("  First Last   <ab@cd.com>") == "ab@cd.com"
    assert get_email_part("ab@cd.com") == "ab@cd.com"


def test_get_email_local_part():
    assert get_email_local_part("ab@cd.com") == "ab"


def test_get_email_domain_part():
    assert get_email_domain_part("ab@cd.com") == "cd.com"
