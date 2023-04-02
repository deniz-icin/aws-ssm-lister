from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from parameters import is_response_successful , list_parameters , print_parameters, list_contents_of_parameter

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/parameters",response_class=HTMLResponse)
async def root(request: Request):
    parameters = print_parameters()
    return templates.TemplateResponse("item.html", {"request": request, "parameter": parameters})

@app.get("/parameters/{parameter}",response_class=HTMLResponse)
async def read_item(request: Request, parameter = str):
    objs = list_contents_of_parameter(parameter)
    return templates.TemplateResponse("contents.html", {"request": request, "parameter": objs})