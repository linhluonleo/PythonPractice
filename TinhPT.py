import math


def ptb1(a, b):
    print("Phương trình có nghiệm x = ", round(-b/a, 2))


def ptb2(a, b, c):
    if a == 0:
        return ptb1(b, c)
    dt = b**2 - 4*a*c
    if dt > 0:
        x1 = round((-b + math.sqrt(dt))/(2*a), 2)
        x2 = round((-b - math.sqrt(dt))/(2*a), 2)
        print("Phương trình có 2 nghiệm x1 = ", x1, ", x2 = ", x2)
    elif dt == 0:
        x = round(-b/(2*a), 2)
        print("Phương trình có nghiệm kép x1 = x2 = ", x)
    else:
        x1 = complex(-b/(2*a), round(math.sqrt(math.fabs(dt)), 2)/(2*a))
        x2 = complex(-b/(2*a), -round(math.sqrt(math.fabs(dt)), 2)/(2*a))
        print("Phương trình có 2 nghiệm phức x1 = ", x1, ", x2 = ", x2)


def ptb3(a, b, c, d):
    if a == 0:
        return ptb2(b, c, d)
    dt = b**2 - 3*a*c
    k = (9*a*b*c - 2*(b**3) - 27*(a**2)*d)/(2*math.sqrt((math.fabs(dt))**3))
    if dt > 0:
        if math.fabs(k) <= 1:
            x1 = round((2*math.sqrt(dt)*math.cos(math.acos(k)/3)-b)/(3*a), 2)
            x2 = round((2*math.sqrt(dt)*math.cos((math.acos(k)/3)-((2*math.pi)/3))-b)/(3*a), 2)
            x3 = round((2*math.sqrt(dt)*math.cos((math.acos(k)/3)+((2*math.pi)/3))-b)/(3*a), 2)
            print("Phương trình có 3 nghiệm x1 = ",
                  x1, " , x2 = ", x2, ", x3 = ", x3)
        else:
            x = round(((math.sqrt(dt)*math.fabs(k))/(3*a*k))*((math.fabs(k)+math.sqrt(k**2-1))**(1/3)+(math.fabs(k)-math.sqrt(k**2-1))**(1/3))-(b/(3*a)), 2)
            print("Phương trình có nghiệm duy nhất x = ", x)
    elif dt == 0:
        if b**3 -27*(a**2)*d == 0:
            x = round(-b/3*a, 2)
            print("Phương trình có nghiệm kép x1 = x2 = ", x)
        elif b**3 -27*(a**2)*d != 0:
            x = round((-b+(b**3 -27*(a**2)*d)**(1/3))/(3*a), 2)
            print("Phương trình có nghiệm duy nhất x = ", x)
    else:
        x = round((math.sqrt(math.fabs(dt))/(3*a))*((k+math.sqrt(k**2-1))**(1/3)+(k-math.sqrt(k**2-1))**(1/3))-(b/(3*a)), 2)
        print("Phương trình có nghiệm duy nhất x = ", x)
        