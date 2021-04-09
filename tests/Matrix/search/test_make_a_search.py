import pytest
from decouple import config

lgn = 'TSTXBN'
pwd = config("TSTXBN_P")


@pytest.mark.resi_search
def test_resi_search(app):
    app.navigation.to_login_page()
    app.session.login(lgn, pwd)
    app.navigation.to_searchForm("Residential")
    app.search.make_resi_search()


@pytest.mark.search_all
def test_prompt_with_get_method(app):
    property_types = ["Residential",
                      "ResidentialLease",
                      "ResidentialIncome",
                      "Land",
                      "Farm",
                      "ManufacturedInPark",
                      "Commercial",
                      "BusinessOpportunity",
                      "Specialty",
                      "CrossProperty"
                      ]

    app.navigation.to_login_page()
    app.session.login(lgn, pwd)
    for property_type in property_types:
        app.navigation.to_searchForm(property_type)
        app.search.street_number_width()
