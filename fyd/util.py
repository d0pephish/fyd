from werkzeug.routing import BaseConverter, ValidationError
import re

YT_RE = re.compile( r'^[a-zA-Z0-9_-]{11}$' )

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
