import psycopg2
import time

try:
    conn = psycopg2.connect(
        dbname='v2_project_sand',
        user='ph_psql',
        password='chckchn02-',
        host='93.125.21.202',
        port='10032'
    )
    cursor = conn.cursor()
    query = f"SELECT * FROM v2_project_sand.public.labels WHERE labels.group = 'milk' LIMIT 100000"
    print("Start process ...")
    time1 = time.time()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result, type(result), len(result))
    time2 = time.time()
    print(time2-time1)

except Exception as arr:
    print(arr)

