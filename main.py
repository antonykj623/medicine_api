
import DataHandle
import Db
import MedicineModel
import user
from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from pydantic import BaseModel
import hashlib
import userauth



app = FastAPI()
security = HTTPBearer()

@app.get("/")
def home():
    return {"message": "Welcome to Medicine Application"}

@app.get("/about")
def about():
    return {"message": "User can order medicines in application "}

@app.get("/medicine/{id}")
def get_user(id: int, authorization: HTTPAuthorizationCredentials = Depends(security)):

    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token = authorization.credentials.replace("Bearer ", "")
    auth = userauth.UserAuthentication()
    isvalid=auth.validToken(token)
    if isvalid:        
      db=Db.Db()
      dt=DataHandle.DataHandleOp(db)
      data=dt.getMedicineBYID(id)
      if(data):
    
        return {"status":1,"message": "success","data":data}
      else:

        return {"status":0,"message":"no data found"}
    else:
        raise HTTPException(status_code=401, detail="Invalid user")


@app.get("/getAllMedicineByStockAscend")
def getAllMedicineAscend(authorization: HTTPAuthorizationCredentials = Depends(security)):
        if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

        token = authorization.credentials.replace("Bearer ", "")
        auth = userauth.UserAuthentication()
        isvalid=auth.validToken(token)
        if isvalid: 
          db=Db.Db()
          dt=DataHandle.DataHandleOp(db)
          data=dt.getMedicineByStockAscend()
          if(len(data)>0):
    
            return {"status":1,"message": "success","data":data}
          else:

            return {"status":0,"message":"no data found"}
    

@app.get("/getAllMedicineByStockDescend")
def getAllMedicineDescend(authorization: HTTPAuthorizationCredentials = Depends(security)):
        if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

        token = authorization.credentials.replace("Bearer ", "")
        auth = userauth.UserAuthentication()
        isvalid=auth.validToken(token)
        if isvalid:     
         db=Db.Db()
         dt=DataHandle.DataHandleOp(db)
         data=dt.getMedicineByStockDescend()
         if(len(data)>0):
    
           return {"status":1,"message": "success","data":data}
         else:

           return {"status":0,"message":"no data found"}    
    
    
  
    

@app.get("/getAllMedicines")
def getAllMedicines(authorization: HTTPAuthorizationCredentials = Depends(security)):
        if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

        token = authorization.credentials.replace("Bearer ", "")
        auth = userauth.UserAuthentication()
        isvalid=auth.validToken(token)
        if isvalid:     
          db=Db.Db()
          dt=DataHandle.DataHandleOp(db)
          data=dt.list_all()
          if(len(data)>0):
    
            return {"status":1,"message": "success","data":data}
          else:

            return {"status":0,"message":"no data found"}  
    

@app.get("/SearchMedicine/{word}")
def getAllMedicines(word:str,authorization: HTTPAuthorizationCredentials = Depends(security)):
        if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

        token = authorization.credentials.replace("Bearer ", "")
        auth = userauth.UserAuthentication()
        isvalid=auth.validToken(token)
        if isvalid:     
          db=Db.Db()
          dt=DataHandle.DataHandleOp(db)
          data=dt.getMedicineByName(word)
          if(len(data)>0):
    
           return {"status":1,"message": "success","data":data}
          else:

           return {"status":0,"message":"no data found"}    


    
@app.get("/deleteMedicine/{id}")
def deleteMedicine(id:str,authorization: HTTPAuthorizationCredentials = Depends(security)):
       if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

         token = authorization.credentials.replace("Bearer ", "")
         auth = userauth.UserAuthentication()
         isvalid=auth.validToken(token)
         if isvalid:       
            db=Db.Db()
            dt=DataHandle.DataHandleOp(db)
            dt.deleteMedicine(id)
            return {"status":1,"message": "successfully deleted medicine",}


@app.post("/addMedicine")
def addMedicine(medicine: MedicineModel.Medicine,authorization: HTTPAuthorizationCredentials = Depends(security)):
       if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

         token = authorization.credentials.replace("Bearer ", "")
         auth = userauth.UserAuthentication()
         isvalid=auth.validToken(token)
         if isvalid: 
           db=Db.Db()
           dt=DataHandle.DataHandleOp(db)
           dt.add(medicine.name,medicine.description,medicine.used_disease,medicine.stock_price,medicine.sale_price,medicine.stock_qty)

           return {
            "message": "Medicine added successfully",
            "data": medicine
        }
  

@app.post("/UpdateMedicine")
def UpdateMedicine(medicine: MedicineModel.Medicine,authorization: HTTPAuthorizationCredentials = Depends(security)):
       if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

         token = authorization.credentials.replace("Bearer ", "")
         auth = userauth.UserAuthentication()
         isvalid=auth.validToken(token)
         if isvalid: 
           db=Db.Db()
           dt=DataHandle.DataHandleOp(db)
           dt.updateMedicine(medicine.id,medicine.name,medicine.description,medicine.used_disease,medicine.stock_price,medicine.sale_price,medicine.stock_qty)

           return {
             "message": "Medicine updated successfully",
             "data": medicine
    }

@app.post("/user/register")
def InsertUser(us:user.User,authorization: HTTPAuthorizationCredentials = Depends(security)):
       if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

         token = authorization.credentials.replace("Bearer ", "")
         auth = userauth.UserAuthentication()
         isvalid=auth.validToken(token)
         if isvalid:     
           db=Db.Db()
           dt=DataHandle.DataHandleOp(db)
           dt.addUser(us.name,us.phone,us.email)

           return{
  "message": "User added successfully",
        "data": us
    }

@app.post("/user/update")
def InsertUser(us:user.User,authorization: HTTPAuthorizationCredentials = Depends(security)):
       if authorization is None:
         raise HTTPException(status_code=401, detail="Authorization header missing")

         token = authorization.credentials.replace("Bearer ", "")
         auth = userauth.UserAuthentication()
         isvalid=auth.validToken(token)
         if isvalid:  
           db=Db.Db()
           dt=DataHandle.DataHandleOp(db)
           encrypted = hashlib.md5(us.password.encode()).hexdigest()
           dt.updateUser(us.id,us.name,us.phone,us.email,encrypted)

           return{
  "message": "User updated successfully",
        "data": us
    }


@app.get("/user/listAllUser")
def listAllUser(authorization: HTTPAuthorizationCredentials = Depends(security)):

    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    token = authorization.credentials

    auth = userauth.UserAuthentication()
    isvalid = auth.validToken(token)

    if not isvalid:
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )

    db = Db.Db()
    dt = DataHandle.DataHandleOp(db)
    data = dt.getAlUser()

    if data:
        return {
            "status": 1,
            "message": "success",
            "data": data
        }

    return {
        "status": 0,
        "message": "No data found"
    }
    
@app.get("/user/generateToken")
def generateToken(mobile,password):
    encrypted = hashlib.md5(password.encode()).hexdigest()
    db=Db.Db()
    dt=DataHandle.DataHandleOp(db)
    data=dt.getUser(mobile,encrypted)
    auth = userauth.UserAuthentication()
    token = auth.createToken(data)
    if(data):
    
        return {"status":1,"message": "success","data":token}
    else:

        return {"status":0,"message":"no data found"}      
    





  
