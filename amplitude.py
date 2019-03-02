import cmath
import matplotlib.pyplot as plot
j = 1j
pi = 3.141592654


def input_numbers():
    num = int(input("num"))
    den = int(input("den"))
    z = num / den
    return z


def number_coeff():
    coeff_array = list()

    coeff = int(input("Anzahl coeff"))

    print("Werte der Koeffizienten")
    for i in range(int(coeff)):
        n = input("coeff:")
        coeff_array.append(float(n))
    print("Koeffizienten: ", coeff_array)
    return coeff_array


def number_omega():
    omega_array = list()

    omega = int(input("Anzahl"))

    print("Omega: [pi]")
    for k in range(int(omega)):
        num = int(input("num"))
        den = int(input("den"))
        o = (num / den) * pi if den != 0 else 0
        omega_array.append(o)
    print("Omegas: ", omega_array)
    return omega_array


def absolute_value(coeff_array, omega_array):
    absolute_array = list()
    for o in omega_array:
        result = 0
        for i in range(len(coeff_array)):
            result += coeff_array[i] * (cmath.cos(o) + j * cmath.sin(o))**(len(coeff_array) - i - 1)
        absolute_array.append(result)
    return absolute_array


if __name__ == "__main__":
    coeff_array = number_coeff()
    omega_array = number_omega()
    absolute_array = absolute_value(coeff_array, omega_array)
    print(absolute_array)

    plot.plot(omega_array, absolute_array)
    plot.show()
