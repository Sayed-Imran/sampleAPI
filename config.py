from pydantic_settings import BaseSettings


class _APIKey(BaseSettings):
    unsplash_access_key: str = "3pw90nMVGtYg1rzFe3tQisIvdgLBxpi8nEq1KkKNlmM"

API_Key = _APIKey()