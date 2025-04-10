from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 建立資料庫引擎與基底
DATABASE_URI = 'sqlite:///../database/church.db'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()


# 定義資料表
class ChurchMember(Base):
    __tablename__ = 'church_members'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    role = Column(String, nullable=False)


# 建立資料表
if __name__ == '__main__':
    Base.metadata.create_all(engine)
