import google.generativeai as genai
from fastapi  import FastAPI, File, UploadFile , HTTPException
# from src.prompts import *
import os


from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



async def convert_java_to_python(java_code):
    prompt = f"""You are Expert in converting Java code to Python Code : \n\n {java_code}
               please convert {java_code} to python and ignore special characterstics
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],java_code])

    print(response)
    return response.text

def convert_java_to_python_1(java_code):
    prompt =[ """
    Convert the following Java code into Python:
       Convert the following Java code into Python:

    {java_code}

    Convert the above Java code logic into Python.
             
    if possible optimize the code 
    remove ``` in beginning and end
             
    also the python code should not have ``` in beginning or end and python code in output and apart from main code everything should be in comments


    """]
    model=genai.GenerativeModel('gemini-pro')
    print("******",prompt[0])
    print("---",java_code)
    response=model.generate_content([prompt[0],java_code])
    return response.text

    # if response and response.candidates:
    #     # Assuming response.candidates is a list, get the first candidate
    #     candidate = response.candidates[0]
        
    #     # Check the type of the candidate and handle accordingly
    #     if hasattr(candidate, 'text'):
    #         return candidate.text.strip()
    #     elif hasattr(candidate, 'content'):
    #         return candidate.content.strip()
    #     else:
    #         raise HTTPException(status_code=500, detail="Conversion failed: no converted code returned.")
    # else:
    #     raise HTTPException(status_code=500, detail="Conversion failed: no candidates found in response.")


    
