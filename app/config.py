from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_hostname: str
    db_port: str
    db_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: str

    def get_db_url(self):
        db_url: str = f"postgresql://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_name}"
        return db_url

    class Config:
        env_file = ".env"


settings = Settings()
