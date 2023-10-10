from fastapi import FastAPI
app=FastAPI()



@app.get("/")
async def hello_func():
    return "Hello word"



if __name__=="__main__":
    import uvicorn
    uvicorn.run(app ,port=8000, host="localhost" )