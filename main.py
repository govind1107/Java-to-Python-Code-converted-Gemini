from fastapi  import FastAPI, File, UploadFile , HTTPException
from fastapi.responses import FileResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import aiofiles
import os
import google.generativeai as genai
import uvicorn
from src.helper import convert_java_to_python
from src.helper import convert_java_to_python_1





app = FastAPI()


INPUT_DIR = "./input_files"
OUTPUT_DIR = "./output_files"

os.makedirs(INPUT_DIR,exist_ok=True)
os.makedirs(OUTPUT_DIR,exist_ok=True)

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})





    
@app.post("/convert")
async def convert_file(file : UploadFile = File(...)):
    if not file.filename.endswith("java"):
        raise HTTPException(status_code = 400 ,detail = "Invalid file type . Only .java files are accepted.")
    
    input_path = os.path.join(INPUT_DIR, file.filename)

    async with aiofiles.open(input_path,'wb') as in_file:
        content = await file.read()
        await in_file.write(content)

    async with aiofiles.open(input_path,'r') as in_file:
        java_code = await in_file.read()

    # desc = await convert_java_to_python(java_code)

    python_code = convert_java_to_python_1(java_code)

    output_filename = file.filename.replace(".java",".py")

    output_path = os.path.join(OUTPUT_DIR,output_filename)

    async with aiofiles.open(output_path, 'w') as out_file:
        await out_file.write(python_code)


    return {"python_code": python_code , "download_link": f"/download/{output_filename}"}


#Endpoint to handle file download

@app.get("/download/{filename}")
async def download_file(filename : str):
    #Define the path of file to be downloaded 

    file_path = os.path.join(OUTPUT_DIR,filename)

    #Check if the file exists

    if os.path.exists(file_path):
        return FileResponse(file_path,filename=filename)
    else:
        raise HTTPException(status_code=404 ,detail = "File not found")
    


if __name__ == "__main__":
    uvicorn.run(app,host = "0.0.0.0",port = 8080)




