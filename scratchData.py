############################################################
##    FILENAME:   scratchData.py    
##    VERSION:    1.0
##    SINCE:      2014-11-14
##    AUTHOR: 
##        Jimmy Lin <jimmylin@cs.utexas.edu>*
##        Hsiang-Fu Yu <rofuyu@cs.utexas.edu>
##        Zhong Kai <zhongkai@ices.utexas.edu>
##        Ian Yen <ianyen@cs.utexas.edu>   
##
############################################################
##    Edited by MacVim
##    Documentation auto-generated by Snippet 
############################################################

import mysql.connector
from mysql.connector import errorcode

FEAT_SEP = " "
INS_SEP = "\n"
f = open("data", "wb+")

## TODO: input database configuration
config = {
  'user': 'scott',
  'password': 'tiger',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,
}

## TODO: SQL query
query = ("SELECT * FROM TABLES")

## connect database with exception control
try:
    connection = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    else:
        print(err)
else:
    print("Succefully Connected.")
    ## TODO: Fetch data from database right here..
    cur = connection.cursor()
    cur.execute(query)
    for instance in cur:
        ins_str = ""
        for feat in instance:
            ins_str += FEAT_SEP + str(feat)
        f.write(ins_str)
        f.write(INS_SEP)
    cur.close()
finally:
    connection.close()

f.close()
