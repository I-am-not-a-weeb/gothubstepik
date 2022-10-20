from commit import *
import pytest

def  test_silnia():
	foo = [1,2,3,4,5]
	baa = [1,2,6,24,120]
	for a,b in zip(foo,baa):
		assert silnia(a) == b


