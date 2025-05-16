class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    
double = Multiplier(2)
triple = Multiplier(3)

# Test if the object is callable
print(callable(double))  # True
print(callable(triple))  # True

# Use the object like a function
print(double(5))  # 10
print(triple(5))  # 15

numbers = [11, 22, 33, 14, 25]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers) # [22, 44, 66, 28, 50]

tripled_numbers = list(map(triple, numbers))
print(tripled_numbers) #[33, 66, 99, 42, 75]