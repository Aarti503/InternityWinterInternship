import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.conn = connector.connect(host='localhost',
                            port='3306',
                            user='root',
                            password='root',
                            database='pythontest', 
                            auth_plugin='mysql_native_password')
        query='create table if not exists user(userID int primary key, username varchar(200), phone varchar(12))'
        cur = self.conn.cursor()
        cur.execute(query)
        print("Table Created")

    #insert method
    def insert_user(self,userID,username,phone):
        query = "insert into user(userID,username,phone) values({},'{}','{}')".format(userID,username,phone)
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Data Added to user Table")

    #fetching data from table method
    def fetch_userData(self):
        query = "select * from user"
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print("UserID: ",row[0])
            print("UserName:",row[1])
            print("Phone Number:",row[2],"\n\n")

     #fetching data from table method by ID
    def fetch_userDataBYID(self):
        query = "select * from user where userID=1"
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print("UserID: ",row[0])
            print("UserName:",row[1])
            print("Phone Number:",row[2],"\n\n")

    # Delete data from user
    def delete_data(self,userID):
        query="delete from user where userID={}".format(userID)
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Data Deleteed with userID =",userID)
        for row in cur:
            print("UserID: ",row[0])
            print("UserName:",row[1])
            print("Phone Number:",row[2],"\n\n")

    #update data 
    def update_data(self,userID,newname,newphone):
        query="update user set username='{}',phone='{}'where userID={}".format(newname,newphone,userID)
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Data updated")
    
