# request_ = request.get_json(force=True)
#     param_keys = request_["queryResult"]["parameters"].keys()
#     param_Values = request_["queryResult"]["parameters"].values()
    
#     key_iterator = iter(param_keys)
#     key = next(key_iterator)
#     print(key)

#     value_iterator = iter(param_Values)
#     value = next(value_iterator)
#     print(value)

#     if(key == "email"):
#         return {'fulfillment_text': "Please Enter your Title Mr / Miss / Ms / Dr / Prof"} #agent.response("fulfillment_text:Please Enter your Title Mr / Miss / Ms / Dr / Prof from Lap")
#             #agent.add("Please Enter your Title Mr / Miss / Ms / Dr / Prof")
#     if(key == "title"):
#         return {'fulfillment_text': "Please Enter Your First Name"} 
#     if(key == "FName"):
#         NameValue = iter(value.values())
#         FName = next(NameValue)
#         print(FName)
#         return {'fulfillment_text': "Please Enter Your Middle Name"} 
#     if(key == "MName"):
#         NameValue = iter(value.values())
#         MName = next(NameValue)
#         print(MName)
#         return {'fulfillment_text': "Please Enter Your Last Name"}
#     if(key == "LName"):
#         NameValue = iter(value.values())
#         LName = next(NameValue)
#         print(LName)
#         return {'fulfillment_text': "Please Enter Your DOB (DD/MM/YYYY)"}
#     if(key == "Dob"):
#         #Value = iter(value.values())
#         #Name = next(Value)
#         #print(LName)
#         return {'fulfillment_text': "Please Enter you Nationality"}
#     if(key == "Nationality"):
#         return {'fulfillment_text': "Please Enter Posport Number"}
#     if(key == "passport"):
#         return {'fulfillment_text': "Thanks for your Registration please continue with this link"}




# def title(title: str):
#     user_data.append(title)
#     print(user_data)
#     return {'fulfillmentText': "Please enter your first name"}

# def first_name(first_name: str):
#     user_data.append(first_name)
#     print(user_data)
#     return {'fulfillmentText': "Please enter your middle name, if you don't have any middle name just say 'No' !"}

# def middle_name(middle_name: str):
#     user_data.append(middle_name)
#     print(user_data)
#     return {'fulfillmentText': "Please enter your last name, if you don't have any last name just say 'No' !"}

# def last_name(last_name: str):
#     user_data.append(last_name)
#     print("lastname", user_data)
#     return {'fulfillmentText': "Please enter your gender"}

# def gender(gender: str):
#     user_data.append(gender)
#     print(user_data)
#     return {'fulfillmentText': "Please enter your date of birth in dd/mm/yyyy format"}

# def dob(dob: str):
#     user_data.append(dob)
#     print(user_data)
#     return {'fulfillmentText': "Please enter your Nationality. (eg: Indian, American, German"}

# def nationality(nationality: str):
#     user_data.append(nationality)
#     print(user_data)
#     return {'fulfillmentText': "Thanks for completing the basic registration process, please follow this link to create your account. "}

# def save_data():
#     print("this is save data" ,user_data)
#     return "pass"


# for key in data_from_user:
    #     print("key...", key)
    #     if key == "email":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print("value...", value)
    #             return verify_email(value, db_session)
    #     if key == "title":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print(value)
    #             return title(value)
    #     if key == "first-name":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print(value)
    #             return first_name(value)
    #     if key == "middle-name":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print(value)
    #             return middle_name(value)
    #     if key == "last-name":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print(value)
    #             return last_name(value)
    #     if key == "gender":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print(value)
    #             return gender(value)
    #     if key == "date-of-birth":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print(value)
    #             return dob(value)
    #     if key == "nationality":
    #         user_input = json_data["queryResult"]["parameters"].values()
    #         for value in user_input:
    #             print(value)
    #             return nationality(value)

    # switcher = {
    #     "existing_user": existing_user,
    #     # "email": verify_email,
    #     # "title": title,
    #     # "first_name": first_name,
    #     # "middle_name": middle_name,
    #     # "last_name": last_name,
    #     # "dob": dob,
    #     # "gender": gender,
    #     # "nationality": nationality,
    # }
    # res = switcher.get(key, lambda: "Invalid value")
    # # save_data()
    # # print("userDataList........",user_data)
    # return res()


# Driver program
# if __name__ == "__main__":
#     argument=0
#     print (numbers_to_strings(argument))

# @router.post("/webhook")
# async def verify_email(json_data: Dict, db_session: Session = Depends(get_db)):
#     print("Request......", json_data)
#     # data_from_user = json_data["queryResult"]["queryText"]
#     data_from_user = json_data["queryResult"]["parameters"]
#     para = data_from_user.keys()
#     for i in para:
#         print(i)

    # print(engine.table_names())

    # db_user = db_session.query(PreRegistration).filter(PreRegistration.email == data_from_user).first()
    # if db_user:
    #     return {'fulfillmentText': "Email already registered"}db_user = db_session.query(PreRegistration).filter(PreRegistration.email == data_from_user).first()
    # if db_user:
    #     return {'fulfillmentText': "Email already registered"}
    # else:
        # user_data.append(data_from_user)
        # newUser = PreRegistration(email= entered_email)
        # db_session.add(newUser)
        # db_session.commit()
        # db_session.refresh(newUser)
        # return {'fulfillmentText': f"{newUser} registered successfully"}
    # return {
    #     'fulfillmentText': "from Sridhar's laptop"
    # }