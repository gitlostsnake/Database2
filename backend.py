import sqlite3
from datetime import datetime
import numpy as np
import pandas as pd


"""Trying to add in OOP"""


class Connect(object):
    """Connect to job, stock, vehicle and assigned stock tables"""

    @staticmethod
    def job():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS road_works
                    (id INTEGER PRIMARY KEY, location TEXT,
                    client TEXT, start_date TEXT, end_date TEXT)
                    """)
        conn.commit()
        conn.close()

    @staticmethod
    def stock():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS stock_inventory
                    (id INTEGER PRIMARY KEY, name TEXT UNIQUE,
                    amount TEXT, weight TEXT, warning_level TEXT)
                    """)
        conn.commit()
        conn.close()

    @staticmethod
    def vehicle():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS vehicles_inventory
                     (id INTEGER PRIMARY KEY, FleetNo TEXT UNIQUE,
                     RegistrationNo TEXT UNIQUE, WeightLimit TEXT)
                     """)
        conn.commit()
        conn.close()

    @staticmethod
    def assigned_stock():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS assigned_stock
                    (id INTEGER PRIMARY KEY,
                    item_id INTEGER,
                    job_id INTEGER,
                    amount_taken TEXT,
                    FOREIGN KEY(item_id)
                    REFERENCES stock_inventory(id),
                    FOREIGN KEY(job_id)
                    REFERENCES road_works(id))
                    """)
        conn.commit()
        conn.close()

    @staticmethod
    def assigned_vehicle():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS assigned_vehicle
                    (id INTEGER PRIMARY KEY,
                    vehicle_id INTEGER,
                    job_id INTEGER, FOREIGN KEY(vehicle_id)
                    REFERENCES vehicles_inventory(id)
                    FOREIGN KEY(job_id)
                    REFERENCES road_works(id))
                    """)

    @staticmethod
    def additional():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS additional
                    (job_id INTEGER,
                    length INTEGER,
                    type TEXT,
                    crew_required INTEGER,
                    FOREIGN KEY(job_id)
                    REFERENCES road_works(id))
                    """)
        conn.commit()
        conn.close()


class Insert(object):
    """Insert job, stock or vehicle"""
    @staticmethod
    def job(location, client, start_date, end_date):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO road_works VALUES (NULL, ?,?,?,?)",
                    (location, client, start_date, end_date))
        start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
        end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M")
        conn.commit()
        conn.close()

    @staticmethod
    def stock(name, amount, weight, warning_level):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO stock_inventory VALUES (NULL, ?,?,?,?)",
                (name, amount, weight, warning_level))
        conn.commit()
        conn.close()

    @staticmethod
    def vehicle(fleet_no, registration_no, weight_limit):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO vehicles_inventory VALUES (NULL, ?,?,?)",
                (fleet_no, registration_no, weight_limit))
        conn.commit()
        conn.close()

    @staticmethod
    def additional(job_id, length, type, crew_required):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO additional VALUES (?,?,?)",
                    (job_id, length, type, crew_required))
        conn.commit()
        conn.close()

    @staticmethod
    def assigned(item_id, job_id, amount_taken):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO assigned_stock VALUES (NULL, ?,?,?)",
                    (item_id, job_id, amount_taken))
        conn.commit()
        conn.close()
        #


class View(object):
    """View job, stock, vehicle"""

    @staticmethod
    def job():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM road_works")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def stock():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM stock_inventory")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def vehicle():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM vehicles_inventory")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def additional(job_id):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM additional where job_id=?", (job_id,))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def assigned():
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM assigned_stock")
        rows = cur.fetchall()
        conn.close()
        return rows


class Search(object):
    """Search table for Roadworks currently works with location"""

    @staticmethod
    def job(location="", client="", start_date="", end_date=""):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""SELECT * FROM road_works WHERE location=?
                        OR client=? OR start_date=? OR end_date=?""",
        (location, client, start_date, end_date))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def stock(id=""):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM stock_inventory WHERE id=?",(id,))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def assigned(job_id=""):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT item_id FROM assigned_stock WHERE job_id=?", (job_id,))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def assigned_test(item_id=""):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""SELECT * FROM assigned_stock
                    INNER JOIN stock_inventory ON assigned_stock.item_id = stock_inventory.id
                    WHERE item_id=?""",(item_id,))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def assigned_taken(item_id=""):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("SELECT amount_taken FROM assigned_stock WHERE item_id=?",(item_id,))
        rows = cur.fetchall()
        conn.close()
        return rows


class Delete(object):
    """Delete job, stock, vehicle in original database tables"""
    @staticmethod
    def job(id):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM road_works WHERE id=?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def stock(id):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM stock_inventory WHERE id=?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def vehicle(id):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM vehicles_inventory WHERE id=?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def assigned(job_id=""):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM assigned_stock WHERE job_id=?", (job_id,))
        conn.commit()
        conn.close()


class Update(object):

    """Update job, stock, vehicle rows in their respective data tables"""
    @staticmethod
    def job(id, location, client, start_date, end_date):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""UPDATE road_works SET location=?, client=?,
                  start_date=?, end_date=? WHERE id=?""",
                    (location, client, start_date, end_date, id))
        conn.commit()
        conn.close()

    @staticmethod
    def stock(id, name, amount, weight, warning_level):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()
        cur.execute("""UPDATE stock_inventory SET name=?,
                    amount=?, weight=?, warning_level=? WHERE id=?""",
                    (name, amount, weight, warning_level, id))
        conn.commit()
        conn.close()



"""\\\\\\\\\\\\\\\\\\\\\\\\OLD CODE BELOW\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""


# create road_works table and interact
def job_connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS road_works
                (id INTEGER PRIMARY KEY, location TEXT,
                client TEXT, start_date TEXT, end_date TEXT)
                """)
    conn.commit()
    conn.close()


def job_insert(location, client, start_date, end_date):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO road_works VALUES (NULL, ?,?,?,?)",
                (location, client, start_date, end_date))
    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
    end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M")
    conn.commit()
    conn.close()


def job_view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM road_works")
    rows = cur.fetchall()
    conn.close()
    return rows


def job_search(location="", client="", start_date="", end_date=""):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM road_works WHERE location=?
                OR client=? OR start_date=? OR end_date=?""",
                (location, client, start_date, end_date))
    rows = cur.fetchall()
    conn.close()
    return rows


def job_delete(id):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM road_works WHERE id=?", (id,))
    conn.commit()
    conn.close()


def job_update(id, location, client, start_date, end_date):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""UPDATE road_works SET location=?, client=?,
                start_date=?, end_date=? WHERE id=?""",
                (location, client, start_date, end_date, id))
    conn.commit()
    conn.close()


# job_connect()


# Create Inventory Table and interact
def stock_connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS stock_inventory
                (id INTEGER PRIMARY KEY, name TEXT,
                amount TEXT, weight TEXT, warning_level TEXT)
                """)
    conn.commit()
    conn.close()


def stock_insert(name, amount, weight, warning_level):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO stock_inventory VALUES (NULL, ?,?,?,?)",
                (name, amount, weight, warning_level))
    conn.commit()
    conn.close()


def stock_view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM stock_inventory")
    rows = cur.fetchall()
    conn.close()
    return rows


def stock_delete(id):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM stock_inventory WHERE id=?", (id,))
    conn.commit()
    conn.close()


def stock_update(id, name, amount, weight, warning_level):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""UPDATE stock_inventory SET name=?,
                amount =?, weight =?, warning_level=? WHERE id=?""",
                (name, amount, weight, warning_level, id))
    conn.commit()
    conn.close()


# stock_connect()

# Create Vehicles table and interact


def vehicle_connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS vehicles_inventory
                (id INTEGER PRIMARY KEY, FleetNo TEXT,
                RegistrationNo TEXT, WeightLimit TEXT)
                """)
    conn.commit()
    conn.close()


def vehicle_insert(fleet_no, registration_no, weight_limit):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO vehicles_inventory VALUES (NULL, ?,?,?)",
                (fleet_no, registration_no, weight_limit))
    conn.commit()
    conn.close()


def vehicle_view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicles_inventory")
    rows = cur.fetchall()
    conn.close()
    return rows


def vehicle_delete(id):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM vehicles_inventory WHERE id=?", (id,))
    conn.commit()
    conn.close()


# vehicle_connect()


def assigned_connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS assigned_to
                (id INTEGER PRIMARY KEY,
                item_id INTEGER,
                job_id INTEGER, FOREIGN KEY(item_id)
                REFERENCES stock_inventory(id),
                FOREIGN KEY(job_id)
                REFERENCES road_works(id))
                """)
    conn.commit()
    conn.close()


def assigned_insert(item_id, job_id):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO assigned_to VALUES (NULL, ?,?)",
                (item_id, job_id))
    conn.commit()
    conn.close()


def assigned_view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM assigned_to")
    rows = cur.fetchall()
    conn.close()
    return rows


# assigned_connect()
Connect.job()
Connect.stock()
Connect.vehicle()
Connect.assigned_stock()
Connect.additional()
