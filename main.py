# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time

import jinja2
from flask import Flask, g
import mysql.connector

app = Flask(__name__)

counter = 0

def get_db():
    if not hasattr(g, "db"):
        g.db = mysql.connector.connect(user="root",
                                       database="shopper",
                                       host="db")
    return g.db

@app.route('/')
def hello():
    global counter
    counter += 1
    return f"Hello World, Its a big old place, ain't it {counter}"

@app.route('/orders')
def orders():
    last_order_time = time.time()
    return f"Last Order was at {last_order_time}"

@app.route('/customers')
def customers():
    sql = "select * from customers"
    template = """<html>
    <head/>
    <body>
        <table border="1">
        <thead>
            <tr>
                <th>Id</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
                <tr>
                    <td>{{ row[0] }}</td>
                    <td>{{ row[1] }}</td>
                    <td>{{ row[2] }}</td>
                    <td>{{ row[3] }}</td>
                </tr>
        {% endfor %}
        </tbody>
        </table>
        
    </body>
    </html>"""

    db = get_db()
    cur = db.cursor()
    cur.execute(sql)
    data = [r for r in cur]

    return jinja2.Template(template).render(data=data)
