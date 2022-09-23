from pathlib import Path
#
# base = Path.home()
# guia = Path(base, "Europa", "Espana", Path("Barcelona", "Sagrada_Familia.txt"))
#
# print(base)
# print(guia.parent)
# print(guia.parent.parent)
# print(guia.parent.parent.parent)

# guia = Path("Europa")
# 
# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)

guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
euro = guia.relative_to(Path("Europa"))
spain = guia.relative_to(Path("Europa", "España"))

print(euro)
print(spain)