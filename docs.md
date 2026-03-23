# NUMERICAL METHODS ROOT APPROXIMATION

- This codebase supports root approximation for the following methods
1. Bisection Method
2. Secant Method
3. Newton-Raphson Method
4. Fixed Point Iteration Method

## DEPENDENCIES

```
pip install tabulate
```

## DOCUMENTATION

```
class RootApprox(fx = None, Fx = None, gx = None, decimals = None)
    Description:
    - The base class template for doing root approximations

    Parameters:
    - fx : the function to find the roots for, should be expressed as lambda
    - Fx : the derivative of the function, should be expressed as lambda
    - gx : the chosen form of fx where x = g(x), should be expressed as lambda
    - decimals : the decimal places to round the outputs from,
               : will not round the number when value is None
```
```
RootApprox.__round(self, num)
    Description:
    - rounds the number depending on self.decimals
    - does not round the number if self.decimals value is None

    Parameters:
    - num : number to round

    Returns:
    - Rounded number
```
```
RootApprox.f(self, x), RootApprox.F(self, x), RootApprox.g(self, x)
    Description:
    - Uses the stored value in the class (fx, Fx, or gx) to compute given the parameter

    Parameters:
    - x : value to substitute to the given function

    Returns:
    - Solved value
```
```
RootApprox.bisection(self, left, right, iters, correction = None, _print_result = True)
    Description:
    - Uses the bisection method to find the root over a given interval
    - self.fx should have a value

    Parameters:
    - left  : the lower value in the interval
    - right : the higher value in the interval
    - iters : how many iterations MAX should be computed
    - correction : % error that the computation must have
                 : exits the loop if the % error is lower than the correction value (in %)
    - _print_result : prints the result in a tabular form

    Returns:
    - header : header of the table if user should want to print it in table
    - out : the output of the method per iteration
```
```
RootApprox.secant(self, xnO, xnI, iters, correction = None, _print_result = True)
    Description:
    - Uses the secant method to find the root
    - self.fx should have a value

    Parameters:
    - xnO : The First value xn0 or xn-1
    - xnI : The second value xn1 or xn
    - iters : how many iterations MAX should be computed
    - correction : % error that the computation must have
                 : exits the loop if the % error is lower than the correction value (in %)
    - _print_result : prints the result in a tabular form

     Returns:
    - header : header of the table if user should want to print it in table
    - out : the output of the method per iteration
```
```
RootApprox.newtons(self, init, iters, correction = None, _print_result = True)
    Description:
    - Uses the newton-raphson method to find the root
    - self.fx and self.Fx should have a value

    Parameters:
    - init : The initial x value
    - iters : how many iterations MAX should be computed
    - correction : % error that the computation must have
                 : exits the loop if the % error is lower than the correction value (in %)
    - _print_result : prints the result in a tabular form

     Returns:
    - header : header of the table if user should want to print it in table
    - out : the output of the method per iteration
```
```
RootApprox.fixedpoint(self, init, iters, correction = None, _print_result = True)
    Description:
    - Uses the fixed-point iteration method to find the root
    - self.gx should have a value

    Parameters:
    - init : The initial x value
    - iters : how many iterations MAX should be computed
    - correction : % error that the computation must have
                 : exits the loop if the % error is lower than the correction value (in %)
    - _print_result : prints the result in a tabular form

     Returns:
    - header : header of the table if user should want to print it in table
    - out : the output of the method per iteration
```
```
RootApprox.printOut(cls, headers, out)
    Description:
    - Prints a table based on the given headers and table content
```
