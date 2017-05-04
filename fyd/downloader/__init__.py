from __future__ import print_function
import os, sys, time
import threading
import pytube
class downloader:
  interval = 30
  purge = 60
  def __init__(self,dirs):
    self.dirs = dirs
    self.start()
  
  def dbg(self,msg):
    print("[Worker Thread:] " + msg , file=sys.stderr)

  def iterate_queue(self):
    try:
      current_queue = os.listdir(self.dirs["queue"])
      for v in current_queue:
        self.dbg("working " + str(v))
        f = open(self.dirs["working"] + "/" + v, "w")
        timestamp = time.strftime("%c")
        f.write(timestamp)
        f.close()
        os.remove(self.dirs["queue"] + "/" + v)
        self.do_work(v)
    except:
      self.dbg("error iterating queue")
      
  def do_work(self,v):
    try:
      yt = pytube.YouTube("http://www.youtube.com/watch?v="+v)
      filename = yt.filename.encode('utf-8')
      yt.set_filename(v)
      video = yt.filter('mp4')[-1]
      video.download(self.dirs["downloads"] + "/")
      f = open(self.dirs["done"] + "/" + v, "w")
      timestamp = time.strftime("%c")
      f.write(timestamp+"\n"+filename)
      f.close()
      os.remove(self.dirs["working"] + "/" + v)
      self.dbg("done with " + str(v)) 
    except:
      self.dbg("error on this go " + str(v)) 
  
  def clean_up(self):
    try:
      done = os.listdir(self.dirs["done"])
      for v in done:
        f = open(self.dirs["done"] + "/" + v)
        t = f.read(24)
        f.close()
        t = time.strptime(t)
        t = time.mktime(t)
        t2 = time.time()
        if t2-t > (60*self.purge):
          self.dbg("purging " + str(v))
          os.remove(self.dirs["done"] + "/" + v)
          os.remove(self.dirs["downloads"] + "/" + v + ".mp4")
    except: 
      self.dbg("error on this clean")

  def start(self):
      self.iterate_queue()
      self.clean_up()
      time.sleep(self.interval)
      self.start()

