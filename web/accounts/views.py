from flask import Blueprint

accounts_bp = Blueprint('accounts', __name__, template_folder='templates',
    static_folder='static')

@accounts_bp.route('/', methods=['GET'])
def index():
    return 'Accounts Page'