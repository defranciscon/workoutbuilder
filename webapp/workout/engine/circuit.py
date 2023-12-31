
class Circuit(dict):
    
    # STRUCTURE defines options for the number of circuit groups and the number of exercises in each circuit
    STRUCTURE = {
    'SS'  : {'style': 'Superset'  , 'size': 2 },
    'TS'  : {'style': 'Triset'    , 'size': 3 },
    'QS'  : {'style': 'Quadset'   , 'size': 4 },
    'SEQ' : {'style': 'Sequential', 'size': 'NONE'},
    }


    # blocks are defined for EDT style workouts only
    BLOCK = {
        '4 min': 4,
        '5 min': 5,
        '6 min': 6,
        '7 min': 7,
        '8 min': 8,
        'NONE' : 'NONE'
        }
    

    # reps are defined for EDT style workouts only
    REPS = {
        '6 reps' :  6, 
        '8 reps' :  8, 
        '10 reps': 10,
        '12 reps': 12,
        'NONE'   : 'NONE'
        }
    

    # Interval definitions for the primary key.
    # values will be used to render the interval timer function
    INTERVAL = {
        '20:10' : {'work': 20, 'rest': 10},
        '30:15' : {'work': 30, 'rest': 15},
        '40:20' : {'work': 40, 'rest': 20},
        '45:15' : {'work': 45, 'rest': 15},
        '50:10' : {'work': 50, 'rest': 10},
        'NONE'  : {'work': 'NONE', 'rest': 'NONE'}
    }
    

    # options for performing a number of sets per circuit within the bounded parameters
    ROUNDS = {
        '2 rounds' : 2 , 
        '4 rounds' : 4 , 
        '6 rounds' : 6 ,
        'NONE'  : 'NONE'
        }

    
    # default parameters for the circuit engine
    default = {
        
        'structure':    STRUCTURE['SS'],
        'block':        BLOCK['NONE'],
        'reps':         REPS['NONE'],
        'interval':     INTERVAL['20:10'],
        'rounds':       ROUNDS['4 rounds'],
        
    }
    
    def __init__(self, **kwargs):
        self.options = {**Circuit.default, **kwargs}
        self.structure = {**Circuit.STRUCTURE}
        self.block = {**Circuit.BLOCK}
        self.reps = {**Circuit.REPS}
        self.interval = {**Circuit.INTERVAL}
        self.rounds = {**Circuit.ROUNDS}
        
        self.exercises = []
    
    
    def get_value(self, key):
        
        return self.options[key]
    
    
    def set_value(self, key, value):
        
        self.options[key] = value
    
    
    def get_all_items(self):
        
        return self.options.items()
    
    
    def store_exercises(self, *exercises):
        
        for e in exercises:
            
            self.exercises.append(e)
        
        self.options.update({'exercises': self.exercises})
        
        return self.options['exercises']
    
    
    def _create_supersets(self):
        
        self.options['structure'] = self.structure['SS']
        
        current = 0
        next = 2
        new_list = [self.exercises[current:next]]
        length = len(self.exercises) - 2
        
        while next <= length:
            current = next
            next += 2
            new_list.append(self.exercises[current:next])
            
            if next > length:
                
                return new_list
            
        
    
    def _create_trisets(self):
        
        self.options['structure'] = self.structure['TS']
        current = 0
        next = 3
        new_list = [self.exercises[current:next]]
        length = len(self.exercises) - 3
        
        while next <= length:
            current = next
            next += 3
            new_list.append(self.exercises[current:next])
            
            if next > length:
                
                return new_list
    
    
    def _create_quadsets(self):
        
        self.options['structure'] = self.structure['QS']
        
        current = 0
        next = 4
        new_list = [self.exercises[current:next]]
        length = len(self.exercises) - 3
        
        while next <= length:
            current = next
            next += 4
            new_list.append(self.exercises[current:next])
            
            if next > length:
                
                return new_list
    
    
    def _create_sequentialsets(self):
        
        self.options['structure'] = self.structure['SEQ']
        
        return self.exercises[:]
    
    
    def set_structure(self, style):
        
        if style == 'Superset':
            # TODO: refactor to compare modulus division
            if len(self.exercises) != self.structure['SS']['size']:
                
                print("Error: Structure style must match size of list")
                
            else:
                
                return self._create_supersets()
                              
                    
        elif style == 'Triset':
            
            if len(self.exercises) != self.structure['TS']['size']:
                
                print("Error: Structure style must match size of list")
                
            else:
                
                return self._create_trisets()
        
        elif style == 'Quadset':
            
            if len(self.exercises) != self.structure['QS']['size']:
                
                print("Error: Structure style must match size of list")
                
            else:
                
                return self._create_quadsets()
        
        elif style == 'Sequential':
            
            if (len(self.exercises) > 4 <= 10):
                
                return self._create_sequentialsets()
            
            else:
                
                print("Error: Structure style must match size of list")
    
    
    def set_interval(self, interval):
        
        self.options['interval'] = self.interval[interval]
    
        
    def set_rounds(self, rounds):
        
        self.options['rounds'] = rounds
    
    
    def set_block(self, block):
        
        self.options['block'] = block
    
    
    def set_reps(self, reps):
        
        self.options['reps'] = reps
        
    