from typing import Any
from .database import session, User
from sqlalchemy import select

def check_have_phone(id_telegram: int) -> bool:
    smtp  = select(User).where(User.id_telegram == id_telegram)
    try:
        session.scalars(smtp).one()
        return True
    except Exception:
        return False

def insert_user(user_id: int, first_name: str, last_name: str, phone_number: str, vcard: Any) -> bool:
    user = User(
        id_telegram=user_id,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        vcard=vcard
    )
    try:
        session.add(user)
        session.commit()
        return True
    except:
        session.rollback()
        return False
