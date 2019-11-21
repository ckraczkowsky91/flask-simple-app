from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/simple-app')
def home():
    return '<p style="color: red">Hiyee!</p>'

if __name__ == 'main':
    app.run()
else :
    print('error')
