import pytest

from decouple import config


LGN = config("TSTXBN_L")
PWD = config("TSTXBN_P")

@pytest.mark.filterwarnings('ignore::PytestUnknownMarkWarning')
@pytest.mark.resi_sfr
@pytest.mark.parametrize("mls_status",
                         [
                             pytest.param('active', marks=pytest.mark.test_01),
                             pytest.param('pending', marks=pytest.mark.test_02),
                             pytest.param('expired', marks=pytest.mark.test_03),
                             pytest.param('withdrawn', marks=pytest.mark.test_04),
                             pytest.param('closed', marks=pytest.mark.test_05),
                             pytest.param('incomplete', marks=pytest.mark.test_06),
                             pytest.param('coming_soon', marks=pytest.mark.test_07)
                         ])
def test_resi_sfr(app, mls_status):
    app.navigation.to_login_page()
    app.session.login(LGN, PWD)
    app.navigation.to_input_form("Residential")
    app.resi_sfr.populate_input_form(mls_status, LGN)
    app.session.logout()

@pytest.mark.lg
def test_login_logout(app):
    app.navigation.to_login_page()
    app.session.login(LGN, PWD)
    app.session.logout()
