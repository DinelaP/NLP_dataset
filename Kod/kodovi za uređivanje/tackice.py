import re

def ocisti_tekst(tekst):
    ociscene_linije = []
    for linija in tekst.splitlines():
        # Ukloni vodeću numeraciju i oznake: 1., 1.1.3., 3), a), (1)
        linija = re.sub(r'^\s*((\d+(\.\d+)*[.)]?|[a-zA-Z][)]|\(\d+\))\s*)+', '', linija)

        # Ukloni vodeće simbole: -, ✓, , , •, ▪, ►, itd.
        linija = re.sub(r'^\s*[-✓•▪►–—●‣⦿⚫]+\s*', '', linija)

        # Ukloni višestruke razmake
        linija = re.sub(r'\s+', ' ', linija).strip()

        if linija:
            ociscene_linije.append(linija)
    return '\n'.join(ociscene_linije)


def ocisti_i_spremi(ulazna_putanja, izlazna_putanja):
    with open(ulazna_putanja, "r", encoding="utf-8") as f:
        tekst = f.read()

    ociscen_tekst = ocisti_tekst(tekst)

    with open(izlazna_putanja, "w", encoding="utf-8") as f:
        f.write(ociscen_tekst)

    print(f"Tekst je očišćen i spremljen kao '{izlazna_putanja}'.")

ocisti_i_spremi("dokumenti4_pdf.txt", "dokumentn4.txt")
