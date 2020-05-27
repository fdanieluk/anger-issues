from forbiddenfruit import curse

def difference(self, other):
	iterable = set(self)
	return iterable.difference(other)

curse(list, "difference", difference)

