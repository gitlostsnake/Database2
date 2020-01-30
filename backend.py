import sqlite3
from datetime import datetime
import numpy as np
import pandas as pd


class Database:

    def __init__(self, dbfile):
        self.conn = sqlite3.connect(dbfile)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS road_works
                    (id INTEGER PRIMARY KEY, location TEXT,
                    client TEXT, start_date TEXT, end_date TEXT)
                    """)
        print("road_works table CONNECTED")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS stock_inventory
                    (id INTEGER PRIMARY KEY, name TEXT UNIQUE,
                    amount TEXT, weight TEXT, warning_level TEXT)
                    """)
        print("stock_inventory table CONNECTED")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS vehicles_inventory
                     (id INTEGER PRIMARY KEY, FleetNo TEXT UNIQUE,
                     RegistrationNo TEXT UNIQUE, WeightLimit TEXT)
                     """)
        print("Vehicles_inventory table CONNECTED")

        self.cur.execute("""
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
        print("assigned_stock table CONNECTED")

        self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS assigned_vehicle
                    (id INTEGER PRIMARY KEY,
                    vehicle_id INTEGER,
                    job_id INTEGER, FOREIGN KEY(vehicle_id)
                    REFERENCES vehicles_inventory(id)
                    FOREIGN KEY(job_id)
                    REFERENCES road_works(id))
                    """)
        print("assigned_vehicle table CONNECTED")

        self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS additional
                    (job_id INTEGER,
                    length INTEGER,
                    type TEXT,
                    crew_required INTEGER,
                    shift TEXT,
                    FOREIGN KEY(job_id)
                    REFERENCES road_works(id))
                    """)
        print("additional table CONNECTED")
        self.conn.commit()


    class Insert:
        """Insert job, stock or vehicle"""
        def __init__(self):
            print("Inserting ...")
            db.cur = db.conn.cursor()

        def job(location, client, start_date, end_date):
            db.cur.execute("INSERT INTO road_works VALUES (NULL, ?,?,?,?)",
                        (location, client, start_date, end_date))
            start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
            end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M")
            db.conn.commit()
            print(f"+|Roadworks created| for {client}")


        def stock(name, amount, weight, warning_level):
            db.cur.execute("INSERT INTO stock_inventory VALUES (NULL, ?,?,?,?)",
                    (name, amount, weight, warning_level))
            db.conn.commit()
            print(f"+|Stock added|{amount} {name}")

        def vehicle(fleet_no, registration_no, weight_limit):
            db.cur.execute("INSERT INTO vehicles_inventory VALUES (NULL, ?,?,?)",
                    (fleet_no, registration_no, weight_limit))
            db.conn.commit()
            print(f"+|Vehicle added|{fleet_no} in fleet")

        def additional(job_id, length, type, crew_required, shift):
            db.cur.execute("INSERT INTO additional VALUES (?,?,?,?,?)",
                        (job_id, length, type, crew_required, shift))
            db.conn.commit()
            print(f"+|Addition data|")

        def assigned(item_id, job_id, amount_taken):
            db.cur.execute("INSERT INTO assigned_stock VALUES (NULL, ?,?,?)",
                        (item_id, job_id, amount_taken))
            db.conn.commit()
            print(f"&|Assigned item| {item_id} to job {job_id}")

    class View:
        """View job, stock, vehicle"""
        def __init__():
            db.cur = db.conn.cursor()

        def job():
            db.cur.execute("SELECT * FROM road_works")
            rows = db.cur.fetchall()
            print("|Viewing Job's| ...")
            return rows

        def stock():
            db.cur.execute("SELECT * FROM stock_inventory")
            rows = db.cur.fetchall()
            print("|Viewing Stock| ...")
            return rows

        def vehicle():
            db.cur.execute("SELECT * FROM vehicles_inventory")
            rows = db.cur.fetchall()
            print("|Viewing Vehicles| ...")
            return rows

        def additional():
            db.cur.execute("SELECT * FROM additional")
            rows = db.cur.fetchall()
            print("|Viewing Additional| ...")
            return rows

        def assigned():
            db.cur.execute("SELECT * FROM assigned_stock")
            rows = db.cur.fetchall()
            print("|Viewing Assigned stock| ...")
            return rows


    class Search(object):
        """Search table for Roadworks currently works with location"""
        def __init__():
            db.cur = db.conn.cursor()

        def job(location="", client="", start_date="", end_date=""):
            db.cur.execute("""SELECT * FROM road_works WHERE location=?
                            OR client=? OR start_date=? OR end_date=?""",
            (location, client, start_date, end_date))
            rows = db.cur.fetchall()
            return rows

        def job_id(id=""):
            db.cur.execute("SELECT * FROM road_works WHERE id=?", (id))
            rows = db.cur.fetchall()
            return rows

        def stock(id=""):
            db.cur.execute("SELECT * FROM stock_inventory WHERE id=?",(id,))
            rows = db.cur.fetchall()
            return rows

        def assigned(job_id=""):
            db.cur.execute("SELECT item_id FROM assigned_stock WHERE job_id=?", (job_id,))
            rows = db.cur.fetchall()
            return rows

        def assigned_kitlist(job_id=""):
            db.cur.execute("""SELECT * FROM assigned_stock
                        INNER JOIN stock_inventory ON assigned_stock.item_id = stock_inventory.id
                        WHERE job_id=?""",(job_id,))
            rows = db.cur.fetchall()
            return rows

        def assigned_joinitem(item_id=""):
            db.cur.execute("""SELECT * FROM assigned_stock
                        INNER JOIN stock_inventory ON assigned_stock.item_id = stock_inventory.id
                        WHERE item_id=?""",(item_id,))
            rows = db.cur.fetchall()
            return rows

        def assigned_taken(item_id=""):
            db.cur.execute("SELECT amount_taken FROM assigned_stock WHERE item_id=?",(item_id,))
            rows = db.cur.fetchall()
            return rows

        @staticmethod
        def additional(job_id):
            conn = sqlite3.connect("road_works.db")
            cur = conn.cursor()
            cur.execute("SELECT ")


    class Delete(object):
        """Delete job, stock, vehicle in original database tables"""
        def __init__():
            db.cur = db.conn.cursor()

        def job(id):
            db.cur.execute("DELETE FROM road_works WHERE id=?", (id,))
            db.conn.commit()
            print("-|Deleting job|")


        def stock(id):
            db.cur.execute("DELETE FROM stock_inventory WHERE id=?", (id,))
            db.conn.commit()
            print("-|Deleting stock|")
        def vehicle(id):
            db.cur.execute("DELETE FROM vehicles_inventory WHERE id=?", (id,))
            db.conn.commit()
            print("-|Deleting vehicle|")
        def assigned(job_id=""):
            db.cur.execute("DELETE FROM assigned_stock WHERE job_id=?", (job_id,))
            db.conn.commit()
            print("-|Deleting assigned stock|")

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

    def __del__(self):
        self.conn.close()


db = Database('road_works.db')
# assigned_connect()
