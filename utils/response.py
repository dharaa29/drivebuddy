def success_response(message: str, data: dict):
    return {
        "success": True,
        "message": message,
        "data": data
    }

def validation_error(errors: dict):
    return {
        "success": False,
        "message": "Validation error",
        "errors": errors
    }

def server_error():
    return {
        "success": False,
        "message": "Internal Server Error. Please try again later."
    }
