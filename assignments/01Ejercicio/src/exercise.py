def main():
    # Escribe tu código abajo de esta línea
    def horas(hr, mn, s):
        s += hr * 3600 + mn * 60
        return s

    print("proceso 1:")

    hr = int(input("Introduce las horas: "))
    mn = int(input("Introduce los minutos: "))
    s = int(input("Introduce los segundos: "))

    print("\nproceso 2:")

    hr2 = int(input("Introduce las horas: "))
    mn2 = int(input("Introduce los minutos: "))
    s2 = int(input("Introduce los segundos: "))

    print("proceso 1:", horas(hr, mn, s))
    print("proceso 2:", horas(hr2, mn2, s2))

if __name__ == '__main__':
    main()
