from flask import Flask, render_template, redirect, url_for, request, g 
import sqlite3


app = Flask(__name__)
app.database = "toplist.db"



@app.route('/')
def home():
   
    return render_template('index.html')


@app.route('/result')
def result():
    g.db = connect_db()
    cur = g.db.execute('select * from listing')
    listing = [dict(Year=row[0], Week=row[1], Artist=row[2], Title=row[3], SpotUrl=row[4], SpotID=row[5], Image=row[6]) for row in cur.fetchall()]
  
    g.db.close()
    return render_template('result.html', listing=listing)


def connect_db():
	return sqlite3.connect(app.database)






if __name__ == '__main__':
    app.run(debug=True)


