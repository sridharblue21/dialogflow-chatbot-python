request_ = request.get_json(force=True)
    param_keys = request_["queryResult"]["parameters"].keys()
    param_Values = request_["queryResult"]["parameters"].values()
    
    key_iterator = iter(param_keys)
    key = next(key_iterator)
    print(key)

    value_iterator = iter(param_Values)
    value = next(value_iterator)
    print(value)

    if(key == "email"):
        return {'fulfillment_text': "Please Enter your Title Mr / Miss / Ms / Dr / Prof"} #agent.response("fulfillment_text:Please Enter your Title Mr / Miss / Ms / Dr / Prof from Lap")
            #agent.add("Please Enter your Title Mr / Miss / Ms / Dr / Prof")
    if(key == "title"):
        return {'fulfillment_text': "Please Enter Your First Name"} 
    if(key == "FName"):
        NameValue = iter(value.values())
        FName = next(NameValue)
        print(FName)
        return {'fulfillment_text': "Please Enter Your Middle Name"} 
    if(key == "MName"):
        NameValue = iter(value.values())
        MName = next(NameValue)
        print(MName)
        return {'fulfillment_text': "Please Enter Your Last Name"}
    if(key == "LName"):
        NameValue = iter(value.values())
        LName = next(NameValue)
        print(LName)
        return {'fulfillment_text': "Please Enter Your DOB (DD/MM/YYYY)"}
    if(key == "Dob"):
        #Value = iter(value.values())
        #Name = next(Value)
        #print(LName)
        return {'fulfillment_text': "Please Enter you Nationality"}
    if(key == "Nationality"):
        return {'fulfillment_text': "Please Enter Posport Number"}
    if(key == "passport"):
        return {'fulfillment_text': "Thanks for your Registration please continue with this link"}