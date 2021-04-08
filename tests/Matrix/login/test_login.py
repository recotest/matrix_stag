from decouple import config

lgn = config("TSTYBI_L")
pwd = config("TSTYBI_P")


def test_login_as_tstybi(app):
    app.navigation.to_login_page()
    app.session.login(lgn, pwd)
    app.session.logout()
