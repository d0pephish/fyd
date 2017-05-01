from flask import render_template, Response, abort
from fyd import app, DIRS
from fyd import worker 
import json
import re

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/do/<yt:v>/grab')
def grab(v):
  return json.dumps(worker.handle_grab(v))

@app.route('/do/<yt:v>/status')
def get_status(v):
  return json.dumps(worker.get_video_status(v))

@app.route('/do/<yt:v>/download')
def download(v):
  data,title = worker.handle_download(v)
  if(data != False):
    r = Response(data, mimetype="video/mp4")
    r.headers["Content-Disposition"] = "attachment; filename="+title.decode('ascii','ignore').replace(" ","_")+".mpg"
    return r
  else:
    abort(404)
