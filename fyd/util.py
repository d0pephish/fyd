from werkzeug.routing import BaseConverter, ValidationError
import re

YT_RE = re.compile( r'^[a-zA-Z0-9_-]{11}$' )
accepted_resolutions = ["4k60fps",
                        "4k30fps",
                        "1440p60fps",
                        "1440p30fps",
                        "1080p60fps",
                        "1080p",
                        "720p60fps",
                        "720p",
                        "480p",
                        "360p",
                        "240p"]

class youtubeResolutionConverter(BaseConverter):
    def __init__(self, map, strict=True):
      super(youtubeResolutionCOnverter, self).__init__(map)
      self.strict = strict
     
    def to_python(self, value):
      if self.strict and value in accepted_resolutions:
        raise ValidationError()
      try:
        return str(value)
      except:
        ValidationError()

    def to_url(self, value):
      return str(value)

class youtubeIdConverter(BaseConverter):
    def __init__(self, map, strict=True):
      super(youtubeIdConverter, self).__init__(map)
      self.strict = strict
    
    def to_python(self, value):
      if self.strict and not YT_RE.match(value):
        raise ValidationError()
      try:
        return str(value)
      except:
        ValidationError()

    def to_url(self, value):
      return str(value)
