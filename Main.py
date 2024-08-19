from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from routers.transaction_type import transaction_type_router

Base.metadata.create_all(bind=engine)

app = FastAPI()



app.title = "Mi super app"
app.description = "esta es un aplicación de prueba"
app.version = "0.0.1"

app.include_router(transaction_type_router)


@app.get("/", tags=["Home"])
def home():
    return HTMLResponse(content="<h1>Mi super app</h1>")