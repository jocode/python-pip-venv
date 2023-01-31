from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1, 2, 3, 4]

@app.get("/contact")
def get_contact():
    return {"name": "John", "email": "correo@correo.com", "phone": "123456789"}

@app.get("/about", response_class=HTMLResponse)
def get_about():
    return """
    <html>
        <head>
            <title>About</title>
        </head>
        <body>
            <h1>About</h1>
            <p>FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.</p>
        </body>
    </html>
    """