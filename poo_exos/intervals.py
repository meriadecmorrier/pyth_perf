class IntervalError(Exception):
    pass

class Interval:
    def __init__(self, inf, sup):
        if not (isinstance(inf, (int, float)) and isinstance(sup, (int, float))):
            raise IntervalError("Invalid interval, bounds must be numbers")
        if inf==0 or sup==0:
            raise IntervalError("Invalid interval, bounds must be non-zero")
        if inf > sup:
            raise IntervalError("Invalid interval, lower bound must be less than upper bound")
        self.inf = inf
        self.sup = sup

    def __str__(self):
        return f"[{self.inf}, {self.sup}]"
    
    def __contains__(self, val):
        return val >= self.inf and val <= self.sup
    
    def __add__(self, other):
        if not isinstance(other, Interval):
            raise IntervalError("Can only add Interval to Interval")
        return Interval(self.inf + other.inf, self.sup + other.sup)

    def __sub__(self, other):
        if not isinstance(other, Interval):
            raise IntervalError("Can only subtract Interval from Interval")
        return Interval(self.inf - other.sup, self.sup - other.inf)
    
    def __mul__(self, other):
        if not isinstance(other, Interval):
            raise IntervalError("Can only multiply Interval by Interval")
        return Interval(self.inf*other.inf, self.sup*other.sup)
    
    def __and__(self, other):
        if not isinstance(other, Interval):
            raise IntervalError("Can only intersect Interval with Interval")
        new_inf = max(self.inf, other.inf)
        new_sup = min(self.sup, other.sup)
        if new_inf > new_sup:
            raise IntervalError("Intervals do not overlap")
        return Interval(new_inf, new_sup)
    

int1 = Interval(1,5)
int2 = Interval(3,6)
print(int1)            # Affiche [1, 5]
print(4 in int1)      # Affiche True
print(int1+int2)
print(int1 & int2)  # Affiche [3, 5]
