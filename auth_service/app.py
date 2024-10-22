import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from auth_service.config.settings import Settings


settings = Settings()

app = FastAPI()


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
