from fastapi import APIRouter, Response
from pymongo.auth import _password_digest
from config.db import conex
from schemas.user import userEntity, usersEntity
from models.user import User
from models.auth import Auth
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from fastapi import FastAPI, HTTPException


user = APIRouter()

# METODO GetUser
@user.get('/users', response_model=list[User])
def find_all_user():
    return usersEntity(conex.local.user.find())


# METODO CreateUser
@user.post('/users', response_model=User)
def create_user(user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']

    id = conex.local.user.insert_one(new_user).inserted_id
    user = conex.local.user.find_one({'_id': id})
    return userEntity(user)


# METODO GetUser
@user.get('/users/{id}')
def find_user(id: str):
    return userEntity(conex.local.user.find_one({"_id": ObjectId(id)}))


# METODO Login
@user.post('/login')
def user_login(auth: Auth):
  try:
    user = userEntity(conex.local.user.find_one({"mobil_phone": auth.mobil_phone}))
    if user is not None and sha256_crypt.verify(auth.password, user["password"]):
      return user
    return Response(status_code=HTTP_401_UNAUTHORIZED)
  except:
    return Response(status_code=HTTP_401_UNAUTHORIZED) 
    



# METODO UPDATE (PUT)
@user.put('/users/{id}')
def update_user(id: str, user: User):
    conex.local.user.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': dict(user)})
    return userEntity(conex.local.user.find_one({'_id': ObjectId(id)}))


# METODO DELETE
@user.delete('/users/{id}')
def delete_user():
    userEntity(conex.local.user.find_one({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
