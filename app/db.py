from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column, String, Text,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase,relationship
import datetime


DATABASE_URL="sqlite+aiosqlite:///./test.db"

class Declarativee(DeclarativeBase):
    pass

class Post(Declarativee):
    __tablename__="posts"

    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    caption=Column(Text)
    url=Column(String,nullable=False)
    file_type=Column(String,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)

# till now we have create the table for the post 
# now we are going to create the database

engine=create_async_engine(DATABASE_URL)
async_session_maker=async_sessionmaker(engine,expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin()as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)
        # await will find all of the classes that are inheriting from the declarative base and create the tables for them in the database

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session