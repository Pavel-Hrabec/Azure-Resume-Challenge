import azure.functions as func
import logging


# Define an http trigger which accepts ?value=<int> query parameter
# Double the value and return the result in HttpResponse

def double(value: int) -> int:
  return value * 2

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Executing second_function.')

    initial_value: int = int(req.params.get('value'))
    doubled_value: int = double(initial_value)

    return func.HttpResponse(
      body=f"{initial_value} * 2 = {doubled_value}",
      status_code=200
    )