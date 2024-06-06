from flask import Flask, render_template, request
import psycopg2
import datetime
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

app = Flask(__name__)

#PostgreSQL資料庫連接
host="dpg-cpfvnd8l5elc738k8cag-a.singapore-postgres.render.com"
database="jpy_currency"
port="5432"
user="admin"
password="vh5Q3XyoCHkDtcWbcohVssrbKizXbapN"

conn = psycopg2.connect(host=host, user=user, password=password, database=database)
print('Opened database successfully')


@app.route('/one')
def one():
    todaydate = datetime.date.today()
    cur = conn.cursor()
    sql = "SELECT * FROM yen WHERE date = %s"
    try:
        cur.execute(sql, (todaydate,))
        rows = cur.fetchall()  # 使用 fetchall 
    except psycopg2.DatabaseError as e:
        print(f"Error: {e}")
        rows = []

    return render_template('index.html', rows=rows)

@app.route('/two')
def two():
    cur = conn.cursor()
    sql = "SELECT * FROM `yen` ORDER BY date DESC LIMIT 7"
    try:
        cur.execute(sql)
        rows = cur.fetchall()  # 使用 fetchall 
    except psycopg2.DatabaseError as e:
        print(f"Error: {e}")
        rows = []
        
    img = BytesIO()
    x = [i[1] for i in rows]
    x.reverse()
    y = [i[5] for i in rows]
    y.reverse()
    
    #plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.figure(figsize=(12,6))
    
    plt.plot(x, y, marker= "o")
    plt.title('Sight_Sale')
    plt.ylabel("Exchange Rate")
    plt.savefig(img, format='png')
    img.seek(0)
    img = base64.b64encode(img.getvalue()).decode()

    return render_template('index1.html', rows=rows, img=img)
    

@app.route('/three')
def three():
    cur = conn.cursor()
    sql = "SELECT * FROM yen ORDER BY date DESC LIMIT 90"
    try:
        cur.execute(sql)
        rows = cur.fetchall()  # 使用 fetchall 
    except psycopg2.DatabaseError as e:
        print(f"Error: {e}")
        rows = []
        
    img = BytesIO()
    x = [i[1] for i in rows]
    x.reverse()
    y = [i[5] for i in rows]
    y.reverse()
    
    #plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.figure(figsize=(12,9))
    
    plt.plot(x, y, marker= "o")
    plt.xticks(rotation=270)
    plt.title('Sight_Sale')
    plt.ylabel("Exchange Rate")
    plt.savefig(img, format='png')
    img.seek(0)
    img = base64.b64encode(img.getvalue()).decode()

    return render_template('index1.html', rows=rows, img=img)

@app.route('/four')
def four():
   cur = conn.cursor()
   sql = "SELECT * FROM yen ORDER BY date DESC LIMIT 180"
   try:
       cur.execute(sql)
       rows = cur.fetchall()  # 使用 fetchall 
   except psycopg2.DatabaseError as e:
       print(f"Error: {e}")
       rows = []
    
   img = BytesIO()
   x = [i[1] for i in rows]
   x.reverse()
   y = [i[5] for i in rows]
   y.reverse()
   
   #plt.rcParams['font.sans-serif'] = 'SimHei'
   plt.figure(figsize=(12,9))
   
   plt.plot(x, y, marker= "o")
   plt.xticks(rotation=270)
   plt.title('Sight_Sale')
   plt.ylabel("Exchange Rate")
   plt.savefig(img, format='png')
   img.seek(0)
   img = base64.b64encode(img.getvalue()).decode() 
       

   return render_template('index1.html', rows=rows, img=img)

if __name__ == '__main__':
    app.run(debug=True)

    
    


