import Db
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

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
    
    def geTotalInventoryStock(self):
       query="SELECT stock_price,stock_qty  FROM medicine"
       data = self.Db.getAlMedicineData(query)
       array1=np.array(data)

       total_inventory=0

    
       for item in array1:
        total_inventory=total_inventory+(float(item['stock_qty'])*float(item['stock_price']))
        


       return total_inventory




    def getTotalEstimatedProfitEach(self):
       query="SELECT stock_price,stock_qty,sale_price  FROM medicine"
       data = self.Db.getAlMedicineData(query)
       

       

    
       for item in data:
        stprice=float(item['stock_price'])
        slprice=float(item['sale_price'])
        dif=slprice-stprice;
        item['unitprofit_price']=dif
        item['total_profit']=(float(item['stock_qty'])*dif)

       return data


    def getTotalEstimatedProfit(self):
       query="SELECT stock_price,stock_qty,sale_price  FROM medicine"
       data = self.Db.getAlMedicineData(query)
       array1=np.array(data)

       total_profit=0

    
       for item in array1:
        stprice=float(item['stock_price'])
        slprice=float(item['sale_price'])
        dif=slprice-stprice;


        

        total_profit=total_profit+(float(item['stock_qty'])*dif)
        


       return round(total_profit, 2)


    
    def getEstimatedProfitByMedicine(self,medicine):
       query="SELECT stock_price,stock_qty,sale_price  FROM medicine WHERE name = %s"
       values=(medicine,)
       data =self.Db.fetchone(query,values)    
       print(data)   
       
       

       total_profit=0
       stprice = float(data["stock_price"])
       stock_qty = float(data["stock_qty"])
       slprice = float(data["sale_price"])
       diff=slprice-stprice
       total_profit=total_profit+(stock_qty*diff)


        


        


       return round(total_profit, 2)




    



    

        
    def getMedicineProperties(self):
       query="SELECT *  FROM medicine"
       data = self.Db.getAlMedicineData(query)
       array1=np.array(data)
       
       arr = np.array([])    
       for item in array1:
        arr = np.append(arr, float(item['sale_price']))


        minprice=np.min(arr) 
        maxprice=np.max(arr)

        mdianval=np.median(arr)
        meeanval=np.mean(arr)

        finalarr={"min_price":minprice,"maxprice":maxprice,"meadian_sale_price":mdianval,"meanval_price":meeanval}
        
        


       return finalarr 

       





       
       

    def getAveragePrice(self, category):

     query = "SELECT * FROM medicine WHERE description LIKE %s"
     value = "%" + category + "%"
     values = (value,)

     data = self.Db.fetchAll(query, values)

     if len(data) == 0:
         return None

     X = []
     y = []

     total_stockprice = 0
     total_stockqty = 0

     for row in data:
        X.append([ float(row["stock_price"]),  float(row["stock_qty"])])
        y.append( float(row["sale_price"]))

        total_stockprice +=  float(row["stock_price"])
        total_stockqty +=  float(row["stock_qty"])

     average_stockprice = total_stockprice / len(data)
     average_stockqty = total_stockqty / len(data)

     model = LinearRegression()
     model.fit(X, y)

     prediction = model.predict([[average_stockprice, average_stockqty]])

     return float(prediction[0]) 

   
   