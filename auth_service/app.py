import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from auth_service.config.settings import Settings
from auth_service.api.v1.routers.users import user_router


settings = Settings()

app = FastAPI()


app.include_router(user_router)


@app.get('/health', status_code=status.HTTP_200_OK)
async def healthcheck():
    return JSONResponse(
        content={'status': 'OK'}, status_code=status.HTTP_200_OK
    )


def main():
    """Main function."""
    uvicorn.run('app:app', host=settings.MAIN_HOST, port=settings.MAIN_PORT)


if __name__ == '__main__':
    main()
