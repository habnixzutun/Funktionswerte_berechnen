from prettytable import PrettyTable
import math


def linear_funktion():
    table = PrettyTable(["X-Werte", "Y-Werte"])
    try:
        while True:
            try:
                m = float(input("M:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                c = float(input("C:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        function = "f(x) = {}x + {}".format(m, c)
        print(function)
        while True:
            try:
                von_x = float(input("Kleinster x Wert?\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                bis_x = float(input("Größter x Wert?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                inkrement = float(input("Inkrement?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        x = von_x
        # dict = {"x": "y"}
        while x <= bis_x:
            # dict[x] = m * x + c
            # xpoints.append(x)
            # ypoints.append(m * x + c)
            table.add_row([x, m * x + c])
            x += inkrement
        print(table)
        # for x_wert, y_wert in dict.items():
        # print("{}\t\t|\t\t{}".format(x_wert, y_wert))
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    table.add_row([x, m * x + c])
                    print(table)
                    # print("{}\t\t|\t\t{}".format(x, m * x + c))
                except ValueError:
                    break
        while True:
            response = input("\nNoch ein spezieller Y-Wert? ").lower()
            if response != "nein":
                try:
                    y = float(response)
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    table.add_row([(y - c)/m, y])
                    print(table)
                except ValueError:
                    break
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def quadratic_funktion():
    table = PrettyTable(["X-Werte", "Y-Werte"])
    try:
        while True:
            try:
                a = float(input("A:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                d = float(input("D:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                e = float(input("E:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        exponent = 2
        if d >= 0 and e >= 0:
            result = "\nScheitelform:\t{}(x + {})^2 + {}".format(a, d, e)
        elif d <= 0 and e >= 0:
            result = "\nScheitelform:\t{}(x {})^2 + {}".format(a, d, e)
        elif d >= 0 and e <= 0:
            result = "\nScheitelform:\t{}(x + {})^2 {}".format(a, d, e)
        else:
            result = "\nScheitelform:\t{}(x {})^2 {}".format(a, d, e)
        print(result)
        scheitelpunkt = "S({}|{})".format(d * 1, e)
        b = -2*a*d
        c = a*(d**2)+e
        if b > 0 and c > 0:
            print("Allgemeine Form:\t{}x^2 + {}x + {}".format(a, b, c))
        elif b > 0 and c < 0:
            print("Allgemeine Form:\t{}x^2 + {}x {}".format(a, b, c))
        elif b < 0 and c > 0:
            print("Allgemeine Form:\t{}x^2 {}x + {}".format(a, b, c))
        else:
            print("Allgemeine Form:\t{}x^2 {}x {}".format(a, b, c))
        if exponent % 2 == 0:
            print(scheitelpunkt)
        if e > 0 and a > 0 or e < 0 and a < 0:
            x1 = ((-b) + ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
            x2 = ((-b) - ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
            if 0 >= e:
                if x1 == x2:
                    nullstellen = f"Nullstelle:\t({x1}|0)"
                else:
                    nullstellen = f"Nullstellen:\t({x1}|0), ({x2}|0)"
                print(nullstellen)
        while True:
            try:
                von_x = float(input("Kleinster x Wert?\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                bis_x = float(input("Größter x Wert?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                inkrement = float(input("Inkrement?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        x = von_x
        while x <= bis_x:
            table.add_row([x, a * (x - d)**exponent + e])
            x += inkrement
        print(table)
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    table.add_row([x, a * (x - d)**exponent + e])
                    print(table)
                except ValueError:
                    break
        while True:
            response = input("\nNoch ein spezieller Y-Wert? ").lower()
            if response != "nein":
                try:
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    y = float(response)
                    if y >= e:
                        if y == e:
                            table.add_row([d, y])
                        else:
                            c_temp = c - y
                            x1 = ((-b) + ((b ** 2) - (4 * a * c_temp)) ** (0.5)) / (2 * a)
                            x2 = ((-b) - ((b ** 2) - (4 * a * c_temp)) ** (0.5)) / (2 * a)
                            table.add_row([f"{x1}, {x2}", y])
                        print(table)
                except ValueError:
                    break
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def quadratic_funktion2():
    table = PrettyTable(["X-Werte", "Y-Werte"])
    try:
        while True:
            try:
                a = float(input("A:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                b = float(input("B:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                c = float(input("C:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        if b >= 0 and c > 0:
            print("\nAllgemeine Form:\t{}x^2 + {}x + {}".format(a, b, c))
        elif b >= 0 and c < 0:
            print("\nAllgemeine Form:\t{}x^2 + {}x {}".format(a, b, c))
        elif b < 0 and c >= 0:
            print("\nAllgemeine Form:\t{}x^2 {}x + {}".format(a, b, c))
        else:
            print("\nAllgemeine Form:\t{}x^2 {}x {}".format(a, b, c))
        d = b / (2 * a)
        e = c - ((b ** 2) / (4 * a))
        if d >= 0 and e >= 0:
            result = "Scheitelform:\t{}(x + {})^2 + {}".format(a, d, e)
        elif d <= 0 and e >= 0:
            result = "Scheitelform:\t{}(x {})^2 + {}".format(a, d, e)
        elif d >= 0 and e <= 0:
            result = "Scheitelform:\t{}(x + {})^2 {}".format(a, d, e)
        else:
            result = "Scheitelform:\t{}(x {})^2 {}".format(a, d, e)
        print(result)
        if e > 0 and a > 0 or e < 0 and a < 0:
            x1 = ((-b) + ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
            x2 = ((-b) - ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
            if 0 >= e:
                if x1 == x2:
                    nullstellen = f"Nullstelle:\t({x1}|0)"
                else:
                    nullstellen = f"Nullstellen:\t({x1}|0), ({x2}|0)"
                print(nullstellen)
        while True:
            try:
                von_x = float(input("Kleinster x Wert?\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                bis_x = float(input("Größter x Wert?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                inkrement = float(input("Inkrement?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        x = von_x
        while x <= bis_x:
            table.add_row([x, (a * (x**2)) + (b * x) + c])
            x += inkrement
        print(table)
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    table.add_row([x, (a * (x**2)) + (b * x) + c])
                    print(table)
                except ValueError:
                    break
        while True:
            response = input("\nNoch ein spezieller Y-Wert? ").lower()
            if response != "nein":
                try:
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    y = float(response)
                    if y >= e:
                        if y == e:
                            table.add_row([d, y])
                        else:
                            c_temp = c - y
                            x1 = ((-b) + ((b ** 2) - (4 * a * c_temp)) ** (0.5)) / (2 * a)
                            x2 = ((-b) - ((b ** 2) - (4 * a * c_temp)) ** (0.5)) / (2 * a)
                            table.add_row([f"{x1}, {x2}", y])
                        print(table)
                except ValueError:
                    break
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def root_funktion():
    table = PrettyTable(["X-Werte", "Y-Werte"])
    try:
        while True:
            try:
                root = float(input("Wurzel:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                a = float(input("A:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                d = float(input("D:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                e = float(input("E:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        function = "f(x) = {}root({}x - {}) + {}".format(root, a, d, e)
        print(function)
        while True:
            try:
                von_x = float(input("Kleinster x Wert?\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                bis_x = float(input("Größter x Wert?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                inkrement = float(input("Inkrement?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        x = von_x
        # dict = {"x": "y"}
        while x <= bis_x:
            if x <= d:
                table.add_row([x, "nicht definiert"])
                x += inkrement
            elif x == d:
                table.add_row([x, 0])
                x += inkrement
            else:
                table.add_row([x, a * (x - d)**(1/float(root)) + e])
                x += inkrement
        print(table)
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    if x <= d:
                        table.add_row([x, "nicht definiert"])
                    elif x == d:
                        table.add_row([x, 0])
                    else:
                        table.add_row([x, a * (x - d) ** (1 / float(root)) + e])
                    print(table)
                except ValueError:
                    break
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def exponential_funktion():
    table = PrettyTable(["X-Werte", "Y-Werte"])
    try:
        while True:
            try:
                basis = float(input("Basis:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                d = float(input("D:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                e = float(input("E:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        function = "f(x) = {}^(x + {}) + {}".format(basis, d, e)
        print(function)
        while True:
            try:
                von_x = float(input("Kleinster x Wert?\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                bis_x = float(input("Größter x Wert?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                inkrement = float(input("Inkrement?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        x = von_x
        while x <= bis_x:
            if x <= 0:
                table.add_row([x, 1 / (basis ** (-x - d)) + e])
                x += inkrement
            else:
                table.add_row([x, basis**(x - d) + e])
                x += inkrement
        print(table)
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    table.add_row([x, basis**(x - d) + e])
                    print(table)
                except ValueError:
                    break
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def logarithmic_funktion():
    table = PrettyTable(["X-Werte", "Y-Werte"])
    try:
        while True:
            try:
                basis = float(input("Basis:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                d = float(input("D:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                e = float(input("E:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        function = "f(x) = log{}(x - {}) + {}".format(basis, d, e)
        print(function)
        while True:
            try:
                von_x = float(input("Kleinster x Wert?\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                bis_x = float(input("Größter x Wert?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                inkrement = float(input("Inkrement?\t\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        x = von_x
        # dict = {"x": "y"}
        while x <= bis_x:
            try:
                table.add_row([x, math.log(x-d, basis) + e])
                x += inkrement
            except ValueError:
                if x == d:
                    table.add_row([x, "-∞"])
                    x += inkrement
                else:
                    table.add_row([x, "nicht definiert"])
                    x += inkrement
        print(table)
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Wert", "Y-Wert"])
                    table.add_row([x, math.log(x-d, basis) + e])
                    print(table)
                except ValueError:
                    break
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def schnittpunkt_lineare_gleichung():
    try:
        while True:
            try:
                m1 = float(input("M von Funktion 1:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                c1 = float(input("C von Funktion 1:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                m2 = float(input("M von Funktion 2:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                c2 = float(input("C von Funktion 2:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        schnittpunkt_x = (c2 - c1) / (m1 - m2)
        schnittpunkt_y = m1 * schnittpunkt_x + c1
        print("Schnittpunkt:\t({}|{})".format(schnittpunkt_x, schnittpunkt_y))
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("Die Geraden sind paralell")


def schnittpunkt_quadratische_gleichung1():
    while True:
        try:
            a1 = float(input("A von Funktion 1:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            d1 = float(input("D von Funktion 1:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            e1 = float(input("E von Funktion 1:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            a2 = float(input("\nA von Funktion 2:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            d2 = float(input("D von Funktion 2:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            e2 = float(input("E von Funktion 2:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    b1 = -2 * a1 * d1
    c1 = a1 * (d1 ** 2) + e1
    b2 = -2 * a2 * d2
    c2 = a2 * (d2 ** 2) + e2
    try:
        a = a2 - a1
        b = b2 - b1
        c = c2 - c1
        x1 = ((-b) + ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
        x2 = ((-b) - ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
        x1 = float(x1)
        x2 = float(x2)
        y = a1 * (x1) ** 2 + b1 * x1 + c1
        if x1 == x2:
            print(f"\nSchnittpunkt:\t({x1}|{y})")
        else:
            print(f"\nSchnittpunkte:\t({x1}|{y}), ({x2}|{y})")
    except TypeError:
        print("\nDie Parabeln schneiden sich nicht")


def schnittpunkt_quadratische_gleichung2():
    while True:
        try:
            a1 = float(input("A von Funktion 1:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            b1 = float(input("B von Funktion 1:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            c1 = float(input("C von Funktion 1:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            a2 = float(input("A von Funktion 2:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            b2 = float(input("B von Funktion 2:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    while True:
        try:
            c2 = float(input("C von Funktion 2:\t"))
            break
        except ValueError:
            print("Bitte eine Zahl eingeben")
    try:
        a = a2 - a1
        b = b2 - b1
        c = c2 - c1
        x1 = ((-b) + ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
        x2 = ((-b) - ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
        x1 = float(x1)
        x2 = float(x2)
        y = a1 * (x1) ** 2 + b1 * x1 + c1
        if x1 == x2:
            print(f"\nSchnittpunkt:\t({x1}|{y})")
        else:
            print(f"\nSchnittpunkte:\t({x1}|{y}), ({x2}|{y})")
    except TypeError:
        print("Die Parabeln schneiden sich nicht")


def streckfaktor_bestimmen():
    try:
        while True:
            try:
                xs = float(input("X-Wert Scheitelpunkt:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                ys = float(input("Y-Wert Scheitelpunkt:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                xp = float(input("X-Wert 2. Punkt:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        while True:
            try:
                yp = float(input("Y-Wert 2. Punkt:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        a = (yp - ys) / ((xp - xs) ** 2)
        d = -xs
        e = ys
        if d >= 0 and e >= 0:
            result = "\nScheitelform:\t\t{}(x + {})^2 + {}".format(a, d, e)
        elif d <= 0 and e >= 0:
            result = "\nScheitelform:\t\t{}(x {})^2 + {}".format(a, d, e)
        elif d >= 0 and e <= 0:
            result = "\nScheitelform:\t\t{}(x + {})^2 {}".format(a, d, e)
        else:
            result = "\nScheitelform:\t\t{}(x {})^2 {}".format(a, d, e)
        print(result)
        b = -2*a*(-d)
        c = a*((-d)**2)+e
        if b > 0 and c > 0:
            print("Allgemeine Form:\t{}x^2 + {}x + {}".format(a, b, c))
        elif b > 0 and c < 0:
            print("Allgemeine Form:\t{}x^2 + {}x {}".format(a, b, c))
        elif b < 0 and c > 0:
            print("Allgemeine Form:\t{}x^2 {}x + {}".format(a, b, c))
        else:
            print("Allgemeine Form:\t{}x^2 {}x {}".format(a, b, c))
        print("Scheitelpunkt:\t\t({}|{})".format((-d) * 1, e))
        if e > 0 and a > 0 or e < 0 and a < 0:
            x1 = ((-b) + ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
            x2 = ((-b) - ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
            if 0 >= e:
                if x1 == x2:
                    nullstellen = f"Nullstelle:\t({x1}|0)"
                else:
                    nullstellen = f"Nullstellen:\t({x1}|0), ({x2}|0)"
                print(nullstellen)
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


while True:
    xpoints = []
    ypoints = []
    table = PrettyTable(["Option", "Nummer"])
    table.add_row(["f(x) = m * x + c", "= 1"])
    table.add_row(["f(x) = a * (x - d)^2 + e", "= 2"])
    table.add_row(["f(x) = a * x^2 + b * x + c", "= 3"])
    table.add_row(["f(x) = wurzel(a * x - d) + e", "= 4"])
    table.add_row(["f(x) = a^(x + d) + e", "= 5"])
    table.add_row(["f(x) = log basis(x - d) + e", "= 6"])
    table.add_row(["-------------------------------", "---"])
    table.add_row(["Schnittpunkt Geraden", "= 7"])
    table.add_row(["Schnittpunkte Parabeln\n(aus Scheitelform)", "= 8"])
    table.add_row(["Schnittpunkte Parabeln\n(aus allgemeiner Form)", "= 9"])
    table.add_row(["-------------------------------", "---"])
    table.add_row(["Parabelgleichung aus 2 Punkten", "= 10"])
    print(table)
    funktionstyp = input("Option: ")
    table = PrettyTable(["X-Werte", "Y-Werte"])
    print("")
    if funktionstyp == "1":
        linear_funktion()
        print("\n\n")
    elif funktionstyp == "2":
        quadratic_funktion()
        print("\n\n")
    elif funktionstyp == "3":
        quadratic_funktion2()
        print("\n\n")
    elif funktionstyp == "4":
        root_funktion()
        print("\n\n")
    elif funktionstyp == "5":
        exponential_funktion()
        print("\n\n")
    elif funktionstyp == "6":
        logarithmic_funktion()
        print("\n\n")
    elif funktionstyp == "7":
        schnittpunkt_lineare_gleichung()
        print("\n\n")
    elif funktionstyp == "8":
        schnittpunkt_quadratische_gleichung1()
        print("\n\n")
    elif funktionstyp == "9":
        schnittpunkt_quadratische_gleichung2()
        print("\n\n")
    elif funktionstyp == "10":
        streckfaktor_bestimmen()
        print("\n\n")
    else:
        print("\n\n")
