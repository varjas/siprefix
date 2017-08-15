# SIPrefix
## Introduction
SIPrefix provides functions for converting full scale numbers to the nearest appropriate SI prefix scale, and expanding values with SI prefixes to full scale.

To use SIPrefix, clone the repository and import the module:
```python
import siprefix
```

## Usage
SIPrefix only uses SI prefixes that are 3 orders of magnitude apart, including:

Y, Z, E, P, T, G, M, k, (base), c, m, µ, n, p, f, a, z, y

### Value Scaling
```python
siprefix.scale(value, combined=True)
```

#### Base Order Input
The `value` parameter can be a `float`, `int`, `Decimal`, or `str` type.

The function will output a `str` with the scaled number and prefix; or a tuple containing a `float` of the scaled number and a `str` of the prefix if the second argument is set to `False`.

```python
# float
siprefix.scale(0.5)
# '500.0 m'

# int
siprefix.scale(9000)
# '9.0 k'

# Decimal
siprefix.scale(Decimal(30))
# '30.0'

# str
siprefix.scale('0.0000000000004')
# '400.0 f'

# Tuple output
siprefix.scale(0.5, False)
# (500.0, 'm')
```

#### Non-Base Order Input
Use of non-base order input requires the value and prefix to be combined into a single string.
The `value` parameter can be a `str`.

```python
siprefix.scale('0.0000005 a')
# '500.0 m'

siprefix.scale('9000000 m')
# '9.0 k'

siprefix.scale('9000000 m', False)
# (9.0, 'k')
```

#### Design
Sorting of values should be done prior to scaling to `str` output with prefixes as magnitude differences will not be handled correctly.

The tuple output option in the `scale()` function is included to allow for easier formatting of the output values.

SIPrefix does not handle units at all. There are many other packages capable of this functionality (see Resources section below). Inclusion of units in some cases will lead to errors due to overlap with SI prefixes. For instance, including the 'meter' abbreviation 'm' as input into `scale()` function will cause incorrect scaling due to treating the unit as the 'milli' prefix.

If units are required, they should be removed from the input value and appended after scaling.

### Value Expansion
```python
siprefix.scale(value)
```

The `value` parameter must be a `str` type.

The function will output a `float` of the expanded number.

```python
siprefix.expand('0.5 m')
# 0.5

siprefix.expand('9 K')
# 9000.0

# Decimal
siprefix.expand('30')
# 30.0

siprefix.expand('400.0 f')
# 0.0000000000004
```

## Resources
- [SIPrefix GitLab](https://www.gitlab.com)
- [SIPrefix GitHub](https://www.github.com)

## License
Code released under the [MIT License](LICENSE.md).

