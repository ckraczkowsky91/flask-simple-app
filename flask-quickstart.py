from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/simple-app')
def home():
    return '<h1 style="color: red">Hiyee!</h1>'

if __name__ == 'main':
    app.run()
else :
    print('error')
