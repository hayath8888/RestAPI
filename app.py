import requests
import random
import json
import string


# url = "http://localhost:8080/identityiq/scim/v2/Accounts/:accountId"

# payload={}
# headers = {
#   'Accept': 'application/json'
# }

# response = requests.get(url, headers=headers, data=payload)

# print(response.status_code)

base_url="https://gorest.co.in"

auth_token="Bearer db4515c18ca79102604339f7edd9d05f5fd435582c0e3763306e3f3b24cba917"

class User:
 def __init__(self,id,name,gender):
   self.id=id
   self.name=name
   self.gender=gender

 def __str__(self):

  return f"Id:{self.id}, Name:{self.name}, Gender:{self.gender}"

#--------------------getting all user using api-----------------------
def getrequest():

  url=base_url+"/public/v2/users/"
  header={"authorization":auth_token}
  response=requests.get(url,headers=header)
  assert response.status_code==200
  json_data=response.json()
  json_str = json.dumps(response.json(),indent=4)
  print(json_str)
  #print(json_data)
  #return response.json()

getrequest()          #users=getrequest()

#user_object=[]

# for user in users:
#   Uobject=User(user["id"], user["name"], user["gender"])
#   user_object.append(Uobject)

# for user in user_object:
#   print(user)

#---------------------------post method send user to api------------------------------
def postrequest():

  url=base_url+"/public/v2/users"

  header={"authorization":auth_token}

  data={
     "name": "hayath",
     "email":"hayath@email.com",
     "gender":"male",
     "status":"active"
  }

  response=requests.post(url, json=data,headers=header)
  #assert response.status_code==200
  json_data=response.json()
  json_str=json.dumps(json_data,indent=4)
  print("post response=",json_str)
  
#postrequest()

#------------------------------get method with userId as paraameter--------------------

def getrequestID():
  url=base_url+"/public/v2/users/5912506"
  header={"authentication":auth_token}
  
  response=requests.get(url,headers=header)
  json_data=response.json()
  json_str=json.dumps(json_data,indent=5)
  print("get UserID:",json_str)

#getrequestID()

#-----------------------put method updating user ----------------------

def putmethod():
   url=base_url+"/public/v2/users/5912506"
   header={"authorization":auth_token}
   data={
     "name":"Basha",
     "email":"basha@gmail.com",
     "status":"inactive"
   }

   response=requests.put(url,json=data,headers=header)
   json_str=json.dumps(response.json(),indent=4)
   print("updated!:",json_str)

#putmethod()

#-----------------delete method to delete a user -------------------------

def deleterequest():
   url=base_url+"/public/v2/users/5912505"
   header={"authorization":auth_token}

   response=requests.delete(url,headers=header)
   json_str=json.dumps(response.json(),indent=4)
   print("deleted!:",json_str)

#deleterequest()




