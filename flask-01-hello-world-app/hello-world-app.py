from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world from Flask!!!"

@app.route('/second')
def second():
    return "murası merkez"

@app.route('/third/subthird')
def third():
    return "this is the subpage of third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page {id}'



if __name__=='__main__':
    app.run(debug=True)