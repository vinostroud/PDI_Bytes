from collections import namedtuple

#namedtuple is score, ninjas. So in dictionary below yellow is key, value is score 50, ninjas 11
BeltStats = namedtuple('BeltStats', 'score ninjas')


ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5),
               'brown': BeltStats(400, 2),
               'black': BeltStats(600, 5)}

            

def get_total_points():
    sum_total = 0
    for i, j in ninja_belts.items(): #i is belt color (eg yellow), j is BeltStats(score, ninjas)
        
        scores = getattr(j, 'score')
        ninj_nums = getattr(j, 'ninjas')
        totals = scores * ninj_nums
        sum_total += totals
    return(sum_total) 

print(get_total_points())


    