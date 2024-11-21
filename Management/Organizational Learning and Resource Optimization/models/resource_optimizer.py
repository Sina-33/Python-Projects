from scipy.optimize import linprog

class ResourceOptimizer:
    def __init__(self, budget, time, people):
        self.resources = {'budget': budget, 'time': time, 'people': people}

    def optimize_allocation(self, priorities):
        c = [-p for p in priorities]
        A = [[1, 2, 1], [2, 1, 2], [1, 1, 1]]
        b = [self.resources['budget'], self.resources['time'], self.resources['people']]
        result = linprog(c, A_ub=A, b_ub=b, method='highs')
        if result.success:
            return result.x
        else:
            raise ValueError('Optimization failed')