#!/usr/bin/env python3

import sys
import sqlite3
import subprocess

if len(sys.argv) < 2:
    print("Usage: nutrition FILE")
    sys.exit(1)

db_path = sys.argv[1]
food_log_table = "food_log"
foods_table = "foods"


def main():
    # print_nutrition_report(today)
    # insert_log_entry()
    # print_nutrition_report(selection)
    insert_new_food()


def print_nutrition_report(date):
    print_nutrition_stats(date)
    print_log_entries(date)


def insert_log_entry():
    return


def insert_new_food():
    new_food = []
    new_food.append(input("Food name: "))
    new_food.append(input("Serving Size: "))
    new_food.append(input("Serving Units: "))
    new_food.append(input("Calories: "))
    new_food.append(input("Total Fat: "))
    new_food.append(input("Saturated Fat: "))
    new_food.append(input("Trans Fat: "))
    new_food.append(input("Polyunsaturated Fat: "))
    new_food.append(input("Monounsaturated Fat: "))
    new_food.append(input("Cholesterol: "))
    new_food.append(input("Sodium: "))
    new_food.append(input("Carbohydrates: "))
    new_food.append(input("Dietary Fiber: "))
    new_food.append(input("Total Sugars: "))
    new_food.append(input("Added Sugars: "))
    new_food.append(input("Protein: "))
    new_food.append(input("Vitamin D: "))
    new_food.append(input("Calcium: "))
    new_food.append(input("Iron: "))
    new_food.append(input("Potassium: "))

    print(new_food)

    sql_new_food = f"""INSERT INTO {foods_table}(DateAdded, Name,
    ServingSize, ServingUnit, Calories, TotalFat, SaturatedFat, TransFat,
    PolyunsaturatedFat, MonounsaturatedFat, Cholesterol, Sodium,
    Carbohydrates, DietaryFiber, TotalSugars, AddedSugars, Protein,
    VitaminD, Calcium, Iron, Potassium)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    for item in new_food:
        cur.execute(sql_new_food, item)

    con.commit()
    con.close()

    # name = input("Food name: ")
    # serving_size = input("Serving Size: ")
    # serving_unit = input("Serving Units: ")
    # calories = input("Calories: ")
    # total_fat = input("Total Fat: ")
    # saturated_fat = input("Saturated Fat: ")
    # trans_fat = input("Trans Fat: ")
    # poly_fat = input("Polyunsaturated Fat: ")
    # mono_fat = input("Monounsaturated Fat: ")
    # cholesterol = input("Cholesterol: ")
    # sodium = input("Sodium: ")
    # carbohydrates = input("Carbohydrates: ")
    # dietary_fiber = input("Dietary Fiber: ")
    # total_sugars = input("Total Sugars: ")
    # added_sugars = input("Added Sugars: ")
    # protein = input("Protein: ")
    # vitamin_d = input("Vitamin D: ")
    # calcium = input("Calcium: ")
    # iron = input("Iron: ")
    # potassium = input("Potassium: ")

    # sql_new_food = f'''INSERT INTO {foods_table}(DateAdded, Name,
    # ServingSize, ServingUnit, Calories, TotalFat, SaturatedFat,
    # TransFat, PolyunsaturatedFat, MonounsaturatedFat, Cholesterol,
    # Sodium, Carbohydrates, DietaryFiber, TotalSugars, AddedSugars,
    # Protein, VitaminD, Calcium, Iron, Potassium)
    # VALUES(date('now', 'localtime'), {name}, {serving_size},
    # {serving_unit}, {calories}, {total_fat}, {saturated_fat},
    # {trans_fat}, {poly_fat}, {mono_fat}, {cholesterol}, {sodium},
    # {carbohydrates}, {dietary_fiber}, {total_sugars}, {added_sugars},
    # {protein}, {vitamin_d}, {calcium}, {iron}, {potassium})'''

    # issue_sql_statement(db_path, sql_new_food)


def print_nutrition_stats(date):
    return


def print_log_entries(date):
    print_report()
    return


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
