from sqlalchemy import Column, Integer, SmallInteger, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    brand = Column(String, nullable=False)
    year = Column(String, nullable=False)
    km_driven = Column(Integer, nullable=False)
    no_of_owners = Column(SmallInteger, nullable=False)
    address = Column(String, nullable=False)
    main_pic = Column(String, nullable=False)
    pic0 = Column(String)
    pic1 = Column(String)
    pic2 = Column(String)
    pic3 = Column(String)
    pic4 = Column(String)
    pic5 = Column(String)
    pic6 = Column(String)
    pic7 = Column(String)
    pic8 = Column(String)
    pic9 = Column(String)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone_primary = Column(String, nullable=True, unique=True)
    phone_secondary = Column(String, nullable=True, unique=True)
    email_verified = Column(Boolean, nullable=False, server_default=text("false"))
    name = Column(String, nullable=True, unique=False)
    about = Column(String, nullable=True, unique=False)
    profile_pic = Column(String, nullable=True, unique=False)
    is_blocked = Column(Boolean, nullable=False, server_default=text("false"))
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    credits = Column(Integer, nullable=False, server_default=text("1000"))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    post_id = Column(
        Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True
    )
