from webapp.auth.models import User
from webapp import client

class Workout:
    
    dbs = client['test']
    
    collection = dbs['testworkouts']
    
    def __init__(self, title, type):
        self.title = title
        self.type = type
    
    def create_workout(self, **kwargs):
        
        self.workout = {}
        
        container = {'title': self.title, 'type': self.type}
        
        for key, val in kwargs.items():
            self.workout.update({key: val})
        
        container.update(
            {": ".join(('Circuit', (str(count)))): item for count, item in enumerate(self.workout.items())})
        
        self.collection.insert_one(container)
    
    def get_all_workouts(self):
        
        all_workouts = {}
        
        for document in self.collection.find():
            
            all_workouts.update(document)
                
        return all_workouts
    
    def get_workout_by_title(self, title):
        
        self.title = title
        
        for document in self.collection.find_one({"title"}, self.title):
            
            if not document:
                
                return 'Workout not found because title does not exist'
            
            else:
                
                return document
            
            
    def get_workout(self, _id):
        
        self._id = _id
        
        for document in self.collection.find_one({"_id": self._id}):
            
            if not document:
                
                return 'Workout not found'
            
            else:
                
                return document
        
        return document
    
    
    def delete_workout(self, _id):
        
        self._id = _id
        
        for document in self.collection.find_one({"_id": _id }):
            
            if not document:
                
                return 'Workout not found. Unable to delete'
            
            else:
                
                self.collection.delete_one(document)
                

class WorkoutList:
    
    dbs = client['test']
    
    collection = dbs['testworkouts']
    
    def __init__(self):
        self.all_workouts = []
    
    def get_all_workouts(self):
        
        for document in self.collection.find({}):
            
            self.all_workouts.append(document)
                
        return self.all_workouts
            
    
    def get_workout_by_title(self, title):
        
        self.title = title
        
        for document in self.collection.find_one({"title"}, self.title):
            
            if not document:
                
                return 'Workout not found because title does not exist'
            
            else:
                
                return document
         