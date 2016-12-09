#-*- coding: utf-8 -*- 
import csv
import sqlite3
from datetime import datetime
import re


# Database Connection Info
db="C:\\Users\\User\\Dev\\LocalVersion\\LocalVersion\\db.sqlite3"
# con = sqlite3.connect(db)
try:
    conn = sqlite3.connect(db)
    #conn.text_factory = lambda x: (x, "utf-8", "ignore")
except Exception:
    print"No Connection"


# Get cursor
cursor = conn.cursor()

ifile  = open('C:\Users\User\Dev\LocalVersion\data.csv', "rb")
reader = csv.reader(ifile)
rownum = 0
DATE_FIELD = 0
PRICE_FIELD = 1
FULL_MARKET = 4
VAT_FIELD = 6
str_a = ""
price_insert = 0.0
full = 0

cursor.execute("TRUNCATE TABLE arealyser_ppr")
reader.next() #skip the first line
for row in reader:
    #Format the date
    dt = datetime.strptime(row[DATE_FIELD], '%m/%d/%Y')
    date_sale = dt.isoformat()
    #Format the price from string
    str_a = row[PRICE_FIELD]
    if str_a.find("**") != -1:
      full = 1
    str_a = str_a.translate(None, " ,€*").decode('unicode_escape').encode('ascii','ignore')
    price_insert = float(str_a)
    full = 0  # reset not_full_market to false  
    address = row[2].decode('utf8')
    county = row[3]
    args = (date_sale, price_insert, address, county, full)
    #cursor.execute("INSERT INTO arealyser_ppr(date_of_sale, price, address, county, not_full_market)" "VALUES (?,?,?,?,?)", args)
    print date_sale, price_insert, address, county, full
    # count += 1
        
ifile.close()             

cursor.close()

conn.commit()

conn.close()

print"Script has successfully run!"