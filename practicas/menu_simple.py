importar sistema

este_python = sys.version_info[:2]
versión mínima = (3, 9)
si este_python < min_version:
    partes_del_mensaje = [
        "Este script no funciona en Python {}.{}.".format(*this_python),
        "La versión mínima compatible de Python es {}.{}.".format(*min_version),
        "Utilice https://bootstrap.pypa.io/pip/{}.{}/get-pip.py en su lugar".format(*this_python),
    ]
    imprimir("ERROR: " + " ".join(partes_del_mensaje))
    sys.exit(1)
