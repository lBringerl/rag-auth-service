from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the app."""

    MAIN_HOST: str = '0.0.0.0'
    MAIN_POR: int = 8000

    class Config:
        env_file = '.env'


class KeycloakSettings(BaseSettings):
    """Settings for the keycloak."""

    KEYCLOAK_REALM: str = 'RAGOps_authh_service'
    KEYCLOAK_CLIENT_ID: str = 'myclient'
    KEYCLOAK_REDIRECT_URI: str = 'http://localhost:8000/callback'
    CLIENT_SECRET: str = 'emfy67UgJnpRfgB9KEPOt0DDS6hRgQSs'

    # URL для авторизации
    @property
    def KEYCLOAK_URL(self):
        return (
            f'http://localhost:8080/realms/{self.KEYCLOAK_REALM}/'
            'protocol/openid-connect/auth'
        )

    @property
    def KEYCLOAK_TOKEN_URL(self):
        return (
            f'http://localhost:8080/realms/{self.KEYCLOAK_REALM}/'
            'protocol/openid-connect/token'
        )

    class Config:
        env_file = '.env'
