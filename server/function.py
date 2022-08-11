def check_have_phone(id_telegram: int) -> bool:
    smtp  = select(User).where(User.id_telegram == id_telegram)
    try:
        print(session.scalars(smtp).one())
        return True
    except Exception:
        print('Could not find user')
        return False