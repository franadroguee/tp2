import random

alumnos = [
    {"apellido": "Garcia",    "nombre": "Ana",    "nota": 9},
    {"apellido": "Lopez",     "nombre": "Bruno",  "nota": 3},
    {"apellido": "Martinez",  "nombre": "Carla",  "nota": 8},
    {"apellido": "Rodriguez", "nombre": "Diego",  "nota": 4},
    {"apellido": "Sanchez",   "nombre": "Elena",  "nota": 7},
    {"apellido": "Torres",    "nombre": "Franco", "nota": 5},
    {"apellido": "Fernandez", "nombre": "Gisela", "nota": 9},
    {"apellido": "Gomez",     "nombre": "Hugo",   "nota": 2},
    {"apellido": "Diaz",      "nombre": "Iris",   "nota": 6},
    {"apellido": "Perez",     "nombre": "Juan",   "nota": 1},
]


def cifrar_alumno(nombre, apellido):
    DESPLAZAMIENTO = 3  # constante local, no se pasa como parámetro

    def cifrar(texto):
        resultado = ""
        for c in texto.upper():
            if c.isalpha():
                resultado += chr((ord(c) - ord('A') + DESPLAZAMIENTO) % 26 + ord('A'))
            else:
                resultado += c
        return resultado

    return cifrar(nombre), cifrar(apellido)


def asignar_grupos(alumnos):
    # Ordenar de mayor a menor nota
    ordenados = sorted(alumnos, key=lambda x: x["nota"], reverse=True)
    n = len(ordenados)
    disponibles = list(range(n))
    grupos = []

    while len(disponibles) >= 2:
        # Tomar el de mayor nota disponible
        idx_alto = disponibles.pop(0)
        alto = ordenados[idx_alto]

        # Criterio probabilístico: más peso a los de nota baja
        pesos = [1 / (ordenados[i]["nota"] + 1) for i in disponibles]
        idx_bajo = random.choices(disponibles, weights=pesos, k=1)[0]
        disponibles.remove(idx_bajo)
        bajo = ordenados[idx_bajo]

        nc_a, ac_a = cifrar_alumno(alto["nombre"], alto["apellido"])
        nc_b, ac_b = cifrar_alumno(bajo["nombre"], bajo["apellido"])

        grupos.append([
            {"nc": nc_a, "ac": ac_a},
            {"nc": nc_b, "ac": ac_b},
        ])

    # Si n es impar, el sobrante va al último grupo (grupo de 3)
    if disponibles:
        sobrante = ordenados[disponibles[0]]
        nc, ac = cifrar_alumno(sobrante["nombre"], sobrante["apellido"])
        grupos[-1].append({"nc": nc, "ac": ac})

    return grupos


def consultar_grupo(apellido, grupos):
    DESPLAZAMIENTO = 3  # constante local

    def descifrar(texto):
        resultado = ""
        for c in texto.upper():
            if c.isalpha():
                resultado += chr((ord(c) - ord('A') - DESPLAZAMIENTO) % 26 + ord('A'))
            else:
                resultado += c
        return resultado

    def cifrar(texto):
        resultado = ""
        for c in texto.upper():
            if c.isalpha():
                resultado += chr((ord(c) - ord('A') + DESPLAZAMIENTO) % 26 + ord('A'))
            else:
                resultado += c
        return resultado

    apellido_cifrado = cifrar(apellido)

    for i, grupo in enumerate(grupos):
        for miembro in grupo:
            if miembro["ac"] == apellido_cifrado:
                print(f"\nGrupo {i + 1}:")
                for m in grupo:
                    print(f"  {descifrar(m['nc'])} {descifrar(m['ac'])}")
                return

    print("Alumno no encontrado.")


# --- Programa principal ---
print("=== ASIGNACIÓN DE GRUPOS ===\n")
grupos = asignar_grupos(alumnos)

print("Grupos (nombres en cifrado César):")
for i, grupo in enumerate(grupos):
    integrantes = " | ".join(f"{m['nc']} {m['ac']}" for m in grupo)
    print(f"  Grupo {i + 1}: {integrantes}")

print("\n=== CONSULTA ===")
apellido_buscar = input("Ingresá el apellido del alumno: ")
consultar_grupo(apellido_buscar, grupos)

"""
*Cómo funciona:*
• `cifrar_alumno` — cifra con César, DESPLAZAMIENTO es local
• `asignar_grupos` — ordena por nota, el de nota alta se empareja probabilísticamente con uno de nota baja (mayor peso = más chance de ser elegido)
• `consultar_grupo` — buscás por apellido real, te muestra el grupo descifrado sin notas
• Si hay número impar de alumnos, el sobrante va al último grupo (quedan 3)

Completen con sus datos reales en la variable `alumnos` 👍

"""