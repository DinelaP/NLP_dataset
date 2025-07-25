def pretvori_kljuceve_u_velika(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key_upper = key.strip().upper()
            value = value.rstrip('\n').strip()
            output_lines.append(f"{key_upper}: {value}\n")
        else:
            output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(output_lines)

    print(f"Gotovo! Novi fajl sa velikim ključevima sačuvan je kao '{output_file}'.")


# ✅ Poziv funkcije:
pretvori_kljuceve_u_velika('dokumentn4.txt', 'dokument1.txt')
