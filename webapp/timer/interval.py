import time

class IntervalTimer:
    'Interval timer to render the workouts and timer module through the browser'
    'Future implementation will be a subscription service of private and commercial use'
    def __init__(self, work, rest, rounds, between_circuits, factor):
        self.work = work
        self.rest = rest
        self.rounds = rounds
        self.between_circuits = between_circuits
        self.factor = factor
        
    def get_start_time(self):
        self.start_time = time.time()
        return self.start_time
        
    def run_work(self):
        for x in range(self.work, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            print(f"{minutes:02}:{seconds:02}")
            time.sleep(1)
    
    def run_rest(self):
        for y in range(self.rest, 0, - 1):
            seconds = y % 60
            minutes = int(y / 60) % 60
            print(f"{minutes:02}:{seconds:02}")
            time.sleep(1)
    
    def run_break(self):
        print('Run Break = ', self.between_circuits)
        for i in range(self.between_circuits, 0, -1):
            seconds = i % 60
            minutes = int(i / 60) % 60
            print(f"{minutes:02}:{seconds:02}")
            time.sleep(1)
        print('End Break')
        
    def run_circuit(self):
        count = 0
        for j in range((self.rounds * self.factor), 0, -1):
            print("Begin round: ", count + 1)
            self.run_work()
            self.run_rest()
            count += 1
        print('Complete')
    
    def reset(self):
        time.sleep(0)
        
    def pause(self):
        return time.time() - self.get_start_time()
    
    def resume(self):
        pass

# timer = IntervalTimer(work=5, rest=5, rounds=2, between_circuits=10, factor=2)
