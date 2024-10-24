import pydantic
import enum


class UserRole(str, enum.Enum):
    """Possible user roles"""

    Admin = 'Admin'
    DataScientist = 'DataScientist'
    User = 'User'


class User(pydantic.BaseModel):
    """User model"""

    email: pydantic.EmailStr
    password: pydantic.SecretStr
    role: UserRole

    class Config:
        schema_extra = {
            'example': {
                'email': 'uVHrN@example.com',
                'password': 'password',
                'roll': 'DataScientist'
            },
        }
