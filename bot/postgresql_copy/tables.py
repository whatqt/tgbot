from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, BigInteger, String
from dotenv import load_dotenv
import os



load_dotenv()
# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
engine = create_async_engine(
    f"postgresql+asyncpg://postgres:{os.getenv("PASSWORD_POSTGRES")}@localhost/tg_bot",
    echo=True
)

class Base(DeclarativeBase): pass
# скорее всего разные базовые классы будут создавать только те таблиы, к которые они имеют отношения
# проверить это на всякий случай и так же проверить с операциями CRUD

class Users(Base):
    __tablename__ = "users"

    id_user = Column(BigInteger, primary_key=True)
    user_name = Column(String)
    id_group = Column(String)



