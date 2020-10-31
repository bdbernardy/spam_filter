import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.core.api_server:app", host="localhost", port=5050, debug=True, reload=True)
