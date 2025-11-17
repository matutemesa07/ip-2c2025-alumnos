items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)     # copiamos los valores iniciales
    n = len(items)
    i = 0
    j = 0                  # arrancamos desde el primer par

def step():
    global items, n, i, j

    # Si ya terminamos todas las pasadas
    if i >= n - 1:
        return {"done": True}

    # Mientras no llegamos al final de esta pasada
    if j < n - i - 1:
        a = j
        b = j + 1

        # Comparamos
        if items[a] > items[b]:
            # swap real
            items[a], items[b] = items[b], items[a]
            j += 1
            return {"a": a, "b": b, "swap": True, "done": False}

        # si no hay swap, igual avanzamos
        j += 1
        return {"a": a, "b": b, "swap": False, "done": False}

    # Si llegamos al final de esta pasada: reseteamos j y pasamos al siguiente i
    i += 1
    j = 0
    return {"a": 0, "b": 0, "swap": False, "done": False}
