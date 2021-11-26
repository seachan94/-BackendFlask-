from flask import Flask, request
import data
app = Flask(__name__)

@app.route('/android',methods = ['GET'])
def get():
    
    print(request.args.get("test"))

    return { "result" : "get ok" }

@app.route('/android',methods = ['POST'])
def post():
    print(request.json)
    get_data = data.TestPost(request.json)
    print(get_data.user)
    return { "result" : "post ok" }


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)