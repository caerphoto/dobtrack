"""The application's model objects"""
from dobtrack.model.meta import Session, Base

from dobtrack.model.item import Item

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
