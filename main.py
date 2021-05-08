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
                    table = PrettyTable(["X-Werte", "Y-Werte"])
                    table.add_row([x, m*x+c])
                    print(table)
                    # print("{}\t\t|\t\t{}".format(x, m * x + c))
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
        while True:
            try:
                exponent = float(input("Exponent:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        function = "f(x) = {}(x - {})^{} + {}".format(a, d, exponent, e)
        scheitelpunkt = "S({}|{})".format(d * 1, e)
        print(function)
        if exponent % 2 == 0:
            print(scheitelpunkt)
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
            # dict[x] = a * (x - d)**exponent + e
            # xpoints.append(x)
            # ypoints.append(a * (x - d)**exponent + e)
            table.add_row([x, a * (x - d)**exponent + e])
            x += inkrement
        print(table)
        # for x_wert, y_wert in dict.items():
        # print("{}\t\t|\t\t{}".format(x_wert, y_wert))
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Werte", "Y-Werte"])
                    table.add_row([x, a * (x - d)**exponent + e])
                    print(table)
                    # print("{}\t\t|\t\t{}".format(x, a * (x - d)**exponent + e))
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
        # for x_wert, y_wert in dict.items():
        # print("{}\t\t|\t\t{}".format(x_wert, y_wert))
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Werte", "Y-Werte"])
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
        # dict = {"x": "y"}
        while x <= bis_x:
            if x <= 0:
                table.add_row([x, 1 / (basis ** (-x - d)) + e])
                x += inkrement
            else:
                # dict[x] = (a * x - d)**(1/float(root)) + e
                # xpoints.append(x)
                # ypoints.append((a * x - d)**(1/float(root)) + e)
                table.add_row([x, basis**(x - d) + e])
                x += inkrement
        print(table)
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Werte", "Y-Werte"])
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
        # for x_wert, y_wert in dict.items():
        # print("{}\t\t|\t\t{}".format(x_wert, y_wert))
        while True:
            response = input("\nNoch ein spezieller X-Wert? ").lower()
            if response != "nein":
                try:
                    x = float(response)
                    table = PrettyTable(["X-Werte", "Y-Werte"])
                    table.add_row([x, math.log(x-d, basis) + e])
                    print(table)
                except ValueError:
                    break
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def nullstellen1():
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
        # print(f"{m1}x + {c1} = {m2}x + {c2}\t| -{c1}")
        # print(f"{m1}x + = {m2}x + {c2 - c1}\t\t| -{m2}x")
        # print(f"{m1 - m2}x = {c2 - c1}\t\t\t| :{m1 - m2}")
        # print(f"x = {(c2 - c1) / (m1 - m2)}")
        schnittpunkt_x = (c2 - c1) / (m1 - m2)
        schnittpunkt_y = m1 * schnittpunkt_x + c1
        print("S({} | {})".format(schnittpunkt_x, schnittpunkt_y))
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("Die Geraden sind paralell")


def quadratic_equation1():
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
        while True:
            try:
                y = float(input("Auflösen nach:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        a = a
        b = -2 * a * d
        c = a * (d ** 2) + e
        c -= y
        x1 = ((-b) + ((b**2) - (4 * a * c))**(0.5))/(2 * a)
        x2 = ((-b) - ((b**2) - (4 * a * c))**(0.5))/(2 * a)
        result = "\nAllgemeine Form:\t{}x^2 + {}x + {}".format(a, b, c)
        print(result)
        if x1 == x2:
            print("Schnittpunkt: {}".format(x1))
        elif x1 > x2:
            x1, x2 = x2, x1
            print("x1 = {}\nx2 = {}".format(x1, x2))
        else:
            print("x1 = {}\nx2 = {}".format(x1, x2))
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")


def quadratic_equation2():
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
        while True:
            try:
                y = float(input("Auflösen nach:\t"))
                break
            except ValueError:
                print("Bitte eine Zahl eingeben")
        a = a
        d = b/(2*a)
        e = c - ((b**2)/(4*a))
        if d >= 0 and e >= 0:
            result = "\nScheitelform:\t{}(x + {})^2 + {}".format(a, d, e)
        elif d <= 0 and e >= 0:
            result = "\nScheitelform:\t{}(x {})^2 + {}".format(a, d, e)
        elif d >= 0 and e <= 0:
            result = "\nScheitelform:\t{}(x + {})^2 {}".format(a, d, e)
        else:
            result = "\nScheitelform:\t{}(x {})^2 {}".format(a, d, e)
        print(result)
        c -= y
        x1 = ((-b) + ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
        x2 = ((-b) - ((b ** 2) - (4 * a * c)) ** (0.5)) / (2 * a)
        if x1 == x2:
            print("Schnittpunkt: {}".format(x1))
        elif x1 > x2:
            x1, x2 = x2, x1
            print("x1 = {}\nx2 = {}".format(x1, x2))
        else:
            print("x1 = {}\nx2 = {}".format(x1, x2))
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")


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
        print("Parabelstreckung:\t{}".format((yp-ys)/(xp-xs)**2))
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def zu_scheitelform():
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
        a = a
        d = b/(2*a)
        e = c - ((b**2)/(4*a))
        if d >= 0 and e >= 0:
            result = "\nScheitelform:\t{}(x + {})^2 + {}".format(a, d, e)
        elif d <= 0 and e >= 0:
            result = "\nScheitelform:\t{}(x {})^2 + {}".format(a, d, e)
        elif d >= 0 and e <= 0:
            result = "\nScheitelform:\t{}(x + {})^2 {}".format(a, d, e)
        else:
            result = "\nScheitelform:\t{}(x {})^2 {}".format(a, d, e)
        print(result)
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


def zu_allgemeine_form():
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
        a = a
        b = -2*a*d
        c = a*(d**2)+e
        if b >= 0 and c >= 0:
            result = "\nAllgemeine Form:\t{}x^2 + {}x + {}".format(a, b, c)
        elif b <= 0 and c >= 0:
            result = "\nAllgemeine Form:\t{}x^2 {}x + {}".format(a, b, c)
        elif b >= 0 and c <= 0:
            result = "\nAllgemeine Form:\t{}x^2 + {}x {}".format(a, b, c)
        else:
            result = "\nAllgemeine Form:\t{}x^2 {}x {}".format(a, b, c)
        print(result)
    except OverflowError:
        print("OverflowError: (34, 'Result too large')")
    except ZeroDivisionError:
        print("ZeroDivisionError: float division by zero")


while True:
    xpoints = []
    ypoints = []
    table = PrettyTable(["Option", "Nummer"])
    table.add_row(["f(x) = m * x + c", "= 1"])
    table.add_row(["f(x) = a * (x - d)^exponent + e", "= 2"])
    table.add_row(["f(x) = wurzel(a * x - d) + e", "= 3"])
    table.add_row(["f(x) = a^(x + d) + e", "= 4"])
    table.add_row(["f(x) = log basis(x - d) + e", "= 5"])
    table.add_row(["-------------------------------", "---"])
    table.add_row(["Nullstellen lineare funktion", "= 6"])
    table.add_row(["Lineare Gleichung lösen\n(aus Scheitelform)", "= 7"])
    table.add_row(["Quadratische Gleichung lösen\n(aus allgemeiner Form)", "= 8"])
    table.add_row(["-------------------------------", "---"])
    table.add_row(["Parabelstreckung bestimmen", "= 9"])
    table.add_row(["Allgemeine Form zu Scheitelform", "= 10"])
    table.add_row(["Scheitelform zu Allgemeine Form", "= 11"])
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
        root_funktion()
        print("\n\n")
    elif funktionstyp == "4":
        exponential_funktion()
        print("\n\n")
    elif funktionstyp == "5":
        logarithmic_funktion()
        print("\n\n")
    elif funktionstyp == "6":
        nullstellen1()
        print("\n\n")
    elif funktionstyp == "7":
        quadratic_equation1()
        print("\n\n")
    elif funktionstyp == "8":
        quadratic_equation2()
        print("\n\n")
    elif funktionstyp == "9":
        streckfaktor_bestimmen()
        print("\n\n")
    elif funktionstyp == "10":
        zu_scheitelform()
        print("\n\n")
    elif funktionstyp == "11":
        zu_allgemeine_form()
        print("\n\n")
    else:
        print("\n\n")
