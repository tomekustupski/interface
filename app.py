import os
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
  return render_template('upload_form.html', uploadButtonName="send")

@app.route("/upload", methods=['POST'])
def upload():
  files = request.files
  for f in files.getlist('file'):
    filename = f.filename
    updir = '/home/ec2-user/s3-2/upload'
    f.save(os.path.join(updir, filename))
  return jsonify()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
