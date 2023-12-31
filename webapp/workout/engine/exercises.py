from webapp import client
import random

class Exercise:
    
    """Access the categories collection of exercises to render lists of exercises for the user
    to choose from when constructing circuits. The exercises are organized by the general
    target region and relative movement vectors of the exercise.
    """
    
    def __init__(self):
        
        self.categories = []
        
        self.dbs = client["workouts"]
        
        self.exercise_collection = self.dbs['categories']
        
        for i in self.exercise_collection.find():
            
            self.categories.append(i)
         
    
    def get_exercises_byId(self, _id):
        
        exercise_dict = {}
        
        for e in self.exercise_collection.find({'_id': _id}, {'_id': False}):
            
            exercise_dict.update(e)
            
        return exercise_dict['exercises']
    
    
    # Get the categorically separated lists of exercises
    def get_core_exercises(self):
        
        return self.categories[0]['exercises']
    
        
    def get_lower_gluteham(self):
        
        return self.categories[1]['exercises']
    
    
    def get_lower_quad(self):
        
        return self.categories[2]['exercises']
    
    
    def get_total_body(self):
        
        return self.categories[3]['exercises']
    
    
    def get_upper_pull(self):
        
        return self.categories[4]['exercises']
    
    
    def get_upper_push(self):
        
        return self.categories[5]['exercises']
    
    
    # Get the category ids of each region
    def get_core_id(self):
        return self.categories[0]['_id']
    
    
    def get_gluteham_id(self):
        return self.categories[1]['_id']
    
    
    def get_quad_id(self):
        return self.categories[2]['_id']
    
    
    def get_totalbody_id(self):
        return self.categories[3]['_id']
    
    
    def get_upperpull_id(self):
        return self.categories[4]['_id']
    
    
    def get_upperpush_id(self):
        return self.categories[5]['_id']
    
    
    # generate pseudo-randomly selected list of exercises by category
    def randomize_selection(self):
        
        i = [0, 1, 2, 3, 4, 5]
        
        r = random.choice(i)
        
        return self.categories[r]['exercises']
    
        
        


