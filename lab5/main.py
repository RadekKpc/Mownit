from mpmath import cos,cosh,sec,sin,sinh,exp,tan,fabs,mpf,log,mp,pi

f1 = lambda x : cos(x)*cosh(x) - 1
f2 = lambda x : 1/x  - tan(x)
f3 = lambda x : 2**(-x) + exp(x) + 2*cos(x) - 6


def bisection(min_precision,left,right,absolute_error,f):

    # ustawienie precyzji
    mp.dps = min_precision
    # zfracany wnik
    x = mpf(0.0)
    # liczba krokow
    k = 0

    left = mpf(left)
    right = mpf(right)
    absolute_error = mpf(absolute_error)

    while fabs(left - right) > absolute_error:

        x = mpf((left + right)/2)
        if fabs(f(x)) <= absolute_error:
            break
        elif mpf(f(left))*mpf(f(x)) < mpf(0):
            right = x
        elif mpf(f(right))*mpf(f(x)) < mpf(0):
            left = x
        k += 1

    print("Miejsce zerowe",x)
    print("Wartosc funkcji",f(x))
    print("Liczba krokow",k)
    print()


#  dla f1

left_f1 = mpf(3/2*pi)
right_f1 = mpf(2*pi)

left_f2 = mpf(0)
right_f2 = mpf(pi/2)

left_f3 = mpf(1)
right_f3 = mpf(3)

# dla f1
bisection(7,left_f1,right_f1,mpf(10**(-7)),f1)

#  dla f2
bisection(7,left_f2 +mpf(10**(-7)),right_f2,mpf(10**(-7)),f2)

#  dla f3
bisection(7,left_f3,right_f3,mpf(10**(-7)),f3)

#  dla f1
bisection(15,left_f1,right_f1,mpf(10**(-15)),f1)

#  dla f2
bisection(15,left_f2+mpf(10**(-15)),right_f2,mpf(10**(-15)),f2)

#  dla f3
bisection(15,left_f3,right_f3,mpf(10**(-15)),f3)

#  dla f1
bisection(33,left_f1,right_f1,mpf(10**(-33)),f1)

#  dla f2
bisection(33,left_f2+mpf(10**(-7)),right_f2,mpf(10**(-33)),f2)

#  dla f3
bisection(33,left_f3,right_f3,mpf(10**(-33)),f3)

k = 10
for i in range(k):
    print("Mijesce zerowe",i+1)
    bisection(10,(i+1)*pi ,(i+2)*pi,mpf(10**(-7)),f1)


# metoda newtona

def newton_method(min_precision,left,right,epsilon,f,df,max_iterations):
    mp.dps = min_precision
    k = 0
    start_point = mpf(left)
    x = mpf(right)
    epsilon = mpf(epsilon)
    while k < max_iterations:

        x = start_point - mpf(f(start_point))/mpf(df(start_point))

        if  fabs(start_point - x) <= epsilon:
            break
        start_point = x
        k += 1

    print("Miejsce zerowe",x)
    print("Wartosc funkcji",f(x))
    print("Liczba krokow",k)


df1 = lambda x : -cosh(x)*sin(x) + cos(x)*sinh(x)
df2 = lambda x : -1/(x**2) - sec(x)**2
df3 = lambda x : exp(x) - 2**(-x)*log(2) - 2*sin(x)

#  dla f1
newton_method(7,left_f1,right_f1,mpf(10**(-7)),f1,df1,200)

#  dla f2
newton_method(7,left_f2 + mpf(10**(-7)),right_f2,mpf(10**(-7)),f2,df2,200)

#  dla f3
newton_method(7,left_f3,right_f3,mpf(10**(-7)),f3,df3,200)

#  dla f1
newton_method(15,left_f1,right_f1,mpf(10**(-15)),f1,df1,200)

#  dla f2
newton_method(15,left_f2+mpf(10**(-15)),right_f2,mpf(10**(-15)),f2,df2,200)

#  dla f3
newton_method(15,left_f3,right_f3,mpf(10**(-15)),f3,df3,200)

#  dla f1
newton_method(33,left_f1,right_f1,mpf(10**(-33)),f1,df1,200)

#  dla f2
newton_method(33,left_f2+mpf(10**(-33)),right_f2,mpf(10**(-33)),f2,df2,200)

#  dla f3
newton_method(33,left_f3,right_f3,mpf(10**(-33)),f3,df3,200)

def euler_method(min_precision,left,right,epsilon,f,max_iterations,k):
    mp.dps = min_precision
    left = mpf(left)
    right = mpf(right)
    epsilon = mpf(epsilon)
    k = 0
    while max_iterations > 0 and fabs(left - right) > epsilon:
        max_iterations -= 1
        k += 1
        x0 = left - f(left)*(left - right)/(f(left) - f(right))
        right = left
        left = x0
        if f(x0) < epsilon:
            break
    print("Miejsce zerowe",x0)
    print("Wartosc funkcji",f(x0))
    print("Liczba krokow",k)
    print()
    # start_point = left
    # x = right

#  dla f1
print("Metoda siecznych")
newton_method(7,left_f1,right_f1,mpf(10**(-7)),f1,df1,200)

#  dla f2
newton_method(7,left_f2 + mpf(10**(-7)),right_f2,mpf(10**(-7)),f2,df2,200)

#  dla f3
newton_method(7,left_f3,right_f3,mpf(10**(-7)),f3,df3,200)

#  dla f1
newton_method(15,left_f1,right_f1,mpf(10**(-15)),f1,df1,200)

#  dla f2
newton_method(15,left_f2 + mpf(10**(-15)),right_f2,mpf(10**(-15)),f2,df2,200)

#  dla f3
newton_method(15,left_f3,right_f3,mpf(10**(-15)),f3,df3,200)

#  dla f1
newton_method(33,left_f1,right_f1,mpf(10**(-33)),f1,df1,200)

#  dla f2
newton_method(33,left_f2 + mpf(10**(-33)),right_f2,mpf(10**(-33)),f2,df2,200)

#  dla f3
newton_method(33,left_f3,right_f3,mpf(10**(-33)),f3,df3,200)