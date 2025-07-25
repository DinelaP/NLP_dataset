import re

def is_separator_line(line, length=80):
    return line.strip() == "=" * length

def should_remove_tip_line(line):
    # Uklanja ako linija počinje sa (TIP i završava sa )
    return re.match(r'^\(TIP.*\)$', line.strip()) is not None

def clean_author_line(line):
    # Ako linija počinje sa Autor(i): i završava nepotrebnom zagradom, ukloni je
    if line.strip().startswith("Autor(i):") and line.strip().endswith(")"):
        return re.sub(r'\)\s*$', '', line)
    return line

def replace_separator_lines(input_file, output_file, separator_length=80, replacement="<***>"):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []

    # ➊ Dodaj <***> na početak fajla sa praznim redom ispred
    new_lines.append("\n" + replacement + "\n")

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ➋ Preskoči linije koje sadrže 'Tekst:'
        if 'Tekst:' in stripped:
            i += 1
            continue

        # ➌ Preskoči linije koje počinju sa (TIP ... )
        if should_remove_tip_line(stripped):
            i += 1
            continue

        # ➍ Ako je linija separator, dodaj prazan red pa <***>
        if is_separator_line(stripped, separator_length):
            new_lines.append("\n" + replacement + "\n")
            
        # ➎ Ako je linija Autor(i): ..., očisti višak zagrade i dodaj prazan red
        elif stripped.startswith("AUTOR(I):"):
            cleaned_line = clean_author_line(line)
            new_lines.append(cleaned_line)
            new_lines.append("\n")
        else:
            new_lines.append(line)

        i += 1

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(new_lines)

    print(f"Zamjena završena! Novi fajl sačuvan kao '{output_file}'.")
    

# Poziv funkcije:
replace_separator_lines('Dokumenti5.txt', 'dokumenti5v.txt')
