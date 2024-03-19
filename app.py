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
                /* CSS styles applied to the page elements */
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                    margin: 0;
                    padding: 0;
                }
                
                .container {
                    width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }
                
                h1 {
                    color: #333;
                    text-align: center;
                }
                
                p {
                    color: #666;
                    line-height: 1.5;
                }
                
                .size {
                    font-size: 8px;
                    color: red;
                }
                
                .button {
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: #fff;
                    text-decoration: none;
                    border-radius: 5px;
                    margin-bottom: 10px;
                }
                
                .image {
                    text-align: center;
                    margin-bottom: 10px;
                }
                
                .block {
                    background-color: #ddd;
                    padding: 10px;
                    margin-bottom: 10px;
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

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
