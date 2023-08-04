from flask import Flask

'''importing request module to insert value in the web API'''
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>shubham renguntha chutya ahe</h1>"

@app.route("/garima_yadav")
def garima_yadav():
    return "<h1>I LOVE YOU </h1>"

@app.route("/duga")
def duga():
    return "<h1>ALWAYS BE HAPPY AND KEEP SMILING DHRUVI BAGARIA 😃</h1>"

@app.route("/test")
def test():
    a = 5+6 
    return "this is my function to run app {}".format(a)

@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return  "this is a data input form my url {}".format(data)

'''request is for inserting value in form of argumnet that is 
why arg is used and to enter the value used get function'''

if __name__=="__main__":
    app.run(host="0.0.0.0")
