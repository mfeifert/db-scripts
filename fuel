#!/usr/bin/env python3

import sys
import sqlite3
import subprocess

if len(sys.argv) < 2:
    print("Usage: fuel FILE")
    sys.exit(1)

db_path = sys.argv[1]
table = 'fuel'

def main():
    amount = input('\nPrice: ')
    ppg = input('Dollars Per Gallon: ')
    gallons = input('Gallons: ')
    avg_mpg = input('Average Miles Per Gallon: ')
    miles = input('Odometer: ')
    sql_log_entry = f"INSERT INTO {table} VALUES (date('now', 'localtime'), {amount}, {ppg}, {gallons}, {avg_mpg}, {miles})"
    sql_log_report = f"SELECT * FROM {table} ORDER BY Date DESC LIMIT 5"
    issue_sql_statement(db_path, sql_log_entry)
    print_report(db_path ,sql_log_report)

def issue_sql_statement(db, statement):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(statement)
    con.commit()
    con.close()

def print_report(db, statement):
    # SELECT statements are run via shell to produce the "-box" output format
    subprocess.run([f"sqlite3 -box {db} '{statement}'"], shell=True)

main()
