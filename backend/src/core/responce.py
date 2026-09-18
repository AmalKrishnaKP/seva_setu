from typing import Any

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def success_response(message: str, data: Any , status_code: int = status.HTTP_200_OK) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "status": status_code,
            "message": message,
            "data": jsonable_encoder(data),
        },
    )


def error_response(message: Any, status_code: Any, data: Any = None) -> HTTPException:
    if isinstance(message, int) and not isinstance(status_code, int):
        message, status_code = status_code, message
    raise HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "status": status_code,
            "message": message,
            "data": jsonable_encoder(data),
        },
    )