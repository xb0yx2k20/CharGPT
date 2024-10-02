from flask import Flask, render_template, request
from g4f.client import Client

app = Flask(__name__)

# Инициализация клиента
client = Client()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем вопрос от пользователя
        user_question = request.form['question']
        
        # Запрашиваем ответ от модели GPT-3.5-turbo через g4f.client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_question}]
        )
        
        # Получаем текст ответа
        bot_answer = response.choices[0].message.content
        
        # Возвращаем шаблон с вопросом и ответом
        return render_template('index.html', question=user_question, answer=bot_answer)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)