from __future__ import annotations
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.models.category import Category

from src.models.base import BaseModel
from src.core.db import db


class Poll(BaseModel):
    __tablename__ = "polls"

    title: Mapped[str] = mapped_column(
        db.String(120),
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        db.Text,
        nullable=True
    )
    start_date: Mapped[datetime] = mapped_column(
        db.DateTime,
        nullable=False
    )
    end_date: Mapped[datetime] = mapped_column(
        db.DateTime,
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        db.Boolean,
        default=True,
    )
    is_anonymous: Mapped[bool] = mapped_column(
        db.Boolean,
        default=True,
    )

    category_id: Mapped[int] = mapped_column(
        db.Integer,
        ForeignKey('categories.id'),
        nullable=True
    )
    category: Mapped['Category'] = relationship(
        'Category',
        backref='polls',
    )

    options: Mapped[list['PollOption']] = relationship(
        'PollOption',
        back_populates='poll',
        cascade='all, delete-orphan',
    )

    votes: Mapped[list['Vote']] = relationship(
        'Vote',
        back_populates='poll',
        cascade='all, delete-orphan',
    )

    poll_stats: Mapped['PollStatistics'] = relationship(
        'PollStatistics',
        back_populates='poll',
        uselist=False
    )


class PollOption(BaseModel):
    __tablename__ = 'poll_options'

    poll_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('polls.id'),
        nullable=False
    )
    text: Mapped[str] = mapped_column(
        db.String(80),
        nullable=False
    )

    poll: Mapped['Poll'] = relationship(
        'Poll',
        back_populates='options'
    )

    votes: Mapped[list['Vote']] = relationship(
        'Vote',
        back_populates='option',
    )

    statistics: Mapped['OptionStatistics'] = relationship(
        'OptionStatistics',
        back_populates='option',
        cascade='all, delete-orphan'
    )
