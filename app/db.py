from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModelMixin:

    def save(self):
        db.session.add(self)

    def add(self):
        db.session.add(self)

    def commit(self):
        db.session.commit()

    
    def delete(self):
        db.session.delete(self) 
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    #delete if not necessary
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()    
        
    @classmethod
    def unique_indicator(cls):
        return cls.query.with_entities(cls.indicator_code, cls.indicator).distinct()

    @classmethod
    def filter_indicator(cls, indicator_code, value):
        return cls.query.filter(cls.indicator_code == indicator_code, cls.value > value ).order_by(cls.value.desc()).all()