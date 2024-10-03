from flask import Flask, request
from g4f.client import Client

app = Flask(__name__)

client = Client()

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()

    user_question = data.get('question', '')
    context = data.get('context')  # История сообщений (список)

    if not user_question:
        return "Question is required", 400

    context.append({"role": "user", "content": user_question})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=context
        )

        bot_answer = response.choices[0].message.content

        return bot_answer

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)