"""LC 68 - Text Justification"""
def full_justify(words, maxWidth):
    lines = []
    line, line_len = [], 0
    for word in words:
        if line_len + len(word) + len(line) > maxWidth:
            lines.append(line)
            line, line_len = [], 0
        line.append(word)
        line_len += len(word)
    lines.append(line)  # last line
    result = []
    for i, line in enumerate(lines):
        if i == len(lines)-1 or len(line) == 1:
            result.append(' '.join(line).ljust(maxWidth))
        else:
            total_spaces = maxWidth - sum(len(w) for w in line)
            gaps = len(line) - 1
            space, extra = divmod(total_spaces, gaps)
            row = line[0]
            for j in range(1, len(line)):
                row += ' ' * (space + (1 if j <= extra else 0)) + line[j]
            result.append(row)
    return result

if __name__ == "__main__":
    cases = [
        (["This","is","an","example","of","text","justification."], 16),
        (["What","must","be","acknowledgment","shall","be"], 16),
        (["Science","is","what","we","understand","well","enough","to","explain"], 20),
    ]
    for words, w in cases:
        print(f"maxWidth={w}:")
        for line in full_justify(words, w):
            print(f"  |{line}|")
