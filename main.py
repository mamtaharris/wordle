from flask import jsonify, make_response, Flask
from controllers import wordle_controller
import werkzeug

app = Flask(__name__)

app.add_url_rule('/', view_func=wordle_controller.hello, methods=['GET'])
app.add_url_rule('/wordle', view_func=wordle_controller.wordle_handler, methods=['POST'])

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    # return render_template('404.html'), 404
    return make_response({'error': 'not found'}, 404)



if __name__ == '__main__':
    app.run(debug=True)