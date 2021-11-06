from fastapi import FastAPI
from routes.user import user

app = FastAPI(
             title='***** REST API - PRUEBA QUICK  FastAPI / MongoDB *******',
             description = '***** PRUEBA TECNICA BACKEND ***** By:  "JUAN CANTILLO "QUILLAONE"')


app.include_router(user)

