import datetime
from flask import Response, abort, current_app, jsonify, request, json
from flask_restful import Resource, fields, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity
from webapp.auth.models import User
from webapp import client

dbs = client['test']
collection = dbs['testworkouts']

class WorkoutApi(Resource):
    @jwt_required
    def get(self, id=None):
        
        if not id:
            workout= []
            workouts = collection.find()
            for w in workouts:
                workout.append(w)
        
        else:
            
            workout = collection.find_one({'_id': id})
            
            if not workout:
                
                abort(404)
            
            else:
            
                return jsonify(workout)
                
                
    def post(self):
        data = request.json
        
        response = collection.insert_one(data)
        
        return jsonify(response)
        

    def put(self, id, **kwargs):
        
        for key, val in kwargs.items():
            response = collection.update_one(filter={'_id': id}, update={key: val})
            
        return jsonify(response)
    
    
    def delete(self, id):
        response = collection.update_one(filter={'_id': id})
        
        if response:
            
            return jsonify({'response': 'Success'})
    
    