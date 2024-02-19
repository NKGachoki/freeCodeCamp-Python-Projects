import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)


    def draw(self, no_of_balls):
        if no_of_balls >= len(self.contents):
            return self.contents
        else:
            drawn_balls = random.choices(self.contents, k=no_of_balls)
            for i in drawn_balls:
                self.contents.remove(i)
            return drawn_balls
        
def experiment(**kwargs):
    values = list(kwargs.values())
    hat_contents = values[0].contents
    expected_balls = []
    for key, value in values[1].items():
        for i in range(value):
            expected_balls.append(key)
    
    count = 0
    for i in range(values[3]):
        deductions = 0
        drawn_balls = random.choices(hat_contents,k=values[2])
        copied_drawn_balls = copy.deepcopy(drawn_balls)
        for key, value in values[1].items():
            for i in range(value):
                try:
                    copied_drawn_balls.remove(key)
                    deductions += 1
                except ValueError:
                    continue
        if deductions == len(expected_balls):
            count += 1
       
    probability = count/values[3]
    return probability
