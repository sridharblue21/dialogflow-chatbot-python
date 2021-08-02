from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session
from .database import get_db
from .models import PreRegistration
from typing import Dict
from starlette.requests import Request

router = APIRouter()
user_data = {}

def existing_user():
    return {'fulfillmentText': "Registered users can login directly from our website using your registered email address. Please enter a different email address to proceed further" }

def verify_email(email: str, db_session: Session, link):
    db_user = db_session.query(PreRegistration).filter(PreRegistration.email == email).first()
    if db_user:
        return {'fulfillmentText': f"Email already registered, Please go ahead and login directly from our website using your registered email address. {link}"}
    user_data.update({'email': email})
    next = "What is your title?  Mr / Mrs / Ms  / Dr /  Prof?"
    return {'fulfillmentText': f"Please answer to few more quesions to finish your registration process, {next}"}

@router.post("/webhook")
def user_registration(request_: Dict, request: Request, db_session: Session = Depends(get_db)):
    website_link = "https://"+request.url.hostname
    param_keys = request_["queryResult"]["parameters"].keys()
    param_Values = request_["queryResult"]["parameters"].values()

    key_iterator = iter(param_keys)
    key = next(key_iterator)
    print(key)

    value_iterator = iter(param_Values)
    value = next(value_iterator)
    print(value)
    
    if(key == "email"):
        return verify_email(value, db_session, website_link)

    if(key == "title"):
        user_data.update({'title': value})
        return {'fulfillment_text': "Please Enter Your First Name"}

    if(key == "FName"):
        NameValue = iter(value.values())
        FName = next(NameValue)
        print(FName)
        user_data.update({'fname': FName})

        return {'fulfillment_text': "Please Enter Your Middle Name"} 

    if(key == "MName"):
        NameValue = iter(value.values())
        MName = next(NameValue)
        print(MName)
        user_data.update({'mname': MName})

        return {'fulfillment_text': "Please Enter Your Last Name"}

    if(key == "LName"):
        NameValue = iter(value.values())
        LName = next(NameValue)
        print(LName)
        user_data.update({'lname': LName})

        return {'fulfillment_text': "Please Enter Your Gender"}

    if(key == "Gender"):
        user_data.update({'gender': value})
        return {'fulfillment_text': "Please Enter you DOB (DD/MM/YYYY)"}

    if(key == "Dob"):
        user_data.update({'dob': value})
        return {'fulfillment_text': "Please Enter you Nationality"}

    if(key == "Nationality"):
        user_data.update({'nationality': value})

        newUser = PreRegistration(email= user_data['email'], title = user_data['title'], first_name = user_data['fname'], middle_name = user_data['mname'], last_name = user_data['lname'], gender=user_data['gender'], dob=user_data['dob'], nationality=user_data['nationality'])
        db_session.add(newUser)
        db_session.commit()
        db_session.refresh(newUser)
        print("Registration successful")
        return {'fulfillmentText': f"Thanks for completing the basic registration process, please follow this link to create your account. {website_link}"}