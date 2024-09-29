from fastapi import APIRouter, UploadFile, File, Depends,HTTPException
from app.auth import create_access_token, verify_token
from app.models import User

router = APIRouter()

@router.post("/login")
async def login(user: User):
    # Validate the ops user and generate a JWT (dummy validation here)
    # In a real scenario, validate against a user database
    if user.username == "ops" and user.password == "ops_password":  
        token = create_access_token(data={"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...), token: str = Depends(verify_token)):
    # Validate the file type and save it
    file_type = file.filename.split('.')[-1]
    if file_type not in ['pptx', 'docx', 'xlsx']:
        raise HTTPException(status_code=400, detail="Invalid file type. Only pptx, docx, and xlsx are allowed.")
    
    # Save the file (implement file saving logic here)
    # e.g., save to MongoDB or file system
    return {"filename": file.filename, "message": "File uploaded successfully."}