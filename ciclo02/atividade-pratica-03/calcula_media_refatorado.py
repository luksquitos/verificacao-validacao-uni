# Fase Refactor (Refatoração do algoritmo)

def calcular_media_refatorado(nota1, nota2, nota3):
    # função com validação caso a entrada seja 
    # de um tipo não desejado ou valores negativos.
    notas = [nota1, nota2, nota3]
    for nota in notas:
        if not isinstance(nota, (int, float)) or nota < 0:
            raise ValueError("As notas devem ser números não negativos.")
    return sum(notas) / 3
