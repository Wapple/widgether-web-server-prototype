from flask import Blueprint

main_bp = Blueprint('main', __name__, template_folder='templates',
    static_folder='static')

@main_bp.route('/', methods=['GET'])
def index():
    return 'Main Page'