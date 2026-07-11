import mysql.connector
import os

class Db:
    
    def __init__(self):
#         mydb=mysql.connector.connect(  host="localhost",
#   user="root",
#   password="root@1234")

        mydb=mysql.connector.connect(  os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),

        mycursor = mydb.cursor(dictionary=True)
        self.mycursor=mycursor
        self.mydb=mydb

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS med_db")
        self.mycursor.execute("USE med_db")
        create_table_query = """
       CREATE TABLE IF NOT EXISTS medicine (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    used_disease VARCHAR(100),
    stock_price DECIMAL(10,2),
    sale_price DECIMAL(10,2),
    stock_qty INT
    )"""   

        self.mycursor.execute(create_table_query)




    def exceuteQuery(self,query,values):
       self.mycursor.execute("USE med_db")
       if values:
           
        self.mycursor.execute(query, values)
       else:
          self.mycursor.execute(query, values)
       self.mydb.commit() 


    def fetchAll(self,query,values):
        self.mycursor.execute("USE med_db")        
        self.mycursor.execute(query,values)
        return self.mycursor.fetchall()

    def fetchOrderByStock(self,query):
         self.mycursor.execute("USE med_db") 
         self.mycursor.execute(query)
         return self.mycursor.fetchall()

          
    


    def fetchone(self,query,values):
         self.mycursor.execute("USE med_db")  
         self.mycursor.execute(query,values)      
         return self.mycursor.fetchone()    

