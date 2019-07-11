#!/usr/bin/python3

import sqlite3

conn=sqlite3.connect("hello.db")
if conn:
    # conn.execute(""" create table Contact2 (
    #     contact_id int primary key not null,
    #     contact_name varchar,
    #     contact_number varchar
    #     ) """)

    conn.execute(""" insert into Contact2 (
        contact_id, contact_name, contact_number
        ) values (
           0,  "Michael", "01234556"
        ) """)

    # print("Table created successfully")
    print("Code inserted")
    conn.commit()


conn.close()


input()
