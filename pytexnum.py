from math import log10

class texnum(object):
    def __init__(self, mantissa, exponent=None):
        self.__update(mantissa, exponent)
    
    # Used to mutate self
    def __update(self,mantissa,exponent=None):
        if exponent is None:
            if isinstance(mantissa,texnum):
                self._mantissa = mantissa._mantissa
                self._exponent = mantissa._exponent
                self._num = mantissa._num
            else:
                self._num = mantissa
                if self._num == 0:
                    self._exponent = 0
                else:
                    self._exponent = int(log10(abs(self._num)))
                self._mantissa = float(self._num) / 10 ** self._exponent
        else:
            if not (1 <= abs(mantissa) < 10):
                exp = int(log10(abs(mantissa))) - 1
                self._mantissa = float(mantissa) / 10**exp
                self._exponent = exponent + exp
            else:
                self._mantissa = mantissa
                self._exponent = exponent
                self._num = mantissa * 10 ** exponent
    
    # Display these numbers a variety of ways
    def __repr__(self):
        return 'texnum({}, {})'.format(self._mantissa, self._exponent)
    #def __str__(self):
    #    return '{}*10^{}'.format(self._mantissa, self._exponent)
    def __str__(self):
        return str(self._num)
    def tex(self,sigfigs=3,naturalPowers={-2,-1,0,1,2},display='auto',full=False):
        # Figure out the display mode
        if display == 'auto':
            display = 'natural' if self._exponent in naturalPowers else 'scientific'
        elif display not in {'scientific','natural'}:
            raise ValueError('Invalid parameter {} in texnum.tex() call'.
                    format(display))
        
        # Do the displaying
        dispmant = '{{0:.{}f}}'.format(sigfigs-1).format(float(self._mantissa))
        if display == 'scientific':
            if self._mantissa == 1 and not full:
                return '10^{{{}}}'.format(self._exponent)
            return r'{}\times10^{{{}}}'.format(dispmant, self._exponent)
        elif display == 'natural':
            if -1 < self._num < 1:
                dispmant = '{{0:.{}f}}'.format(sigfigs).format(float(self._mantissa))
            return str(float(dispmant)*10**self._exponent)
        else:
            raise Error('It should not be possible to get here')
    
    # Get each of the parts
    def nu(self): return self._num
    def ma(self): return self._mantissa
    def ex(self): return self._exponent
    
    # Make calling other math functions easy, if they don't already work
    def call(self, func):
        return texnum(func(self._num))
    
    # Unary operators
    def __neg__(self):
        return texnum(-self._mantissa, self._exponent)
    def __abs__(self):
        return texnum(abs(self._mantissa), self._exponent)
    
    # Basic operators
    def __add__(self,other):
        return texnum(self._num + other)
    def __radd__(self,other):
        return texnum(other + self._num)
    def __sub__(self,other):
        return texnum(self._num - other)
    def __rsub__(self,other):
        return texnum(other - self._num)
    def __mul__(self,other):
        return texnum(self._num * other)
    def __rmul__(self,other):
        return texnum(other * self._num)
    def __div__(self,other):
        return texnum(float(self._num) / other)
    def __rdiv__(self,other):
        return texnum(other / float(self._num))
    def __floordiv__(self,other):
        return texnum(float(self._num) // other)
    def __rfloordiv__(self,other):
        return texnum(other // float(self._num))
    
    # The assignment operators (+= -+ etc.)
    def __iadd__(self,other):
        self.__update(self._num + other)
        return self
    def __isub__(self,other):
        self.__update(self._num - other)
        return self
    def __imul__(self,other):
        self.__update(self._num * other)
        return self
    def __idiv__(self,other):
        self.__update(self._num / other)
        return self
    def __ifloordiv__(self,other):
        self.__update(self._num // other)
        return self
    
    # Pow is a little more complicated
    def __pow__(self,power):
        return texnum(self._num ** power)
    def __rpow__(power,other):
        return texnum(other ** power._num)
    
    # Type conversion
    def __complex__(self):
        return complex(self._num)
    def __int__(self):
        return int(self._num)
    def __long__(self):
        return long(self._num)
    def __float__(self):
        return float(self._num)
    

class ctexnum(texnum):
    def __str__(self):
        return str(float(self))
