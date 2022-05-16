from models import Base, engine, User
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

with Session(engine)as session:
    a = User(name="admin", password="111111")
    session.add(a)
    session.commit()
