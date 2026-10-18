from pprint import pprint

from mean_var_std import calculate


if __name__ == "__main__":
    example = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    pprint(calculate(example))

    # Check the required error for a list with fewer than nine numbers.
    try:
        calculate([1, 2, 3])
    except ValueError as error:
        print(f"Validation test passed: {error}")
