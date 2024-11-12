import httpx
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse


from auth_service.config.settings import KeycloakSettings


keycloak_settings = KeycloakSettings()


user_router = APIRouter(
    prefix='/users',
    tags=['User'],
    responses={404: {'description': 'Not found'}}
)


@user_router.get(
        '/register', status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )
async def register_user() -> RedirectResponse:
    """Register a new user."""

    url = (
        f'{keycloak_settings.KEYCLOAK_URL}'
        f'?client_id={keycloak_settings.CLIENT_ID}'
        f'&response_type=code&scope=openid'
        f'&redirect_uri={keycloak_settings.REDIRECT_URI}'
    )
    return RedirectResponse(url=url)


@user_router.get('/callback', status_code=status.HTTP_200_OK)
async def callback(request: Request) -> JSONResponse:
    """Callback from keycloak."""

    code = request.query_params.get('code')

    if code is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Нет данных для авторизации'
        )
    async with httpx.AsyncClient() as client:
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': keycloak_settings.CLIENT_ID,
            'client_secret': keycloak_settings.CLIENT_SECRET,
            'redirect_uri': keycloak_settings.REDIRECT_URI
        }
        try:
            keycloak_token = await client.post(
                keycloak_settings.KEYCLOAK_TOKEN_URL, data=data
                )
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=keycloak_token.status_code,
                detail=str(exc)
            )
    if keycloak_token.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Ошибка получения токена'
        )

    return JSONResponse(content=keycloak_token.json())
