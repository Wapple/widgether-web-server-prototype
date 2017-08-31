from flask import Blueprint

widgets_bp = Blueprint('widgets', __name__, template_folder='templates',
    static_folder='static')

@widgets_bp.route('/', methods=['GET'])
def index():
    return 'Widgets Page'