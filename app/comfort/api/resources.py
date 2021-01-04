from os import path 
import csv
from flask import request, Blueprint, current_app
from flask_restful import Api, Resource
from .schemas import SatisfactionIndicatorSchema, SatisfactionUniqueSchema
from ..models import SatisfactionIndicator
from app.common.error_handling import ObjectNotFound, IntegretyValueError

comfort_v1 = Blueprint('comfort_v1', __name__)
comfort_schema = SatisfactionIndicatorSchema()
unq_comfort_schema = SatisfactionUniqueSchema()

api = Api(comfort_v1)

class SatisfactionListResource(Resource):
    def get(self):
        satisfaction = SatisfactionIndicator.get_all()
        result = comfort_schema.dump(satisfaction, many=True)
        return result

    def post(self):
        data = request.get_json()
        satisfaction_dict = comfort_schema.load(data)
        satisfaction = SatisfactionIndicator(
                country_code = satisfaction_dict['country_code'], 
                country = satisfaction_dict['country'], 
                indicator_code = satisfaction_dict['indicator_code'], 
                indicator = satisfaction_dict['indicator'], 
                mesasure_code = satisfaction_dict['mesasure_code'], 
                mesasure = satisfaction_dict['mesasure'], 
                inequality_code = satisfaction_dict['inequality_code'], 
                inequality = satisfaction_dict['inequality'], 
                unit_code = satisfaction_dict['unit_code'], 
                unit = satisfaction_dict['unit'], 
                power_code_ref = satisfaction_dict['power_code_ref'], 
                power_code = satisfaction_dict['power_code'], 
                reference_period_code = satisfaction_dict['reference_period_code'], 
                reference_period = satisfaction_dict['reference_period'], 
                value = satisfaction_dict['value'],         
                flag_code = satisfaction_dict['flag_code'], 
                flag = satisfaction_dict['flag'], 
        )

        satisfaction.save()
        resp = comfort_schema.dump(satisfaction)

        return resp, 201

class SatisfactionFilterResource(Resource):
    def get(self, value, indicator_code='SW_LIFS'):
        if not value.isnumeric():
            raise IntegretyValueError('Invalid value for indicator')
        satisfaction = SatisfactionIndicator.filter_indicator(indicator_code, value)
        result = comfort_schema.dump(satisfaction, many=True)
        return result

class SatisfactionUniqueResource(Resource):
    def get(self):
        satisfaction = SatisfactionIndicator.unique_indicator()
        result = unq_comfort_schema.dump(satisfaction, many=True)
        return result


class SatisfactionResource(Resource):
    def get(self, satisfaction_indicator_id):
        satisfaction = SatisfactionIndicator.get_by_id(satisfaction_indicator_id)
        if satisfaction is None:
            raise ObjectNotFound('Indicator not found')
        
        resp = comfort_schema.dump(satisfaction)
        return resp


class SatisfactionPreloaderResource(Resource):
    def post(self):
        current_app.logger.info('Inserting infor in the recorded data_set')
        required_fields = ['country_code','country','indicator_code','indicator','mesasure_code','mesasure','inequality_code','inequality','unit_code','unit','power_code_ref','power_code','reference_period_code','reference_period','value','flag_code','flag' ]
        values_to_insert = []
        satisfaction = SatisfactionIndicator.get_all()
        count = 0
        csv_file = path.join(current_app.instance_path.replace('instance','files'),'data.csv' )
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)

            for row in data:
                satisfaction_dict = {required_fields[x]:row[x] for x in range(len(row))}    
                values_to_insert.append(satisfaction_dict)

        for indicator in  values_to_insert:
            count += 1
            satisfaction_dict = comfort_schema.load(indicator)
            satisfaction = SatisfactionIndicator(
                country_code = satisfaction_dict['country_code'], 
                country = satisfaction_dict['country'], 
                indicator_code = satisfaction_dict['indicator_code'], 
                indicator = satisfaction_dict['indicator'], 
                mesasure_code = satisfaction_dict['mesasure_code'], 
                mesasure = satisfaction_dict['mesasure'], 
                inequality_code = satisfaction_dict['inequality_code'], 
                inequality = satisfaction_dict['inequality'], 
                unit_code = satisfaction_dict['unit_code'], 
                unit = satisfaction_dict['unit'], 
                power_code_ref = satisfaction_dict['power_code_ref'], 
                power_code = satisfaction_dict['power_code'], 
                reference_period_code = satisfaction_dict['reference_period_code'], 
                reference_period = satisfaction_dict['reference_period'], 
                value = satisfaction_dict['value'],         
                flag_code = satisfaction_dict['flag_code'], 
                flag = satisfaction_dict['flag'], 
            )
            satisfaction.add()

            if count % 500 == 0:
                current_app.logger.info('rows added => {} '.format(count,))
        try:
            satisfaction.commit()
        except Exception as e:
            current_app.logger.info('error at loading the dataset => {} '.format(str(e),))
            
        return {'msg':'data loaded'},201


api.add_resource(SatisfactionFilterResource, '/api/v1/satisfaction/filter/<string:value>/<string:indicator_code>', endpoint='filter')
api.add_resource(SatisfactionFilterResource, '/api/v1/satisfaction/filter/<string:value>', endpoint='filter_default')
api.add_resource(SatisfactionUniqueResource, '/api/v1/satisfaction/unique/', endpoint='satisfaction_unique')
api.add_resource(SatisfactionPreloaderResource, '/api/v1/preload_data/', endpoint='preload_data')
api.add_resource(SatisfactionListResource, '/api/v1/satisfaction/', endpoint='satisfcation_list_resource')
api.add_resource(SatisfactionResource, '/api/v1/satisfaction/<int:satisfaction_indicator_id>', endpoint='satisfcation_resource')


