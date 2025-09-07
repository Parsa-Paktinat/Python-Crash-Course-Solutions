from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().strip()

for line in contents.splitlines():
    print(line)

# This line below will do the same as previous lines
for line in path.read_text().strip().splitlines():
    print(line)
