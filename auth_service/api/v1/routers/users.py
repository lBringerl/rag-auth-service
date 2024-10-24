from fastapi import APIRouter, status  # HTTPException,

from auth_service.models.config.users import User


user_router = APIRouter(
    prefix='/users',
    tags=['User'],
    responses={404: {'description': 'Not found'}}
)


@user_router.post(
        '/register', response_model=User, status_code=status.HTTP_201_CREATED
    )
async def create_user(user: User) -> User:
    return user
