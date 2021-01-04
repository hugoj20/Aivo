from marshmallow import fields
from app.ext import ma

class SatisfactionIndicatorSchema(ma.Schema):
    satisfaction_indicator_id = fields.Integer(dump_only=True)
    country_code = fields.String(required=True) 
    country = fields.String() 
    indicator_code = fields.String() 
    indicator = fields.String() 
    mesasure_code = fields.String() 
    mesasure = fields.String() 
    inequality_code = fields.String() 
    inequality = fields.String() 
    unit_code = fields.String() 
    unit = fields.String() 
    power_code_ref = fields.String() 
    power_code = fields.String() 
    reference_period_code = fields.String() 
    reference_period = fields.String() 
    value = fields.String()         
    flag_code = fields.String() 
    flag = fields.String() 

class SatisfactionUniqueSchema(ma.Schema):
    indicator_code = fields.String() 
    indicator = fields.String() 