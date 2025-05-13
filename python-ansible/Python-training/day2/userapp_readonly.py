
from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from schema import userdata
from random import randrange 
from userapp import data
from userapp import searchuser
from database import engine, get_connection 
import models
from sqlalchemy.orm import Session 

router= APIRouter(tags=["BOA USER reader APP"])


@router.get("/loaduser/{id}")
def finduserwithID (id:int):
    a=  searchuser(id)
    if a == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= " Given ID is not found")
    return a



@router.get("/welcome")
def showWelcome():
    return {"message", "Welcome to Fast  API !!!"}


@router.get("/login")
def loginpage():
    return{"Welcome to login!! "}

#get function which is used to load the userdata 
@router.get("/userdata")
def userdatafun(db:Session= Depends(get_connection)):
    data = db.query(models.Userapp).all()
    return{"Data": data}
