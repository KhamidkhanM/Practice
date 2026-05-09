print("====== Numbers =====")
# variables in java is a name of the storage
# variable is named reference

count = 100
count_type = type(count)
print("Count Type:", count_type)
print(f"Count: {count} and Count Type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("====== Strings =====")
# Methods: title() upper() lower() find() replace()

course = "Ai Python fullstack"
result = type(course)
print(f"Result (1): {result}")

result = course.title()
print(f"Result (2): {result}")

result = course.upper()
print(f"Result (3): {result}")

result = course.replace("fullstack", "masterclass")
print(f"Result (4): {result}")


print("====== Booleans =====")
# functions: type(), input(), bool(), int(), str()

y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print("result:", result)
print("the input value is numeric:", result)

# Truthy vs Falsy
# Truthy: True values: 100, -100, "MIT"
# Falsy: False values: 0, 0.0, 0j, None, False, [], {}, set(), "", range(0)

test_falsy = "" or False or None or 0  # or 100
print("test_falsy:", bool(test_falsy))

test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))
