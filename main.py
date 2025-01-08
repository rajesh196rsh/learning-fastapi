from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'testjson':'Hello'}

@app.get('/about/test1')
def about():
    return {"about": "Displaying about info"}


@app.get('/about/test12')
def about_again():
    return {"about": "Displaying about again"}
    
