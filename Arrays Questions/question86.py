# Pattern Searching
text = "AABAACAADAABAABA"
pattern = "AABA"
size = len(text)
window = len(pattern)

for i in range(size):
    window_text = []
    if (window+i) <= size:
        for j in range(i, window+i):
            window_text.append(text[j])
        txt = "".join(window_text)
        if pattern == txt:
            print(f"{pattern} found at index {i}.")
