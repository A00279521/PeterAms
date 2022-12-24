from flask import Flask, redirect


app = Flask(__name__)


@app.route('/home')
def hello_internet():
    return 'num*num'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)