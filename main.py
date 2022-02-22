from flask import Flask
from controllers import wordle_controller

app = Flask(__name__)

app.add_url_rule('/', view_func=wordle_controller.hello, methods=['GET'])
app.add_url_rule('/wordle', view_func=wordle_controller.wordle_handler, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)