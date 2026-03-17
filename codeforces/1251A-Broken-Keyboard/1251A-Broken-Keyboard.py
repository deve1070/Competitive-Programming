for _ in range(int(input())):
	s=input()
	print(''.join(c for c in sorted(set(s)) if s.count(c)>2*s.count(c+c)))