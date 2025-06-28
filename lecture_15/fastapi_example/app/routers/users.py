from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.models.user import UserInfo
from app.models.user import CreateUserRequest
from app.models.user import CreateUserResponse
from app.services.db_service import DBService
from app.services.db_service import get_db_service


users_router = APIRouter()


@users_router.get("/users/", tags=["users"])
async def get_users(db_service: DBService = Depends(get_db_service)) -> list[UserInfo]:
    return await db_service.get_users()


@users_router.post(
    "/users/",
    tags=["users"],
    response_model=CreateUserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new user to the database",
)
async def add_user(
    request_user: CreateUserRequest, db_service: DBService = Depends(get_db_service)
):
    """
    Adds a new user to the database with the provided username and password.
    """
    try:
        await db_service.add_user(
            username=request_user.username, password=request_user.password
        )
        return CreateUserResponse(message="User has been added successfully.")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not add user: {e}",
        )
