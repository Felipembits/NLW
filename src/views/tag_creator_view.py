from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse



class TagCreatorView:
    
    # Responsabilidade para interagir com HTTP
    
    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        # Lógica de regra de negócio

        # Retorno de HTTP

        return HttpResponse(status_code=200, body={"hello": "world"})