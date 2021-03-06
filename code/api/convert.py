from flask import Blueprint

from api import converter
from api.schemas import ArgumentsSchema
from api.utils import get_json

convert_api = Blueprint('convert', __name__)


@convert_api.route('/convert', methods=['POST'])
def convert():
    arguments = get_json(schema=ArgumentsSchema())
    indicators_bulk = converter.convert(arguments)
    response = {'indicators': indicators_bulk}
    return response
