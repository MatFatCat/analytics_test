import pandas as pd

milk_history = pd.read_csv("/Users/nikolamuravev/Desktop/analytics_test/test/milk_story_db.csv", encoding="cp1252",
                           on_bad_lines="skip")
milk_history.reset_index(drop=True)

list_of_date_exist = 0
date = []
sales_number = []
counter = 0


def row_handler(row, date, sales_number):
    date_row = row["created_at"].split(" ")[0]
    global list_of_date_exist

    if list_of_date_exist == 0:
        date.append(date_row)
        sales_number.append(1)
        list_of_date_exist += 1
    else:
        date_exist = 0
        for i in date:
            if date_row == i:
                sales_number[date.index(date_row)] += 1
                date_exist = 1
        if date_exist == 0:
            date.append(date_row)
            sales_number.append(1)


milk_history.apply(lambda row: row_handler(row, date, sales_number), axis=1)

data = {'Date': date, 'Number of sales': sales_number}
df = pd.DataFrame(data)
df.to_csv("/Users/nikolamuravev/Desktop/date-sales_number.csv")