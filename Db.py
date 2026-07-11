import mysql.connector

class Db:
    
    def __init__(self):
        mydb=mysql.connector.connect(  host="sql12.freesqldatabase.com",
  user="sql12832775",
  password="nDyArKF9pK",
  )

        mycursor = mydb.cursor(dictionary=True)
        self.mycursor=mycursor
        self.mydb=mydb

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS sql12832775")
        self.mycursor.execute("USE sql12832775")
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
       self.mycursor.execute("USE sql12832775")
       if values:
           
        self.mycursor.execute(query, values)
       else:
          self.mycursor.execute(query, values)
       self.mydb.commit() 


    def fetchAll(self,query,values):
        self.mycursor.execute("USE sql12832775")        
        self.mycursor.execute(query,values)
        return self.mycursor.fetchall()

    def fetchOrderByStock(self,query):
         self.mycursor.execute("USE sql12832775") 
         self.mycursor.execute(query)
         return self.mycursor.fetchall()

          
    


    def fetchone(self,query,values):
         self.mycursor.execute("USE sql12832775")  
         self.mycursor.execute(query,values)      
         return self.mycursor.fetchone()    

