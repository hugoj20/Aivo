from app.db import db, BaseModelMixin
from datetime import datetime
from sqlalchemy import Index



class SatisfactionIndicator(db.Model, BaseModelMixin):
    satisfaction_indicator_id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(3))
    country = db.Column(db.String(75))
    indicator_code = db.Column(db.String(20))
    indicator = db.Column(db.String(75))
    mesasure_code = db.Column(db.String(20))
    mesasure = db.Column(db.String(75))
    inequality_code = db.Column(db.String(20))
    inequality = db.Column(db.String(75))
    unit_code = db.Column(db.String(20))
    unit = db.Column(db.String(75))
    power_code_ref = db.Column(db.String(20))
    power_code = db.Column(db.String(75))
    reference_period_code = db.Column(db.String(20))
    reference_period = db.Column(db.String(75))
    value = db.Column(db.String(100))
    flag_code = db.Column(db.String(20))
    flag = db.Column(db.String(75))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    __table_args__ = (Index('country_indicator_code_idx', 'country_code', 'indicator_code','inequality_code'),db.UniqueConstraint('country_code', 'indicator_code','inequality_code'), )

    def __repr__(self):
        return f'SatisfactionIndicator({self.indicator})'

    def __str__(self):
        return f'{self.indicator}'