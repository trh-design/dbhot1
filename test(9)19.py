class A:
    pass 

class B(A):
    pass

isinstance(A(), A)
type(A()) == A
isinstance(B(), A)
type(B()) == A