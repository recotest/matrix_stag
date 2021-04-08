import pytest
from decouple import config

lgn = config("TSTYBI_L")
pwd = config("TSTYBI_P")


@pytest.mark.create_contact
def test_contacts_remove_all(app):
    app.navigation.to_login_page()
    app.session.login(lgn, pwd)
    app.navigation.to_contacts()
    app.contacts.remove_all_contacts()


@pytest.mark.remove_contact
def test_contacts_create(app):
    app.navigation.to_login_page()
    app.session.login(lgn, pwd)
    app.navigation.to_contacts()
    for i in range(3):
        app.contacts.create_contact_required()
