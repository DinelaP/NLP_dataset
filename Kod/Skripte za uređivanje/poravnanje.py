import re

def justify_text(line_words, width=180):
    if not line_words:
        return '' 
    if len(line_words) == 1:
        return line_words[0].ljust(width)

    total_chars = sum(len(word) for word in line_words)
    total_spaces = width - total_chars
    spaces_between_words = total_spaces // (len(line_words) - 1)
    extra_spaces = total_spaces % (len(line_words) - 1)

    justified_line = ""
    for i, word in enumerate(line_words[:-1]):
        justified_line += word
        justified_line += ' ' * spaces_between_words
        if i < extra_spaces:
            justified_line += ' '
    justified_line += line_words[-1]
    return justified_line


def process_block_text(text, width=80):
    words = text.split()
    lines = []
    current_line_words = []
    current_len = 0

    for word in words:
        if current_len + len(word) + len(current_line_words) > width:
            lines.append(justify_text(current_line_words, width))
            current_line_words = [word]
            current_len = len(word)
        else:
            current_line_words.append(word)
            current_len += len(word)
    if current_line_words:
        lines.append(' '.join(current_line_words))

    return '\n'.join(lines)


def justify_txt_file(input_file, output_file, width=80):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    inside_block = False
    block_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("DATUM:"):
            line = re.sub(r'\s*-\s*\d{1,2}:\d{2},?', '', line)
            line = re.sub(r'(\d{2}\.\d{2})\.(\d{2})\.', r'\1.20\2.', line)

        if stripped.startswith("AUTOR(I):"):
            inside_block = True
            output_lines.append(line)
            output_lines.append('\n')
            block_lines = []
        elif inside_block:
            if stripped == "<***>":
                block_text = ''.join(block_lines)
                justified_text = process_block_text(block_text, width)
                output_lines.append(justified_text + '\n\n')
                output_lines.append(line)
                inside_block = False
            else:
                block_lines.append(line)
        else:
            output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(output_lines)

    print(f"Gotovo! Poravnani tekst je sačuvan u '{output_file}'.")

# Poziv funkcije:
justify_txt_file('clancisport3.txt', 'clancisport4.txt', width=120)