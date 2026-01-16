def main():
    def celsius_a_fahrenheit(c):
        return (c * 9/5) + 32

    def kelvin_a_fahrenheit(k):
        return (k - 273.15) * 9/5 + 32

    def fahrenheit_a_celsius(f):
        return (f - 32) * 5/9

    def kelvin_a_celsius(k):
        return k - 273.15

    def celsius_a_kelvin(c):
        return c + 273.15

    def fahrenheit_a_kelvin(f):
        return (f - 32) * 5/9 + 273.15

    try:
        temp = float(input("Ingrese la temperatura: "))
        origen = input("Unidad de origen (C/F/K): ").upper()
        destino = input("Unidad de destino (C/F/K): ").upper()
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    result = 0

    if origen == destino:
        result = temp
    elif origen == 'C' and destino == 'F':
        result = celsius_a_fahrenheit(temp)
    elif origen == 'C' and destino == 'K':
        result = celsius_a_kelvin(temp)
    elif origen == 'F' and destino == 'C':
        result = fahrenheit_a_celsius(temp)
    elif origen == 'F' and destino == 'K':
        result = fahrenheit_a_kelvin(temp)
    elif origen == 'K' and destino == 'C':
        result = kelvin_a_celsius(temp)
    elif origen == 'K' and destino == 'F':
        result = kelvin_a_fahrenheit(temp)
    else:
        print("Unidad no válida.")
        return

    print(f"{temp:.1f}°{origen} = {result:.2f}°{destino}")

if __name__ == "__main__":
    main()