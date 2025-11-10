"""Module providing a function to generate numbers from text and sum them."""

import re
from typing import Callable, Generator


def generator_numbers(context: str) -> Generator[float, None, None]:
    """
    Analyzes text, finds all valid numbers (int and float),
    and returns them as a generator.

    Args:
        text (str): Input string to analyze.

    Returns:
        Generator[float, None, None]: A generator yielding the found numbers as floats.
    """

    # Regex to find integers or floats (e.g., "1000" or "1000.01")
    # \d+       - one or more digits (integer part)
    # (?:\.\d+)? - optional non-capturing group for decimal part
    pattern = r"\d+(?:\.\d+)?"

    # Use finditer for memory-efficient iteration
    for match in re.finditer(pattern, context):
        # Yield the matched number string, converted to float
        yield float(match.group(0))


def sum_profit(
    text: str, func: Callable[[str], Generator[float, None, None]]
) -> float:
    """
    Calculates the total profit by summing numbers from a generator function.

    Args:
        text (str): The text to be passed to the generator.
        func (Callable): The generator function (e.g., generator_numbers) to use.

    Returns:
        float: The total sum of the numbers found.
    """
    # Call the generator function and sum its output directly
    return sum(func(text))


# --- Example Usage ---
SAMPLE_TEXT = (
    "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, "
    "доповнений додатковими надходженнями 27.45 і 324.00 доларів."
)
total_income = sum_profit(SAMPLE_TEXT, generator_numbers)
print(f"Загальний дохід: {total_income}")
