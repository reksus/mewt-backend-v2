from .main import app

# create handler for creating a lambda package 
# that will be linked to aws_lambda target
from mangum import Mangum
def handler(event, context=None):
    asgi_handler = Mangum(app=app)
    response = asgi_handler(event, context)
    return response

