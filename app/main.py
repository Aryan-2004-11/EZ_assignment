from fastapi import FastAPI
from app.database import connect_to_db, close_db_connection
from app.routes import ops_user, client_user

app = FastAPI()

# Middleware to connect to the database for each request
@app.middleware("http")
async def db_session_middleware(request, call_next):
    await connect_to_db()  # Connect to the database
    response = await call_next(request)
    await close_db_connection()  # Close the database connection
    return response

# Include the routes
app.include_router(ops_user.router)
app.include_router(client_user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the secure file-sharing API!"}
