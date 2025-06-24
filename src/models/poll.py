from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.attributes import backref_listeners
from sqlalchemy import ForeignKey
from src.models.category import Category  # Импортируем модель категории

from src.models.base import BaseModel
from src.core.db import db


class Poll(BaseModel):  # Таблица "polls" — опросы
    __tablename__ = "polls"

    # Основные поля
    title: Mapped[str] = mapped_column(  # Заголовок опроса
        db.String(120),
        nullable=False
    )
    description: Mapped[str] = mapped_column(  # Описание (необязательное)
        db.Text,
        nullable=True
    )
    start_date: Mapped[datetime] = mapped_column(  # Дата начала
        db.DateTime,
        nullable=False
    )
    end_date: Mapped[datetime] = mapped_column(  # Дата окончания
        db.DateTime,
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(  # Активен ли опрос
        db.Boolean,
        default=True,
    )
    is_anonymous: Mapped[bool] = mapped_column(  # Анонимный ли опрос
        db.Boolean,
        default=True,
    )

    # Новое: связь с категорией
    category_id: Mapped[int] = mapped_column(  # ID категории (внешний ключ на таблицу categories)
        db.Integer,
        ForeignKey('categories.id'),
        nullable=True
    )
    category: Mapped["Category"] = relationship(  # Сам объект категории (удобно обращаться: poll.category.name)
        "Category",
        backref="polls",  # Позволяет из категории получить список опросов: category.polls
    )

    # Relations (связи с другими таблицами)

    options: Mapped[list['PollOption']] = relationship(  # Связь с вариантами ответа
        'PollOption',
        back_populates='poll',
        cascade='all, delete-orphan',
    )

    votes: Mapped[list['Vote']] = relationship(  # Связь с голосами
        'Vote',
        back_populates='poll',
        cascade='all, delete-orphan',
    )

    statistics: Mapped['PollStatistic'] = relationship(  # Связь со статистикой по опросу
        'PollStatistic',
        back_populates='poll',
        uselist=False,  # Один к одному
        cascade='all, delete-orphan',
    )


class PollOption(BaseModel):  # Таблица poll_options — варианты ответа на опрос
    __tablename__ = 'poll_options'

    poll_id: Mapped[int] = mapped_column(  # Внешний ключ на опрос
        db.Integer,
        db.ForeignKey('polls.id'),
        nullable=False
    )
    text: Mapped[str] = mapped_column(  # Текст варианта ответа
        db.String(80),
        nullable=False
    )

    # Relations

    poll: Mapped[Poll] = relationship(  # Обратная связь с Poll
        'Poll',
        back_populates='options'
    )

    votes: Mapped[list['Vote']] = relationship(  # Связь с голосами, отданными за этот вариант
        'Vote',
        back_populates='option',
    )

    statistics: Mapped['OptionStatistics'] = relationship(  # Статистика по конкретному варианту
        'OptionStatistics',
        back_populates='option',
        cascade='all, delete-orphan'
    )
