pytexnum
========

A short python library to simplify the handling of numbers in scientific notation. Designed for use in sympytex.


Usage
-----

Create a `texnum` object
```python
>>> from pytexnum import texnum
>>> a = texnum(5.5,6)
>>> b = texnum(4500000)
>>> a
texnum(5.5, 6)
>>> b
texnum(4.5, 6)
```

Use them the way you would use any other number
```python
>>> a + b
texnum(1.0, 7)
>>> a - b
texnum(1.0, 6)
>>> a * b
texnum(2.475, 13)
>>> a / b
texnum(1.22222222222, 0)
```

Get a LaTeX string representation
```python
>>> a.tex()
'5.50\times10^{6}'
```

If writing the number in scientific notation would result in 10^a, where a is
between -1 and 1, the number is not printed in scientific notation. Override
this with the argument `display='scientific'`, or by using the `naturalPowers`
argument.
```python
>>> texnum(5).tex()
'5.00'
>>> texnum(5).tex(display='scientific')
'5.00\times10^{0}'
>>> texnum(50).tex()
'50.0'
>>> texnum(50).tex(naturalPowers={0})
'5.00\times10^{1}'
```

If the mantissa is 1, it won't be printed.
Override this with the argument `full=True`.
```python
>>> texnum(1,5).tex()
'10^{5}'
>>> texnum(1,5).tex(full=True)
'1.00\times10^{5}'
```

The default is 3 significant figures, but you can specify how many you want.
```python
>>> texnum(5.4321,6).tex()
'5.43\times10^{6}'
>>> texnum(5.4321,6).tex(5)
'5.4321\times10^{6}'
>>> texnum(5.4321,6).tex(sigfigs=5)
'5.4321\times10^{6}'
```

You should be able to use standard math functions, but these won't return a
texnum object.
```python
>>> import math
>>> math.sqrt(a)
2345.207879911715
```

If you want a texnum object, you can use the `.call()` method
```python
>>> a.call(math.sqrt)
texnum(2.34520787991, 3)
```

If you want to access the individual pieces of the number use
`.ma()`, `.ex()`, and `.nu()`
```python
>>> a.ma()
5.5
>>> a.ex()
6
>>> a.nu()
5500000.0
```