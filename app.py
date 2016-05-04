from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
  return render_template('upload_form.html', uploadButtonName="send")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
