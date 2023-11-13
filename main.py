import api_handle
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Muy buenas tardes soy Creep1ng.</h1>
"""

def run():
    response = api_handle.get_categories()
    print(response.text)
    print(response.status_code)

if __name__ == "__main__":
    run()