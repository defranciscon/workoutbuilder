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
                
        