import Db

class DataHandleOp:

    def __init__(self,Db):
        self.Db=Db



    def getMedicineByName(self,text):

     query = """
SELECT * FROM medicine 
WHERE name LIKE %s 
AND description LIKE %s
"""

     value = "%" + text + "%"
     return self.Db.fetchAll(query,(value,value))

   

    def add(self, name, desc, disease, sp, cp, qty):
        query = """
        INSERT INTO medicine 
        (name, description, used_disease, stock_price, sale_price, stock_qty)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        self.Db.exceuteQuery(query, (name, desc, disease, sp, cp, qty))
        print("Medicine Added ✅")


    def addUser(self, name, phone, email,password):
        query = """
        INSERT INTO users 
        (name, phone, email,password)
        VALUES (%s,%s,%s,%s)
        """
        self.Db.exceuteQuery(query, (name, phone, email,password))
        print("User Added ✅")        

    def list_all(self):
        q="SELECT * FROM medicine"
        return self.Db.fetchAll(q,None)
            

    def getAllDataByID(self,id):
       
       self.Db.exceuteQuery("USE medicine_db")
       query = """
SELECT * FROM medicine 
WHERE id = %s
"""

       value = id+""

       self.Db.exceuteQuery(query, (value,))

       myresult = self.Db.fetchone() 
       return myresult 
    



    def updateMedicine(self,id,name, desc, disease, sp, cp, qty):
       query = """
    UPDATE medicine 
    SET name = %s,
        description = %s,
        used_disease = %s,
        stock_price = %s,
        sale_price = %s,
        stock_qty = %s
    WHERE id = %s
    """
       values = (name, desc, disease, sp, cp, qty, id)

       self.Db.exceuteQuery(query, values)
       
       print("Data updated successfully")  



    def deleteMedicine(self,id):
       query = """
    DELETE FROM medicine 
    WHERE id = %s
    """
       values = (id,)

       self.Db.exceuteQuery(query, values)
        
       print("Data Deleted successfully")


    def getMedicineByStockAscend(self):
       query="SELECT * FROM medicine ORDER BY id ASC"
       return self.Db.fetchOrderByStock(query)
    

    def getMedicineByStockDescend(self):
       query="SELECT * FROM medicine ORDER BY id DESC"
       return self.Db.fetchOrderByStock(query)
    
    def getMedicineBYID(self,id):
       query="SELECT * FROM medicine WHERE id = %s"
       values=(id,)
       return self.Db.fetchone(query,values)
    
    def getAlUser(self):
       query="SELECT * FROM users"
       
       return self.Db.getAllUser(query) 

    def updateUser(self,id,name,phone, email, password):
       query = """
    UPDATE users 
    SET name = %s,
        email = %s,
        phone = %s,
        password = %s
    WHERE id = %s
    """
       values = (name, email, phone, password, id)

       self.Db.exceuteQuery(query, values)
       
       print("Data updated successfully")         
    
    def getUser(self,email,password):
       query="SELECT * FROM users WHERE phone = %s AND password = %s"
       values=(email,password)
       return self.Db.fetchone(query,values)       


   
