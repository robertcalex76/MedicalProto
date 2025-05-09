from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NursingHome(Base):
    __tablename__ = 'nursing_homes'

    id = Column(Integer, primary_key=True, index=True)
    provider_name = Column(String, index=True)
    address = Column(String)
    rating = Column(Float)
    staffing = Column(Integer)
    violations = Column(Integer)

    def __repr__(self):
        return f"<NursingHome(provider_name={self.provider_name}, address={self.address}, rating={self.rating})>"