# Mean-Variance-Standard Deviation Calculator

A Python project that uses NumPy to calculate the mean, variance, standard deviation, maximum, minimum, and sum of a 3 × 3 matrix.

For each statistic, the function returns:
1. Column-wise results
2. Row-wise results
3. A result for all nine values flattened together

## Requirements

- Python 3.8 or newer
- NumPy

## Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the example

```bash
python main.py
```

## Run the tests

```bash
python -m unittest -v test_module.py
```

## Example

```python
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result["mean"])
# [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]
```

The function raises `ValueError("List must contain nine numbers.")` unless the input contains exactly nine numbers.

Created as a freeCodeCamp Data Analysis with Python project.
