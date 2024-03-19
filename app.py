import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flask App</title>
            <style>
                /* CSS стили применяемые к элементам страницы */
                body {
                    font-family: Arial, sans-serif; /* Устанавливаем шрифт для всего документа */
                    background-color: #f2f2f2; /* Устанавливаем цвет фона */
                    margin: 0; /* Убираем отступы по умолчанию */
                    padding: 0; /* Убираем внутренние отступы по умолчанию */
                }
                
                .container {
                    width: 600px; /* Устанавливаем ширину контейнера */
                    margin: 0 auto; /* Выравниваем контейнер по центру */
                    padding: 20px; /* Добавляем внутренние отступы */
                    background-color: #fff; /* Устанавливаем цвет фона контейнера */
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Добавляем тень контейнеру */
                }
                
                h1 {
                    color: #333; /* Устанавливаем цвет заголовка */
                    text-align: center; /* Выравниваем заголовок по центру */
                }
                
                p {
                    color: #666; /* Устанавливаем цвет текста */
                    line-height: 1.5; /* Устанавливаем межстрочный интервал */
                }
                
                .size {
                    font-size: 8px; /* Устанавливаем размер шрифта */
                    color: red; /* Устанавливаем цвет шрифта */
                }
                
                .button {
                    display: inline-block; /* Отображаем кнопку в виде блока */
                    padding: 10px 20px; /* Добавляем внутренние отступы кнопки */
                    background-color: #4CAF50; /* Устанавливаем цвет фона кнопки */
                    color: #fff; /* Устанавливаем цвет текста кнопки */
                    text-decoration: none; /* Убираем подчеркивание текста кнопки */
                    border-radius: 5px; /* Закругляем углы кнопки */
                    margin-bottom: 10px; /* Добавляем отступ снизу */
                }
                
                .image {
                    text-align: center; /* Выравниваем изображение по центру */
                    margin-bottom: 10px; /* Добавляем отступ снизу */
                }
                
                .block {
                    background-color: #ddd; /* Устанавливаем цвет фона блока */
                    padding: 10px; /* Добавляем внутренние отступы блока */
                    margin-bottom: 10px; /* Добавляем отступ снизу */
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello Flask from alpine-linux!</h1>
                <p>Size on the page: <span class="size">8</span></p>
                <a href="#" class="button">Button 1</a>
                <a href="#" class="button">Button 2</a>
                <a href="#" class="button">Button 3</a>
                
                <div class="image">
                    <img src="https://example.com/image1.jpg" alt="Image 1">
                </div>
                
                <div class="image">
                    <img src="https://example.com/image2.jpg" alt="Image 2">
                </div>
                
                <div class="block">
                    <h3>Block 1</h3>
                    <p>This is block 1 content.</p>
                </div>
                
                <div class="block">
                    <h3>Block 2</h3>
                    <p>This is block 2 content.</p>
                </div>
            </div>
        </body>
        </html>
    '''

if ____name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
