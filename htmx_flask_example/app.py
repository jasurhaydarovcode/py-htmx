from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f'<div id="result"><p>Salom, {name}!</p></div>'

if __name__ == '__main__':
    app.run(debug=True)
