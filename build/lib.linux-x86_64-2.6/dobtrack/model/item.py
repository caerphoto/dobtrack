"""DOB Item model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, Boolean

from dobtrack.model.meta import Base

class Item(Base):
    __tablename__ = "dobitems"

    rep = Column(Integer, primary_key=True)
    initials = Column(String(3))
    datein = Column(String(20))
    kind = Column(String(3))
    customer = Column(String(30))
    fujitsuowned = Column(Boolean)
    value = Column(Integer) # will be divided by 10 when displayed
    costcentre = Column(String(20))
    ordernum = Column(String(20))
    make = Column(String(30))
    model = Column(String(50))
    part = Column(String(30))
    serial = Column(String(30))
    asset = Column(String(30))
    warranty = Column(String(20))
    issue = Column(String(300))
    state = Column(String(300))
    location = Column(String(300))
    solution = Column(String(300))
    grn = Column(String(8))
    sap = Column(String(8))
    rtsdate = Column(String(20))
    folio = Column(Integer)
    comment = Column(String(300))

    def __init__(self, rep=0, initials='', datein='', kind='DOB', customer='',
                 fujitsuowned=False, value=0, costcentre='', ordernum='', make='',
                 model='', part='', serial='', asset='', warranty='', issue='',
                 state='', location='', solution='', grn='', sap='',
                 rtsdate='', folio=0, comment=''):
        self.rep = rep
        self.initials = initials
        self.datein = datein
        self.kind = kind
        self.customer = customer
        self.fujitsuowned = fujitsuowned
        self.value = value
        self.costcentre = costcentre
        self.ordernum = ordernum
        self.make = make
        self.model = model
        self.part = part
        self.serial = serial
        self.asset = asset
        self.warranty = warranty
        self.issue = issue
        self.state = state
        self.location = location
        self.solution = solution
        self.grn = grn
        self.sap = sap
        self.rtsdate = rtsdate
        self.folio = folio
        self.comment = comment

    def __repr__(self):
        result = '{'
        result += '"rep": "%s", ' % self.rep
        result += '"initials": "%s"' % self.initials
        result += '"datein": "%s"' % self.datein
        result += '"kind": "%s"' % self.kind
        result += '"customer": "%s", ' % self.customer
        result += '"value": "%s", ' % self.value
        result += '"costcentre": "%s", ' % self.costcentre
        result += '"make": "%s", ' % self.make
        result += '"model": "%s", ' % self.model
        result += '"part": "%s", ' % self.part
        result += '"serial": "%s", ' % self.serial
        result += '"asset": "%s", ' % self.asset
        result += '"warranty": "%s", ' % self.warranty
        result += '"location": "%s", ' % self.location
        result += '"issue": "%s", ' % self.issue
        result += '"state": "%s", ' % self.state
        result += '"solution": "%s", ' % self.solution
        result += '"grn": "%s", ' % self.grn
        result += '"sap": "%s", ' % self.sap
        result += '"rtsdate": "%s", ' % self.rtsdate
        result += '"folio": "%s"' % self.folio
        result += '"comment": "%s"' % self.comment
        result += '}'

        return result