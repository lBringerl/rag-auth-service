import uvicorn
from fastapi import FastAPI, status

from auth_service.packages.config.constants import MAIN_HOST, MAIN_PORT


app = FastAPI()


@app.get("/health", status_code=status.HTTP_200_OK)
async def healthcheck():
    return {'status': 'ok'}


def main():
    uvicorn.run('app:app', host=MAIN_HOST, port=MAIN_PORT)


if __name__ == "__main__":
    main()
