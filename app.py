from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return "Hello, This is example for CICD pipeline"





if __name__ == "__main__":
    app.run(debug=True)