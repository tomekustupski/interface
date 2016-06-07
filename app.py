import os, boto3
from album_queue import request_album
from uuid import uuid4
from flask import Flask, render_template, jsonify, request, send_from_directory
app = Flask(__name__)

bucket_address = 'https://s3.eu-central-1.amazonaws.com/153412-kkanclerz'

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
  return render_template('upload_form.html', uploadButtonName="send")

@app.route("/upload", methods=['POST'])
def upload():
  files = request.files
  album = {
    'photos': []
  }
  for f in files.getlist('file'):
    print f
    destination_name = generate_filename(f)
    album['photos'].append('%s/%s' % (bucket_address, destination_name))
    upload_s3(f, destination_name)
  return jsonify(album)

@app.route("/request-album", methods=['POST'])
def request_album_creation():
  album = {
    'photos': [
      'https://s3.eu-central-1.amazonaws.com/153412-kkanclerz/photos/009d30b3d9a143a5937fbab9a50a4009/empty_image.jpg',
      'https://s3.eu-central-1.amazonaws.com/153412-kkanclerz/photos/009d30b3d9a143a5937fbab9a50a4009/empty_image.jpg'
    ]
  }
  request_album(album)
  return jsonify()

def upload_s3(source_file, destination_filename):
  bucket_name = '153412-kkanclerz'
  s3 = boto3.resource('s3')
  bucket = s3.Bucket(bucket_name)
  bucket.put_object(Key=destination_filename, Body=source_file)

def generate_filename(source_file):
  destination_filename = "photos/%s/%s" % (uuid4().hex, source_file.filename)
  return destination_filename

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
