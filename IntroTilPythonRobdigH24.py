# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:44:15 2024

@author: gunsto
"""

from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define the equation
equation = Eq(2*x/3+x/4, 5/6-6)

# Solve the equation
solution = solve(equation, x)

# Display the solution
print("The solution is:", solution)