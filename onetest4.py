# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_one(app):
    app.open_catalog_page()
    app.open_autorisation()
    app.autorisation(Group(username="ekylasov@gmail.com", password="2730443rusPERM"))
    app.logout()
