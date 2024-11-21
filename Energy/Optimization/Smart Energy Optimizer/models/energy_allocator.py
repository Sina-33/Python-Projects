from scipy.optimize import linprog

class EnergyAllocator:
    def __init__(self, total_energy):
        self.total_energy = total_energy

    def optimize_allocation(self, demands, priorities):
        c = [-p for p in priorities]
        A = [[1] * len(demands)]
        b = [self.total_energy]

        result = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="highs")
        if result.success:
            return result.x
        else:
            raise ValueError("Optimization failed")
