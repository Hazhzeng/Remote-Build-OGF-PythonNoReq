import logging

import azure.functions as func
from dataclasses import dataclass

@dataclass
class awesome:
    version: float = 37

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
         f"HttpTrigger{awesome().version}",
         status_code=200
    )
