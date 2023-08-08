from pydantic_settings import BaseSettings


class _APIKey(BaseSettings):
    unsplash_access_key: str

API_Key = _APIKey()