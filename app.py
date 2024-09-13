from flask import Flask, request, jsonify
from flask_cors import CORS
from src.knowlegde_base_loader import knowledge_base_loader
from src.inference_engine import inference_engine

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

knowledge_base = knowledge_base_loader()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/recommendation', methods=['POST'])
def knowledge():
    if request.is_json:
        input_data = request.json.get('input_data', {})
        if input_data:
            recommendations = inference_engine(input_data, knowledge_base)
            return jsonify(recommendations)
        else:
            return jsonify({'error': 'No input data provided'}), 400
    else:
        return jsonify({'error': 'Content-Type must be application/json'}), 415


if __name__ == '__main__':
    app.run(debug=False)
