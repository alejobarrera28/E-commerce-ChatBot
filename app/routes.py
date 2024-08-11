from flask import Blueprint, request, jsonify, render_template
from .model import process_input

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_text = data.get('input')
    output_text = process_input(input_text)
    return jsonify({'output': output_text})
