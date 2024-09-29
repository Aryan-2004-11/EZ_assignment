
## Overview
The Secure File Sharing System is a web application that allows two different types of users (Ops User and Client User) to securely upload and share files. The system uses JWT (JSON Web Tokens) for authentication and supports various file types.

## Technologies
### Backend
- FastAPI

### Database
- MongoDB

### Authentication
- JWT (JSON Web Tokens)

### Frontend
- (if applicable, mention it here)

### Environment
- Python 3.x

## Features
- User authentication with JWT.
- Secure file upload for specific file types (e.g., .pptx, .docx, .xlsx).
- File validation and error handling.
- Support for different user roles (Ops User and Client User).

## Installation
### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/secure-file-sharing-system.git
cd secure-file-sharing-system
```

### Step 2: Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install the dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up your environment variables
Create a `.env` file in the root directory and add the following:
```
JWT_SECRET=your_jwt_secret_key
MONGODB_URI=your_mongodb_uri
```

### Step 5: Run the application
```bash
uvicorn app.main:app --reload
```

## Usage
1. **Authentication**: Send a POST request to `/login` with the username and password to receive a JWT token.
2. **File Upload**: Use the JWT token to access the `/upload-file` endpoint. Set the `Authorization` header as `Bearer your_generated_token` and send the file in the body as form-data.

## API Endpoints
| Method | Endpoint     | Description                                     |
|--------|--------------|-------------------------------------------------|
| POST   | /login       | Authenticate user and return a JWT token.      |
| POST   | /upload-file | Upload a file (only specific formats allowed). |

