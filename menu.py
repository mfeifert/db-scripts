import sqlite3
import subprocess
import platform

if platform.system() == 'Linux':
    path = '/home/maf/docs/db/'
else: 
    path = '/Users/maf/docs/db/'

# change the string part of value of these variables to "test.db" for testing
health_db = path + "health.db"
auto_db = path + "auto.db"
media_db = path + "media.db"

def main():
    menu = [
    "",
    "1: Water",
    "2: Yoga",
    "3: Fuel",
    "4: Reading"
    ]
    for i in menu:
        print(i)
    choice = input("\n")
    if choice == "1":
        water()
    elif choice == "2":
        yoga()
    elif choice == "3":
        fuel()
    elif choice == "4":
        reading()

def sql_statement(db, statement):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(statement)
    con.commit()
    con.close()

def sql_select(db, statement):
    # SELECT statements are run via shell to produce the "-box" output format
    subprocess.run([f"sqlite3 -box {db} '{statement}'"], shell=True)
    # subprocess.run(["sqlite3", "-box", db, statement], shell=True)

def water():
    db = health_db
    table = "water"
    liters = input("\nLiters: ")
    insert_water = f"INSERT INTO {table} VALUES (date('now', 'localtime', '-1 day'), {liters})"
    select_water = f"SELECT * FROM {table} ORDER BY Date DESC LIMIT 5"
    sql_statement(db, insert_water)
    sql_select(db, select_water)

def yoga():
    db = health_db
    table = "yoga"
    minutes = input("\nMinutes: ")
    insert_yoga = f"INSERT INTO {table} VALUES (date('now', 'localtime'), {minutes})"
    select_yoga = f"SELECT * FROM {table} ORDER BY Date DESC LIMIT 5"
    sql_statement(db, insert_yoga)
    sql_select(db, select_yoga)

def fuel():
    db = auto_db
    table = "fuel"
    amount = input("\nAmount: ")
    ppg = input("PPG: ")
    gallons = input("Gallons: ")
    avg_mpg = input("AvgMPG: ")
    miles = input("Miles: ")
    insert_fuel = f"INSERT INTO {table} VALUES (date('now', 'localtime'), {amount}, {ppg}, {gallons}, {avg_mpg}, {miles})"
    select_fuel = f"SELECT * FROM {table} ORDER BY Date DESC LIMIT 5"
    sql_statement(db, insert_fuel)
    sql_select(db ,select_fuel)

def reading():
    db = media_db
    table = "reading"
    select_reading = f"SELECT * FROM {table}"
    sql_select(db, select_reading)

main()