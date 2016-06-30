from collections import Counter

c = Counter()

for ch in 'ProgramMing':
	c[ch] = c[ch]+1

print c