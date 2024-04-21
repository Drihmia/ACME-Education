#!/usr/bin/python3
"""Define the Lessons API"""
from api.v1.views import app_views
import json
import MySQLdb as db


@app_views.route("/lessons", methods=["GET"], strict_slashes=False)
@app_views.route("/lessons/<id>", methods=["GET"], strict_slashes=False)
def all(id=None):
    userName = "mohamed_remote"
    password = "mohamed_remote"
    dbName = "ACME"
    conn = db.connect(host="34.207.120.158", port=3306, user=userName,
                      passwd=password, db=dbName)
    curs = conn.cursor()
    if id:
        stat = "select * from ACME.lessons where id={}".format(id)
    else:
        stat = "select * from ACME.lessons"
    curs.execute(stat)
    result = curs.fetchall()
    lessList = []
    for elem in result:
        temp = {
                "id": elem[0],
                "name": elem[1],
                "download_link": elem[2],
                "teacher_id": elem[3],
                "institution_id": elem[4],
                "subject_id": elem[5],
                "created_at": elem[6],
                "updated_at": elem[7]
               }
        lessList.append(temp)
    conn.close()
    data = json.dumps(lessList, indent=2, default=str) + "\n"
    return (data, 200)
