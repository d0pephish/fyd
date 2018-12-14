from fyd import DIRS
import os, time

def get_video_status(v):
  for k in ["queue","done","working"]:
    current_queue = os.listdir(DIRS[k])
    if v in current_queue:
      f = open(DIRS[k] + "/" + v, "r")
      text = f.read()
      f.close()
      timestamp = text[:24]
      title = text[25:]
      return { "status" : k, "time" : timestamp, "title" : title }
  return False  

def handle_grab(v, res="best"):
  status = get_video_status(v)
  if not status:
    timestamp = time.strftime("%c")
    f = open(DIRS["queue"] + "/" + v, "w")
    f.write(timestamp)
    f.close()
    return { "status" : "created", "time" : timestamp }
  else:
    return status
def handle_download(v):
  status = get_video_status(v)
  if not status or status["status"] != "done":
    return False,False,False
  filename = v+".mp4"
  directory = "/".join(DIRS["downloads"].split("/")[1:])
  path = DIRS["downloads"] + "/"+ filename 
  if not os.path.isfile(path):
    return False,False,False
#  f = open(path, "r")
#  data = f.read()
#  f.close()
  return directory,filename,status["title"]
