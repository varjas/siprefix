# SIPrefix
## Introduction
SIPrefix converts numbers between varied orders of magnitude and SI prefix based magnitudes.

Large or small numbers can be scaled to between 10⁰ and 10³ with a corresponding SI prefix. Scaled numbers with an SI prefix can be converted back to the full magnitude representation.

These functions allow for improved visualization of large or small numbers, and enable easy use of numbers with SI prefixes in calculations.

To use SIPrefix, clone the repository and import the module:
```python
from siprefix import siprefix
```

## Usage
SIPrefix only uses SI prefixes that are separated by 3 orders of magnitude, including:

Y, Z, E, P, T, G, M, k, (base), c, m, µ, n, p, f, a, z, y

Hecto- (h), deca- (da), deci- (d), centi- (c), and any non-SI prefixes are not used in SIPrefix.

### Value Scaling
Scales input value to within 10⁰ and 10³ with a corresponding SI prefix. (Scaling can exceed 10³ if input is beyond range of SI prefix magnitudes)

```python
siprefix.scale(value, combined=True)
```

#### Base Order Input
The `value` parameter can be a `float`, `int`, `Decimal`, or `str` type.

The function will output a `str` with the scaled number and prefix separated by a space.

If the `combined` argument is set to `False`, the function will output a tuple containing a `float` of the scaled number and a `str` of the prefix.

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
Use of non-base order input requires the value and prefix to be combined into a single `str` type. The value and prefix are not required to be separated by a space.

```python
siprefix.scale('0.0000005 a')
# '500.0 m'

siprefix.scale('0.0000005a')
# '500.0 m'

siprefix.scale('9000000 m')
# '9.0 k'

siprefix.scale('9000000 m', False)
# (9.0, 'k')
```

### Value Expansion
Expands input value with SI prefix to full scale representation.

```python
siprefix.scale(value)
```

The `value` parameter should be a `str` type to include an associated SI prefix. The prefix can directly follow the number without a space. The function will not expand any values if the parameter is a `float`, `int`, or `Decimal` type.

The function will output a `float` of the expanded number.

```python
siprefix.expand('500 m')
# 0.5

siprefix.expand('9 K')
# 9000.0

siprefix.expand('30')
# 30.0

siprefix.expand('400.0 f')
# 0.0000000000004
```

### Considerations
Sorting of values should be done prior to scaling as magnitude differences will not be handled correctly in the output `str` type.

The tuple output option is included to allow for easier formatting of the output values.

SIPrefix does not handle units at all. There are many other packages capable of this functionality (see Resources section below). Inclusion of units in some cases will lead to errors due to overlap with SI prefixes. For instance, including the 'meter' abbreviation 'm' as input will cause incorrect scaling/expansion due to treating the unit as the 'milli' prefix.

If units are required, they should be removed from the input value and appended after scaling.

## Resources
- [SIPrefix GitLab](https://gitlab.com/varjas/siprefix)
- [SIPrefix GitHub](https://github.com/varjas/siprefix)
- [Magnitude Library](https://github.com/juanre/magnitude)
- [Metric prefix - Wikipedia](https://wikipedia.org/wiki/Metric_prefix)

## License
Code released under the [MIT License](LICENSE.md).

