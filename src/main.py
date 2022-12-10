from fastapi import FastAPI

app = FastAPI(version='0.0.0',
              title='FastAPI based WebApp!',
              description='Step by step walk through to building a Python web app!',
              contact={'GitHub': 'https://github.com/rich-sykes'},
              docs_url=None,
              redoc_url='/',
              )


@app.get("/")
async def root():
    return {"message": "Hello World"}