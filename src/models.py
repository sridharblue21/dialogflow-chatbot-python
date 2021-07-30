from sqlalchemy import Column, Integer, String, DateTime, text, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class PreRegistration(Base):
    __tablename__ = "preregistration"

    pre_registration_id = Column(Integer, primary_key=True)
    email=Column(String,nullable=False)
    title = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    gender = Column(String, nullable=False)
    dob = Column(DateTime, nullable=False)
    nationality = Column(String, nullable=False)
    