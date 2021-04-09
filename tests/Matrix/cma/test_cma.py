import pytest
from decouple import config

lgn = 'TSTXBN'
pwd = config("TSTXBN_P")


@pytest.mark.cma
def test_cma(app):
    app.navigation.to_login_page()
    app.session.login(lgn, pwd)
    app.navigation.to_cma()
    app.cma.start_cma()
    app.cma.select_cma_contact()
    app.cma.pages_page()
    app.cma.subject_page()
    app.cma.cover_page()
    app.cma.comparables_page()
    app.cma.map_page()
    app.cma.adjustments_page()
    app.cma.pricing_page()
    app.cma.finish_page()


print(lgn)
