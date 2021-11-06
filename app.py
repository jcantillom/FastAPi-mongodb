from fastapi import FastAPI
from routes.user import user

app = FastAPI(title='***** PRUEBA QUICK *******',
             description= '***** PRUEBA TECNICA BACKEND ***** By:  "JUAN CANTILLO "QUILLAONE"')


app.include_router(user)

