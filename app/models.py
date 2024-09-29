from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    password: str

class FileUpload(BaseModel):
    filename: str
    file_type: str
    content: str  # Use Base64 for file content if necessary

class UserResponse(BaseModel):
    username: str
    files: List[str]  # List of file names uploaded by the user
