"""FastAPI WebApp

Returns:
    _type_: _description_
"""
from fastapi import FastAPI

app = FastAPI(version='0.0.0',
              title='FastAPI based WebApp!',
              description='Step by step walk through to building a Python web app!',
              contact={'GitHub': 'https://github.com/rich-sykes'},
              docs_url=None,
              redoc_url='/',
              )


@app.get("/get-request/{name}")
async def root(name: str = 'Richard') -> dict:
    """A get requeest with a query parameter

    Args:
        name (str, optional): A string value, a name for example. Defaults to 'Rich'.

    Returns:
        dict: A personalised message in a dict.
    """
    return {"message": f"Hello {name}"}
