
import DataHandle
import Db
import MedicineModel
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Medicine Application"}

@app.get("/about")
def about():
    return {"message": "User can order medicines in application "}

@app.get("/medicine/{id}")
def get_user(id: int):
    return {"user_id": id}

@app.get("/getAllMedicineByStockAscend")
def getAllMedicineAscend():
    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    data=dt.getMedicineByStockAscend()
    if(len(data)>0):
    
        return {"status":1,"message": "success","data":data}
    else:

        return {"status":0,"message":"no data found"}
    

@app.get("/getAllMedicineByStockDescend")
def getAllMedicineDescend():
    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    data=dt.getMedicineByStockDescend()
    if(len(data)>0):
    
        return {"status":1,"message": "success","data":data}
    else:

        return {"status":0,"message":"no data found"}    
    
    
@app.get("/getAllMedicineByStockDescend")
def getAllMedicineDescend():
    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    data=dt.getMedicineByStockDescend()
    if(len(data)>0):
    
        return {"status":1,"message": "success","data":data}
    else:

        return {"status":0,"message":"no data found"}       
    

@app.get("/getAllMedicines")
def getAllMedicines():
    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    data=dt.list_all()
    if(len(data)>0):
    
        return {"status":1,"message": "success","data":data}
    else:

        return {"status":0,"message":"no data found"}  
    

@app.get("/SearchMedicine/{word}")
def getAllMedicines(word:str):
    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    data=dt.getMedicineByName(word)
    if(len(data)>0):
    
        return {"status":1,"message": "success","data":data}
    else:

        return {"status":0,"message":"no data found"}         
    
@app.get("/deleteMedicine/{id}")
def deleteMedicine(id:str):
    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    dt.deleteMedicine(id)
    return {"status":1,"message": "successfully deleted medicine",}


@app.post("/addMedicine")
def addMedicine(medicine: MedicineModel.Medicine):

    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    dt.add(medicine.name,medicine.description,medicine.used_disease,medicine.stock_price,medicine.sale_price,medicine.stock_qty)

    return {
        "message": "Medicine added successfully",
        "data": medicine
    }
  

@app.post("/UpdateMedicine")
def UpdateMedicine(medicine: MedicineModel.Medicine):

    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    dt.updateMedicine(medicine.id,medicine.name,medicine.description,medicine.used_disease,medicine.stock_price,medicine.sale_price,medicine.stock_qty)

    return {
        "message": "Medicine updated successfully",
        "data": medicine
    }
  
