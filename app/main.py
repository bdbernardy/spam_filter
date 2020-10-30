import uvicorn
from app.api.server import app

if __name__ == "__main__":
    uvicorn.run("api.server:app", host="localhost", port=5050, debug=True, reload=True)
