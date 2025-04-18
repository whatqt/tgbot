from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from dotenv import load_dotenv
import os



load_dotenv()
engine = create_async_engine(
    f"postgresql+asyncpg://postgres:{os.getenv("PASSWORD_POSTGRES")}@localhost/tg_bot",
    echo=False
)

class Base(DeclarativeBase): pass

class Users(Base):
    __tablename__ = "users"

    id_user = Column(BigInteger, primary_key=True)
    user_name = Column(String)
    id_group = Column(String)

class SendMessTime(Base):
    __tablename__ = "send_mess_time"
    id_user = Column(BigInteger, primary_key=True)
    time_set = Column(TIMESTAMP)


