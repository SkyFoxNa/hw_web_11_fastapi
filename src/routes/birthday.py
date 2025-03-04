from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import birthday as repositories_contacts
from src.schemas.birthday import BirthdayResponse


router = APIRouter(prefix = '/birthday', tags = ['birthdays'])


@router.get("/", response_model=list[BirthdayResponse])
async def get_contact_with_upcoming_birthday(
    upcoming_days: int = Query(default=7, ge=1, le=365),
    limit: int = Query(10, ge=10, le=200),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db)
):
    contacts = await repositories_contacts.get_contact_with_upcoming_birthday(
        upcoming_days, limit, offset, db
    )
    return contacts
