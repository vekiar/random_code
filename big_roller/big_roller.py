import sys
from random import randint
import sqlite3
import os
import uuid

# Setup the die
DIE_STARTING_POSITION = 1
if DIE_STARTING_POSITION > 20: sys.exit("Your die is broken")

def roll_die(sides):
    value = randint(1,sides)
    return value

def roll_to_target(target, turns):
    turn = 1
    earnt = 0
    turns_to_target = 0
    die_value = DIE_STARTING_POSITION
    die_values_list = []
    session_id = str(uuid.uuid4())
    while (die_value < target):
        if turn >= turns: break
        turn += 1
        turns_to_target += 1
        die_values_list.append(die_value)
        die_value = roll_die(20)
    while (turn <= turns):
        earnt += die_value
        die_values_list.append(die_value)
        turn += 1
    data = [(session_id, target, earnt, die_value, turns_to_target)]
    return data

if __name__ == '__main__':
    # Setup the databse
    datastore = "big_roller.db"
    connection = sqlite3.connect(datastore)
    cursor = connection.cursor()
    table = "roll_stats"
    if (cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='roll_stats'").fetchall() == []):
        cursor.execute("CREATE TABLE roll_stats(session_id, target_value, earnt, die_value, turns_to_target)")

    turns = 100
    cases = range(1,21)
    for case in cases:
        data = roll_to_target(case, turns)
        print(data)
        cursor.executemany("INSERT INTO roll_stats VALUES(?, ?, ?, ?, ?)", data)
    
    connection.commit()