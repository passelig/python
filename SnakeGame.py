from sympy import symbols, Eq, solve, sqrt

# Define the variable
z = symbols('z')

# Step 1: Write the equation
equation = Eq(z**2 - 2*z + 6, 0)
print(f"Step 1: The equation is: {equation}")

# Step 2: Use the quadratic formula to solve for z
# The quadratic formula is z = (-b ± sqrt(b^2 - 4ac)) / 2a
a = 1
b = -2
c = 6

# Calculate the discriminant
discriminant = b**2 - 4*a*c
print(f"Step 2: The discriminant is: {discriminant}")

# Step 3: Calculate the roots based on the discriminant
if discriminant > 0:
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)
    print(f"Step 3: The equation has two real roots: z = {root1} and z = {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Step 3: The equation has one real root: z = {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = sqrt(-discriminant) / (2*a)
    root1 = real_part + imaginary_part*1j
    root2 = real_part - imaginary_part*1j
    print(f"Step 3: The equation has two complex roots: z = {root1} and z = {root2}")
