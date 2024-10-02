from flask import Flask
import Task_Library

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

if __name__ == '__main__':
    app.run(debug=True)
    
