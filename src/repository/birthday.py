from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta

from src.entity.models import Contact


async def get_contact_with_upcoming_birthday(upcoming_days: int, limit: int, offset: int, db: AsyncSession,
                                             future_date=None):
    current_date = datetime.now().date()
    future_date = current_date + timedelta(days = upcoming_days)

    data = select(Contact).filter(Contact.birthday.between(current_date, future_date)).offset(offset).limit(limit)

    contacts = await db.execute(data)
    return contacts.scalars().all()
