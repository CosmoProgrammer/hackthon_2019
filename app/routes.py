from app import app
import mysql.connector
from mysql.connector import Error

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Hi")
def hello1():
    return "Hello Anirudh"

@app.route("/login", method=["GET","POST"])
def login():
    connection = mysql.connector.connect(
        host="127.0.0.0",
        database='wizlearn',
        user='root',
        password='pokemon2345'
    )
    error = None
    if request.method == 'POST':
        app.logger.debug("Inside login POST")
        username = request.form['username']
        category = request.form['category']
        password = request.form['password']
    #return redirect(url_for('home'))
    #return render_template('loginpage.html', error=error)

@app.route("/TestDBConnection")
def testDB():
    try:
        connection = mysql.connector.connect(host='127.0.0.1',database='school_py',user='root',password='pokemon2345')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ",db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print ("Your connected to - ", record)
    except Exception as e:
        print ("Error while connecting to MySQL", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed") 


