def calculate(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    else:
        return "Invalid operation"

print(calculate("add",4,5))
print(calculate("multiply",4,5))
print(calculate("max",4,5))
print(calculate("min",4,5))
print(calculate("total",4,5))

