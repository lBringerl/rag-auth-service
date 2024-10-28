from fastapi import APIRouter, status  # HTTPException,
from fastapi.responses import RedirectResponse

from auth_service.config.settings import KeycloakSettings


keycloak_settings = KeycloakSettings()


user_router = APIRouter(
    prefix='/users',
    tags=['User'],
    responses={404: {'description': 'Not found'}}
)


@user_router.get(
        '/register', status_code=status.HTTP_200_OK
    )
async def register_user() -> RedirectResponse:
    url = (
        f'{keycloak_settings.KEYCLOAK_URL}'
        f'?client_id={keycloak_settings.KEYCLOAK_CLIENT_ID}'
        f'&response_type=code&scope=openid'
        f'&redirect_uri={keycloak_settings.KEYCLOAK_REDIRECT_URI}'
    )
    return RedirectResponse(url=url)
