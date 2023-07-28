import sqlite3
import subprocess
import platform

if platform.system() == 'Linux':
    path = '/home/maf/docs/db/'
else:
    path = '/Users/maf/docs/db/'

# change the string part of value of this variable to "test.db" for testing
media_db = path + "media.db"

shows = {
    'tos': 'Star Trek: The Original Series',
    'tas': 'Star Trek: The Animated Series',
    'tng': 'Star Trek: The Next Generation',
    'cosmos': 'Cosmos',
    'connections': 'Connections',
    'growingup': 'Growing Up in the Universe',
    'mk': 'Master Keaton',
    'xfiles': 'The X-Files',
    'twilightzone': 'The Twilight Zone'
}

def main():
    index = 1
    for i in list(shows.items()):
       print(f'{index}: {i[1]}')
       index += 1



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

def show(table):
    db = media_db
    menu = [
    "",
    "1: List episodes",
    "2: Next episode",
    "3: Random episode",
    "4: Mark episode as watched"
    ]
    if table == "xfiles":
        menu.append("m: List mythology arc")
    for i in menu:
        print(i)
    choice = input("\n")
    select_all = f"SELECT * from {table}"
    select_next = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY NumOverall LIMIT 1"
    select_random = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY random() LIMIT 1"
    select_mytharc = f"SELECT * FROM {table} WHERE Mytharc IS NOT NULL"
    if choice == "1":
        print("")
        sql_select(db, select_all)
        print("")
    elif choice == "2":
        print("")
        sql_select(db, select_next)
        print("")
    elif choice == "3":
        print("")
        sql_select(db, select_random)
        print("")
    elif choice == "4":
        episode = int(input("\nEpisode: "))
        update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
        sql_statement(db, update_episode)
        print("")
    elif choice == "m":
        sql_select(db, select_mytharc)

main()




def oldmain():
    menu = [
    "",
    "1: Star Trek: The Original Series",
    "2: Star Trek: The Animated Series",
    "3: Star Trek: The Next Generation",
    "4: Master Keaton",
    "5: The X-Files",
    "6: Cosmos",
    "7: Connections",
    "8: Growing Up in the Universe",
    "9: The Twilight Zone"
    ]
    for i in menu:
        print(i)
    choice = input("\n")
    if choice == "1":
        show("tos")
    elif choice == "2":
        show("tas")
    elif choice == "3":
        show("tng")
    elif choice == "4":
        show("mk")
    elif choice == "5":
        show("xfiles")
    elif choice == "6":
        show("cosmos")
    elif choice == "7":
        show("connections")
    elif choice == "8":
        show("growingup")
    elif choice == "9":
        show("twilightzone")