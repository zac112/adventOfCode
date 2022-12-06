from collections import deque
with open("data.txt") as f:
    data = f.read()

bufsize = 14
buffer = deque(data[:bufsize], maxlen=bufsize)

for i, char in enumerate(data, 1):
    buffer.append(char)
    if len(set(buffer))==bufsize:
        print(f"{''.join(buffer)} at character {i}")
        break
