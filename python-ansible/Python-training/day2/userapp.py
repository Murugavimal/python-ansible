
from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from schema import userdata
from random import randrange 
from database import engine, get_connection 
import models
from sqlalchemy.orm import Session 

router= APIRouter(tags=["BOA USER APP"])



data=[]

def searchuser(id):
    for i, v in enumerate(data):
        if v["ID"] == id:
            return v

def searchpositionofID(id):
    for i, v in enumerate(data):
        if v["ID"] == id:
            return i



@router.delete("/deleteusr/{id}", status_code= status.HTTP_200_OK)
def deleteusr (id:int):
    a=  searchpositionofID(id)
    if a == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= " Given ID is not found")
    data.pop(a)
    
    return data


@router.put("/update/{id}")
def updateuser(id:int, udata:userdata):
    position = searchpositionofID(id)
    if position == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    udatadict = udata.model_dump()
    if data[position]["ID"] == id:
        data[position] = udatadict
        return {"updated " : data}





@router.post("/userdata", status_code= status.HTTP_201_CREATED)
def userdatapost(user:userdata, db:Session=Depends(get_connection)):


    singleuser=models.Userapp(**user.model_dump())
    db.add(singleuser)
    db.commit()
 
    return {"User details" : data}

    
