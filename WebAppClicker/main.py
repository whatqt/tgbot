if __name__ == "__main__":
    import uvicorn
    uvicorn.run("asgi:app", log_level="info", reload=True)