from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine

engine = create_engine("sqlite:///user.db", echo=False)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    auth = Column(String(5),default="admin")
    avatar=Column(String(200),default="https://pic1.zhimg.com/v2-9740d68f2961f9c1368561456654e9e7_xs.jpg")
    password = Column(String(32))

    def __repr__(self):
        return self.name

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


if __name__ == "__main__":
    Base.metadata.create_all(engine)
