import copy
import random
# Consider using the modules imported above.

class Hat(object):
  def __init__(self,**kwargs):
    self.contents = []
    for ball in kwargs.items():
      for count in range(ball[1]):
        self.contents.append(ball[0])
      
  def draw(self,qty):
    #if we want to draw more than we have
    if qty > len(self.contents):
      contents = self.contents[:]
      self.contents = []
      return contents
    
    #pick random number and pop balls into a draw array
    drawn = []
    while qty:
      idx = random.randint(0,len(self.contents)-1)
      pulled = self.contents.pop(idx)
      drawn.append(pulled)
      qty -= 1
    
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_cnt = 0

  for run in range(num_experiments):
    hat_cpy = copy.deepcopy(hat)
    drawn = hat_cpy.draw(num_balls_drawn)

    #transform drawn list to dict
    drawn_dict = {}
    for ball in drawn:
      if ball in drawn_dict:
        drawn_dict[ball] += 1
      else:
        drawn_dict[ball] = 1

    # now see whether drawn satisfies experiment criteria
    criteria_failed = False
    for ball in expected_balls.items():
      expected_ball_name = ball[0]
      expected_ball_qty = ball[1]
      if expected_ball_name not in drawn_dict or drawn_dict[expected_ball_name] < expected_ball_qty:
        criteria_failed = True;
        break;


    if not criteria_failed :
      success_cnt +=1
    
  return success_cnt/num_experiments
