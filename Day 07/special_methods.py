class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Albun: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Delete successfully")


mi_cd = CD('ACDC', "Black in Blac", 10)
print(mi_cd)
print(len(mi_cd))
del mi_cd