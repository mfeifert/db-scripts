import sqlite3
import subprocess
import platform

if platform.system() == 'Linux':
    path = '/home/maf/docs/db/'
else:
    path = '/Users/maf/docs/db/'

# change the string part of value of this variable to "test.db" for testing
media_db = path + 'media.db'

# 'table name': 'show title'
shows = {
    'tos': 'Star Trek: The Original Series',
    'tas': 'Star Trek: The Animated Series',
    'tng': 'Star Trek: The Next Generation',
    'ds9': 'Star Trek: Deep Space Nine',
    'stv': 'Star Trek: Voyager',
    'ste': 'Star Trek: Enterprise',
    'babylon5': 'Babylon 5',
    'cosmos': 'Cosmos',
    'connections': 'Connections',
    'growingup': 'Growing Up in the Universe',
    'xfiles': 'The X-Files',
    'twilightzone': 'The Twilight Zone',
    'ft': 'Fawlty Towers',
    'mk': 'Master Keaton',
    'monster': 'Monster',
    'lotgh': 'Legend of the Galactic Heroes',
    'rolw': 'Record of Lodoss War'
}

def main():
    index = 1
    print()
    for i in list(shows.items()):
       print(f'{index}. {i[1]}')
       index += 1
    print()
    selection = int(input()) - 1
    print_menu_for_selected_show(list(shows.items())[selection][0])

def issue_sql_statement(db, statement):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(statement)
    con.commit()
    con.close()

def print_report(db, statement):
    # SELECT statements are run via shell to produce the "-box" output format
    subprocess.run([f"sqlite3 -box {db} '{statement}'"], shell=True)

def print_menu_for_selected_show(table):
    db = media_db
    menu = [
    '',
    '1. List episodes',
    '2. Next episode',
    '3. Random episode',
    '4. Mark episode as watched',
    'q. Quit'
    ]
    if table == 'xfiles':
        menu.append('m. List mythology arc')
    for i in menu:
        print(i)
    sql_all_episodes = f"SELECT * from {table}"
    sql_next_episode = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY NumOverall LIMIT 1"
    sql_random_episode = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY random() LIMIT 1"
    sql_mytharc_episodes = f"SELECT * FROM {table} WHERE Mytharc IS NOT NULL"

    while True:
        choice = input(f'\n{shows[table]}> ')
        if choice == '1':
            print()
            print_report(db, sql_all_episodes)
        elif choice == '2':
            print()
            print_report(db, sql_next_episode)
        elif choice == '3':
            print()
            print_report(db, sql_random_episode)
        elif choice == '4':
            episode = int(input('\nEpisode: '))
            update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
            issue_sql_statement(db, update_episode)
        elif choice == 'q':
            print()
            break
        elif choice == 'm':
            print_report(db, sql_mytharc_episodes)

main()
