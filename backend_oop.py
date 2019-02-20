import sqlite3
from datetime import datetime

class Connect():

    def __init__(self):
        conn = sqlite3.connect("road_works.db")
        cur = conn.cursor()

    def job(self):
        cur.execute("""CREATE TABLE IF NOT EXISTS road_works
                    (id INTEGER PRIMARY KEY, location TEXT,
                    client TEXT, start_date TEXT, end_date TEXT)
                    """)
        conn.commit()
        conn.close()

    def stock(self):
        cur.commit("""CREATE TABLE IF NOT EXISTS stock_inventory
                    (id INTEGER PRIMARY KEY, name TEXT UNIQUE,
                    amount TEXT, weight TEXT, warning_level TEXT)
                    """)
        conn.commit()
        conn.close()

    def vehicle(self):
        cur.execute("""CREATE TABLE IF NOT EXISTS vehicles_inventory
                     (id INTEGER PRIMARY KEY, FleetNo TEXT UNIQUE,
                     RegistrationNo TEXT UNIQUE, WeightLimit TEXT)
                     """)
        conn.commit()
        conn.close()

    def assign_stock(self):
        cur.execute("""CREATE TABLE IF NOT EXISTS assigned_stock
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

    def assign_vehicle(self):
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS assigned_vehicle
                    (id INTEGER PRIMARY KEY,
                    vehicle_id INTEGER,
                    job_id INTEGER, FOREIGN KEY(vehicle_id)
                    REFERENCES vehicles_inventory(id)
                    FOREIGN KEY(job_id)
                    REFERENCES road_works(id))
                    """)
        conn.commit()
        conn.close()

    def additional(self):
        cur.execute("""CREATE TABLE IF NOT EXISTS additional
                    (job_id INTEGER,
                    length INTEGER,
                    type TEXT,
                    crew_required INTEGER,
                    FOREIGN KEY(job_id)
                    REFERENCES road_works(id))
                    """)
        conn.commit()
        conn.close()


class Insert(Connect):
