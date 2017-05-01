from flask import Flask
from util import *
import os, sys, atexit
from werkzeug.serving import is_running_from_reloader
import threading
from fyd.downloader import *

DIRS = {"queue" : "queue", "downloads" :"downloads", "working" : "working", "done" : "done" }
# DIRS is the directories I will use for the flat file queue system. because sometimes sql is teh suxors


for k in DIRS.keys():
  if not os.path.isdir(DIRS[k]):
    if os.path.isfile(DIRS[k]):
      print "I need the following file to be a dir:", DIRS[k]
      sys.exit(1)
    else:
      print "creating dir:", DIRS[k]
      os.mkdir(DIRS[k])
  elif not os.access(DIRS[k], os.W_OK | os.X_OK ):
      print "I need +wx on the following directory:", DIRS[k]

def create_app():
  app = Flask(__name__)
  app.url_map.converters['yt'] = youtubeIdConverter
  
  def interrupt():
    global stillRunning
    stillRunning = False

  if not is_running_from_reloader():
    global DIRS
    t = threading.Thread(target=downloader,args=([ DIRS]))
    t.daemon = True
    t.start()

  return app
app = create_app()

from fyd import views


