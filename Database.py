# i made this in like 2 mins

import json

class database:
  def __init__(self):
    self.db = {

    }

  def init_db(self, file):
    try:
      with open(file, 'r') as openfile:
        json_object = json.load(openfile)

      self.db = json_object
    except:
      return False

  def get_key(self, key):
    if self.db[key]:
      return self.db[key]
    else:
      return KeyError

  def set_key(self, key, item):
    self.db[key] = item

  def clear_db(self):
    self.db = {}

  def get_db_dict(self):
    return(self.db)

  def get_db_file(self, file):
    with open(file, 'r') as f:
      return json.load(f)

  def save_db(self, file):    
    json_object = json.dumps(self.db, indent = 4)

    with open(file, "w") as outfile:
      outfile.write(json_object)
