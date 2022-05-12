# Sort elements by frequency
from audioop import reverse


arr = [2, 5, 2, 8, 5, 6, 8, 8]
size = len(arr)

frequencies = {}
for i in range(size):
    if arr[i] not in frequencies:
        frequencies[arr[i]] = 1
    else:
        frequencies[arr[i]] += 1

freqData = sorted(frequencies.items(), reverse=True, key=lambda x: x[1])
output = []
for data in freqData:
    temp = [data[0] for _ in range(data[1])]
    output += temp

print(f"""
Input: {arr}
Output: {output}
""")