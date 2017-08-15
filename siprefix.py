import math
# Return prefix or scale based on one input
# Only handles prefixes separated by 3 orders of magnitude
def siConvert(order=None, prefix=None):
	# Require at least one argument
	if prefix is None and order is None:
		raise TypeError('siConvert() missing at least 1 positional argument: \'order\' or \'prefix\'')
	# Define prefix, scale relations
	data = {
		'Y': 24,
		'Z': 21,
		'E': 18,
		'P': 15,
		'T': 12,
		'G': 9,
		'M': 6,
		'k': 3,
		'': 0,
		'm': -3,
		'µ': -6,
		'n': -9,
		'p': -12,
		'f': -15,
		'a': -18,
		'z': -21,
		'y': -24
	}
	# If prefix is set
	if prefix is not None:
		# Return scale
		try:
			return data[prefix]
		# Unless prefix is not found
		except KeyError:
			raise KeyError("invalid 'prefix' defined")
	# If scale is set
	if order is not None:
		# Return prefix
		try:
			return next((k for k, v in data.items() if v == order))
		# Unless scale is not found
		except StopIteration:
			raise KeyError("invalid 'order' defined")

# Returns scaled value with SI prefix
def scale(value, combined=True):
	# Set starting order
	if type(value) == str:
		# Expand number
		value = expand(value)

	value = float(value)
	
	# Get number of non-decimal digits
	order = int(math.log(abs(value)))
	# Convert order to multiple of 3
	order = math.floor(order / 3) * 3

	# Attempt to get prefix from order
	prefix = siConvert(order=order)

	if combined is True:
		# Return scaled value and SI prefix as string
		return (str(value) + ' ' + prefix).strip()
	elif combined is False:
		# Return scaled value and SI prefix as tuple
		return (value, prefix)

# Returns expanded value in base scale
def expand(value):
	# Set starting order
	order = 0
	if type(value) == str:
		# Determine order if prefix is included
		if value[-1].isalpha():
			prefix = value[-1]
			order = siConvert(prefix=prefix)
			# Remove prfix from value string
			value = value[:-1].strip()

	value = float(value)

	# Scale value by order of magnitude determined
	value = value * 10 ** order

	return value
