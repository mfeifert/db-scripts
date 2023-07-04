import sqlite3
import subprocess

# change the value of these global variables to "test.db" for testing
health_db = "~/docs/db/health.db"
auto_db = "~/docs/db/auto.db"
media_db = "~/docs/db/media.db"

def main():
    menu = [
    "",
    "1: Water",
    "2: Yoga",
    "3: Fuel",
    "4: Star Trek: The Original Series",
    "5: Star Trek: The Animated Series",
    "6: Star Trek: The Next Generation",
    "7: Master Keaton",
    "8: Reading"
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
        tos()
    elif choice == "5":
        tas()
    elif choice == "6":
        tng()
    elif choice == "7":
        mk()
    elif choice == "8":
        reading()

def sql_statement(db, statement):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(statement)
    con.commit()
    con.close()

def sql_select(db, statement):
    # SELECT statements are run via shell to produce the desired output format
    subprocess.run([f"sqlite3 -box {db} '{statement}'"], shell=True)
    # subprocess.run(["sqlite3", "-box", db, statement], shell=True)

def water():
    db = health_db
    table = "water"
    liters = input("\nLiters: ")
    insert_water = f"INSERT INTO {table} VALUES (date('now', 'localtime', '-1 day'), {liters})"
    sql_statement(db, insert_water)
    select_water = f"SELECT * FROM {table} ORDER BY Date DESC LIMIT 5"
    sql_select(db, select_water)

def yoga():
    db = health_db
    table = "yoga"
    minutes = input("\nMinutes: ")
    insert_yoga = f"INSERT INTO {table} VALUES (date('now', 'localtime'), {minutes})"
    sql_statement(db, insert_yoga)
    select_yoga = f"SELECT * FROM {table} ORDER BY Date DESC LIMIT 5"
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
    sql_statement(db, insert_fuel)
    select_fuel = f"SELECT * FROM {table} ORDER BY Date DESC LIMIT 5"
    sql_select(db ,select_fuel)

def tos():
    # Star Trek: The Original Series
    db = media_db
    table = "tos"
    menu = [
    "",
    "1: List episodes",
    "2: Random episode",
    "3: Mark episode as watched"
    ]
    for i in menu:
        print(i)
    choice = input("\n")
    if choice == "1":
        select_all = f"SELECT * from {table}"
        sql_select(db, select_all)
    elif choice == "2":
        select_random = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY random() LIMIT 1"
        sql_select(db, select_random)
    elif choice == "3":
        episode = input("\nEpisode: ")
        update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
        sql_statement(db, update_episode)

def tas():
    # Star Trek: The Animated Series
    db = media_db
    table = "tas"
    menu = [
    "",
    "1: List episodes",
    "2: Next episode",
    "3: Mark episode as watched"
    ]
    for i in menu:
        print(i)
    choice = input("\n")
    if choice == "1":
        select_all = f"SELECT * from {table}"
        sql_select(db, select_all)
    elif choice == "2":
        select_next = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY NumOverall LIMIT 1"
        sql_select(db, select_next)
    elif choice == "3":
        episode = input("\nEpisode: ")
        update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
        sql_statement(db, update_episode)

def tng():
    # Star Trek: The Next Generation
    db = media_db
    table = "tng"
    menu = [
    "",
    "1: List episodes",
    "2: Random episode",
    "3: Mark episode as watched"
    ]
    for i in menu:
        print(i)
    choice = input("\n")
    if choice == "1":
        select_all = f"SELECT * from {table}"
        sql_select(db, select_all)
    elif choice == "2":
        select_random = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY random() LIMIT 1"
        sql_select(db, select_random)
    elif choice == "3":
        episode = input("\nEpisode: ")
        update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
        sql_statement(db, update_episode)

def mk():
    # Master Keaton
    db = media_db
    table = "mk"
    menu = [
    "",
    "1: List episodes",
    "2: Next episode",
    "3: Mark episode as watched"
    ]
    for i in menu:
        print(i)
    choice = input("\n")
    if choice == "1":
        select_all = f"SELECT * from {table}"
        sql_select(db, select_all)
    elif choice == "2":
        select_next = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY NumOverall LIMIT 1"
        sql_select(db, select_next)
    elif choice == "3":
        episode = input("\nEpisode: ")
        update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
        sql_statement(db, update_episode)

def reading():
    db = media_db
    table = "reading"
    select_reading = f"SELECT * FROM {table}"
    sql_select(db, select_reading)

main()