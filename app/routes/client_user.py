from fastapi import APIRouter, Depends, HTTPException
from app.models import User, UserResponse
from app.auth import create_access_token, verify_token

router = APIRouter()

@router.post("/sign-up")
async def sign_up(user: User):
    # Implement user registration logic (dummy implementation)
    # In a real scenario, you would save the user to a database
    verification_url = f"http://localhost:8000/verify/{user.username}"
    return {"verification_url": verification_url}

@router.post("/login")
async def login(user: User):
    # Validate the client user and generate a JWT (dummy validation here)
    if user.username == "client" and user.password == "client_password":  
        token = create_access_token(data={"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/download-file/{file_id}")
async def download_file(file_id: str, token: str = Depends(verify_token)):
    # Generate a secure download link (implement the logic here)
    download_link = f"http://localhost:8000/download-file/{file_id}"
    return {"download_link": download_link, "message": "success"}

@router.get("/list-files", response_model=UserResponse)
async def list_files(token: str = Depends(verify_token)):
    # Return a list of files uploaded by the client user (dummy implementation)
    return {"username": "client_username", "files": ["file1", "file2"]}
