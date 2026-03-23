from tabulate import  tabulate
import math

def error(pres, prev):
    if prev is None:
        return None
    return abs((pres - prev) / pres * 100)

def is_same_sign(num1, num2):
    if(num1 >= 0):
        return True if num2 > 0 else False
    return True if num2 < 0 else False

class RootApprox:
    def __init__(self, fx = None, Fx = None, gx = None, decimals = None):
        self.fx = fx
        self.Fx = Fx
        self.gx = gx
        self.decimals = decimals

    def __round(self, num):
        if self.decimals is None:
            return num
        return round(num, self.decimals)

    def f(self, x):
        return self.__round(self.fx(x))

    def F(self, x):
        return self.__round(self.Fx(x))

    def g(self, x):
        return self.__round(self.gx(x))

    def bisection(
        self,
        left,
        right,
        iters,
        correction = None,
        _print_result = True
    ):
        out = []
        prev = None
    
        for i in range(iters):
            lo = left
            hi = right
            mi = (lo + hi) / 2
            flo = self.f(lo)
            fhi = self.f(hi)
            fmi = self.f(mi)
            err = error(mi, prev)
        
            prev = mi
            out.append([i, lo, mi, hi, flo, fmi, fhi, err])

            if(not err is None and not correction is None and err < correction):
                break

            if(is_same_sign(flo, fhi)):
                if(is_same_sign(flo, fmi)):
                    raise ValueError("No root found")
            
                lomi_dist = abs(flo - fmi)
                mihi_dist = abs(fmi - fhi)

                if(lomi_dist < mihi_dist):
                    left = lo
                    right = mi
                else:
                    left = mi
                    right = hi

                continue
 
            if(not is_same_sign(flo, fmi)):
                left = lo
                right = mi
                continue

            if(not is_same_sign(fmi, fhi)):
                left = mi
                right = hi
                continue

        headers = ["i", "xlo", "xmi", "xhi", "f(xlo)", "f(xmi)", "f(xhi)", "err(%)"]
        if(_print_result):
            self.printOut(headers, out)
        return headers, out

    def secant(
        self,
        xnO,
        xnI,
        iters,
        correction = None,
        _print_result = True
    ):
        out = []
        prev = None

        for i in range(iters):
            old = xnO
            curr = xnI
            fold = self.f(old)
            fcurr = self.f(curr)

            try:
                new = curr - fcurr * (curr - old) / (fcurr - fold)
            except ZeroDivisionError:
                break

            fnew = self.f(new)
            err = error(new, prev)
            prev = new

            out.append([i, old, curr, new, fold, fcurr, fnew, err])

            if(not err is None and not correction is None and err < correction):
                break

            xnO = curr
            xnI = new

        headers = ["i", "xn-1", "xn", "xn+1", "f(xn-1)", "f(xn)", "f(xn+1)", "err(%)"]
        if(_print_result):
            self.printOut(headers, out)
        return headers, out

    def newtons(
        self,
        init,
        iters,
        correction = None,
        _print_result = True
    ):
        out = []
        prev = None
        for i in range(iters):
            curr = init
            fcurr = self.f(curr)
            Fcurr = self.F(curr)
            new = curr - fcurr/Fcurr
            err = error(new, prev)
            prev = new

            out.append([i, curr, fcurr, Fcurr, new, err])
            
            if(not err is None and not correction is None and err < correction):
                break

            init = new

        headers = ["i", "xn", "f(xn)", "f`(xn)", "xn+1", "err(%)"]
        if(_print_result):
            self.printOut(headers, out)
        return headers, out

    def fixedpoint(
        self,
        init,
        iters,
        correction = None,
        _print_result = True
    ):
        out = []
        prev = None

        for i in range(iters):
            curr = init
            new = self.g(curr)
            err = error(new, prev)
            prev = new
            out.append([i, curr, new, err])

            if(not err is None and not correction is None and err < correction):
                break

            init = new
        headers = ["i", "xn", "xn+1", "err(%)"]
        if(_print_result):
            self.printOut(headers, out)
        return headers, out

    @classmethod
    def printOut(cls, headers, out):
        print(tabulate(out, headers=headers, tablefmt="fancy_grid"))        
