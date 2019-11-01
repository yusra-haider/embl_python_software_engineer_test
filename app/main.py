from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from .database import session

# creating the FastAPI app
app = FastAPI()


# this is so far the best way to override the status code
# for validation errors:
# https://github.com/tiangolo/fastapi/issues/643#issuecomment-548139778
# unfortunately this doesn't get reflected in the auto generated docs
# and the only way to do so would be to define and raise custom exceptions
# which would defeat the purpose of built-in validations
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400, content={"detail": exc.errors()}
    )


from . import views