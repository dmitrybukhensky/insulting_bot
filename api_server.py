from flask import Flask, request, jsonify
from api_client import get_insult
from bot import get_processed_message
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')


@app.route('/process', methods=['POST'])
def process():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    processed_message = get_processed_message(message)
    return jsonify({'processed_message': processed_message})


@app.route('/get_insult', methods=['GET'])
async def api_get_insult():
    # This endpoint will return an insult
    insult_text = await get_insult()
    return jsonify({'insult': insult_text})

if __name__ == "__main__":
    app.run(debug=True)
