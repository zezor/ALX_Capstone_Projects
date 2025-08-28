# accounts/utils.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            "error": True,
            "errors": response.data,
            "status_code": response.status_code
        }
        return Response(custom_response, status=response.status_code)

    # Handle unexpected errors
    return Response({
        "error": True,
        "errors": str(exc),
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
