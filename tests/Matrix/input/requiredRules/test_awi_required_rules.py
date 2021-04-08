import pytest
from decouple import config

# lgn = config("TSTXBN_L")
lgn = 'TSTXBN'
pwd = config("TSTXBN_P")


@pytest.mark.rr
@pytest.mark.parametrize("property_type",
                         [
                             pytest.param('Residential', marks=pytest.mark.rr_resi),
                             pytest.param('Residential New Home', marks=pytest.mark.rr_resi_nh),
                             pytest.param('Residential Lease', marks=pytest.mark.rr_rlse),
                             pytest.param('Residential Income', marks=pytest.mark.rr_rinc),
                             pytest.param('Land', marks=pytest.mark.rr_land),
                             pytest.param('Farm', marks=pytest.mark.rr_farm),
                             pytest.param('Manufactured in Park', marks=pytest.mark.rr_mprk),
                             pytest.param('Commercial Sale', marks=pytest.mark.rr_coms),
                             pytest.param('Commercial Lease', marks=pytest.mark.rr_coml),
                             pytest.param('Business Opportunity', marks=pytest.mark.rr_buso),
                             pytest.param('Specialty', marks=pytest.mark.rr_sptl),
                             pytest.param('Residential Comp', marks=pytest.mark.rr_comp)
                         ])
def test_required_rules_awi(app, property_type):
    app.navigation.to_login_page()
    app.session.login(lgn, pwd)
    app.navigation.to_input_form(property_type)
    app.valid_rules.check_required_rules()
