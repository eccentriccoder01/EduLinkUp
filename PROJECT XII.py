def main_menu():
    ch = 'y'
    while ch == 'y':
        print("***********STUDENT REGISTRATION SYSTEM*************")
        print("1: To show databases") 
        print("2: To create a table")
        print("3: To show tables present in the database") 
        print("4: To display structure of the table")
        print("5: To add a record in the table")
        print("6: To update a record in the table") 
        print("7: To delete a record from the table") 
        print("8: To display all the records from the table")
        print("9: To sort the data in descending order of total")
        print("10: To quit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            show_database() 
        elif choice == 2:
            create_table() 
        elif choice == 3:
            showtables()
        elif choice == 4:
            display_struc() 
        elif choice == 5:
            add_rec()
        elif choice == 6:
            update_rec()
        elif choice == 7:
            delete_rec()
        elif choice == 8:
            fetch_data()
        elif choice == 9:
            topper_list()
        elif choice == 10:
            print("Exiting")
            break
        else:
            print("Wrong Input")
    ch = input("Thank You")

def show_database():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", 
        user = "root", password = "GN847DUMySQL!")
        cursor = db.cursor()
        cursor.execute("show databases")
        for x in cursor:
            print(x)
    except:
        print("Error in connection")

def create_table():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost",
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        cursor.execute("create table student1(rollno int primary key,\
        name varchar(20), stream varchar(10), total\
        int, grade varchar(3), Class int)")
        print("Table created")
    except:
        print("Error in connection")

def showtables():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost",
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        cursor.execute("show tables")
        for x in cursor:
            print(x)
    except:
        print("Error in connection")

def display_struc():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost",
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        cursor.execute("desc student1")
        for x in cursor:
            print(x)
    except:
        print("Error in connection")
def add_rec():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost",
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        rno = int(input("Enter roll number")) 
        nm = input("Enter name")
        st = input("Enter stream")
        tot = int(input("Enter total")) 
        gr = input("Enter grade")
        C = int(input ("Enter class"))
        sql_query = "insert into student1 values(%s,%s,%s,%s,%s,%s)" 
        val = (rno,nm,st,tot,gr,C)
        cursor.execute(sql_query,val) 
        db.commit() 
        print("Record added")
    except:
        db.rollback()
        print("Error, Record not added")
def update_rec():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost",
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        rno = int(input("Enter rollno")) 
        tot = int(input("Enter total"))
        sql_query = "Update student1 set total = %s where rollno = %s"
        val = (tot,rno)
        cursor.execute(sql_query,val)
        print(cursor.rowcount, "record updated")
        db.commit()
    except:
        db.rollback()
        print("Record not updated")
def delete_rec():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost",
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        rno = int(input("Enter rollno"))
        sql_query = "delete from student1 where rollno = %s"
        cursor.execute(sql_query,(rno,)) 
        print(cursor.rowcount, "record deleted")
        db.commit()
    except:
        db.rollback()
        print("Record not deleted")
def fetch_data():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", 
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student1")
        records = cursor.fetchall()
        for x in records:
            print(x[0],x[1],x[2],x[3],x[4],x[5])
    except:
        print("Error, unable to fetch data")
def topper_list():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost",
        user = "root", password = "GN847DUMySQL!", 
        database = "school")
        cursor = db.cursor()
        cursor.execute("select * from student1 order by total desc")
        records = cursor.fetchall()
        for x in records:
            print(x[0],x[1],x[2],x[3],x[4],x[5])
    except:
        print("Error, unable to sort")
main_menu()
