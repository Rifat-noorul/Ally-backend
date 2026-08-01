from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from database import Base
import datetime
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, index=True)
    phone = Column(String, unique=True, index=True)
    kyc_status = Column(String, default="pending")
    trust_tier = Column(String, default="bronze")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class HelperProfile(Base):
    __tablename__ = "helper_profiles"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, index=True)  # FK in a real DB
    tier = Column(String, default="bronze")
    rating_avg = Column(Float, default=0.0)
    night_squad_opt_in = Column(Boolean, default=False)
    verified_at = Column(DateTime, nullable=True)

class SosEvent(Base):
    __tablename__ = "sos_events"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, index=True)  # FK
    status = Column(String, default="active") # active, resolved
    lat = Column(Float)
    lng = Column(Float)
    trigger_type = Column(String) # stealth, button, fake_call
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    audio_recording_url = Column(String, nullable=True)
