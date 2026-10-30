
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def home(request):
    return Response(
        {
            "message": "Welcome to CSC 325!",
            "status": "CI/CD Pipeline Successful",
            # The response confirms successful CI/CD deployment.
        }
    )


@api_view(["GET"])
def about(request):
    return Response(
        {
            "course": "CSC 325",
            "description": "Continuous Integration and Continuous Delivery (CI/CD).",
        }
    )
