from typing import List

from sqlalchemy import Column, ForeignKey, Integer, Text, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(Text, nullable=False)
    full_name = mapped_column(Text, nullable=False)
    password = mapped_column(Text, nullable=False)
    role = mapped_column(Text, nullable=False, server_default=text("' '"))

    Note: Mapped[List['Note']] = relationship('Note', uselist=True, back_populates='Users_')


class Note(Base):
    __tablename__ = 'Note'

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(Text, nullable=False)
    author = mapped_column(ForeignKey('Users.id'), nullable=False)
    created_at = mapped_column(Text, nullable=False)
    content = mapped_column(Text, nullable=False)
    updated_at = mapped_column(Text)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Note')
