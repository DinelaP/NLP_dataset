import re
import unicodedata

def naslov_u_slug(naslov):
    naslov = unicodedata.normalize('NFKD', naslov).encode('ascii', 'ignore').decode('ascii')
    naslov = re.sub(r'[^a-zA-Z0-9\s-]', '', naslov) 
    naslov = re.sub(r'\s+', '-', naslov.strip())  
    return naslov.lower()

def formatiraj_datum(datum_str):
    dan, mjesec, godina = datum_str.strip('.').split('.')
    return f"{godina}/{mjesec.zfill(2)}/{dan.zfill(2)}"

def zamijeni_stranu_i_pretvori_u_veliko(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    datum = ""
    naslov = ""
    output_lines = []

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key_upper = key.strip().upper()
            value = value.rstrip('\n').strip()

            if key_upper == "DATUM":
                datum = value
            elif key_upper == "NASLOV":
                naslov = value

            if key_upper == "STRANA":
                try:
                    datum_url = formatiraj_datum(datum)
                    slug = naslov_u_slug(naslov)
                    link = f"https://tip.ba/{datum_url}/{slug}/"

                    # Piši samo link bez broja ispred
                    nova_linija = f"{key_upper}: {link}\n"
                except Exception as e:
                    print(f"Greška kod generisanja linka: {e}")
                    nova_linija = f"{key_upper}: {value}\n"
                output_lines.append(nova_linija)
            else:
                output_lines.append(f"{key_upper}: {value}\n")
        else:
            # Ostavlja linije bez ':' kakve jesu (npr. prazan red)
            output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(output_lines)

    print(f"Gotovo! Novi fajl sa linkovima i velikim slovima sačuvan je kao '{output_file}'.")



zamijeni_stranu_i_pretvori_u_veliko('clancisport.txt', 'clancisport3.txt')
