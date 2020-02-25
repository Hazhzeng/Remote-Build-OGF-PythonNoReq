import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    if (name := req.params.get('name')) is not None:
        return func.HttpResponse(f"HttpTrigger38!")
    else:
        return func.HttpResponse(
             "HttpTrigger38",
             status_code=200
        )
