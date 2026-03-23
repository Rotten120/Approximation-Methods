from nummeth import RootApprox

problem = RootApprox(
    fx = lambda x: x**3 - x - 2,
    Fx = lambda x: 3*x**2 - 1,
    decimals = 10
)

# Even if the error is still above 1%
# Process stops at 50th iteration
problem.bisection(1, 2, 50, correction = 1)


# Does not print the output
headers, values = problem.secant(1, 2, 10, _print_result = False)

# Manually prints the value if user wants to edit
# First the output (in this case prints the last 3 values)
problem.printOut(headers, values[-5:])

problem.newtons(1.5, 3)
