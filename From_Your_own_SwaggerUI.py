from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def swagger_ui():
    return render_template('swagger_ui.html')


@app.route('/spec')
def get_spec():
    return send_from_directory(app.root_path, 'swagger.yaml')


if __name__ == '__main__':
    app.run(debug=True)