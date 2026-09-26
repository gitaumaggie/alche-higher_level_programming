#!/usr/bin/python3
"""Display states whose names match the user-provided argument."""

import sys
import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query.format(sys.argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()
