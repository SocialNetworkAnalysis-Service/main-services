from flask import Flask
from flask_admin import Admin
from flask_babelex import Babel
from flask_basicauth import BasicAuth

from src.db.database import sync_session
from src.models.users.model import Users
from src.models.verification_codes.model import VerificationCodes
from src.models.users.admin import UsersAdminView
from src.models.verification_codes.admin import VerifCodesAdminView

from src.config import config

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = config.flask_admin_swatch
app.config["BASIC_AUTH_USERNAME"] = config.basic_auth_username
app.config["BASIC_AUTH_PASSWORD"] = config.basic_auth_password
app.config["BASIC_AUTH_FORCE"] = config.basic_auth_force

basicauth = BasicAuth(app)

babel = Babel(app)


@babel.localeselector
def get_locale():
    return "ru"


admin = Admin(app, name='Social-Network', template_mode='bootstrap4')

admin.add_view(UsersAdminView(Users, sync_session))
admin.add_view(VerifCodesAdminView(VerificationCodes, sync_session))