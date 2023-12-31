from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello-world-<variant>')
def hello_world(variant):
   return f'Hello World {variant}', 200

if __name__ == '__main__':
   app.run(debug=True)