# Installation
---
## Create virtual environment
`python -m venv C:\path\of\this\project\.venv`
## Activate virtual environment (powershell)

### 1. Modify policy
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
### 2. Go to project directory
`cd C:\path\of\this\project`
### 3. Execute venv script
`.venv\bin\Activate.ps1`

## Install dependencies
`pip install flask flask-mysqldb python-dotenv`

# Post install
---
- Import `flask_endterm.sql` to your database
- Modify .env variables to your MySQL credentials
