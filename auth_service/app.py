import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from auth_service.config.constants import MAIN_HOST, MAIN_PORT


app = FastAPI()


@app.get('/health', status_code=status.HTTP_200_OK)
async def healthcheck():
    return JSONResponse(
        content={'status': 'OK'}, status_code=status.HTTP_200_OK
    )


def main():
    uvicorn.run('app:app', host=MAIN_HOST, port=MAIN_PORT)


if __name__ == '__main__':
    main()
