from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr  # Pydantic validates email format before the route handler runs
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"  # standard OAuth2 token type — defaulted so clients always receive it
