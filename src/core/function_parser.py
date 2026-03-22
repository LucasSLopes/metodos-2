from collections.abc import Callable

from sympy import Symbol, sympify
from sympy.core.sympify import SympifyError
from sympy.utilities.lambdify import lambdify

ScalarFunction = Callable[[float], float]


def parse_function(expr: str) -> ScalarFunction:
    """Parse a math expression string into a callable f(x) -> float.

    Supports any expression that sympy understands: sin, cos, exp, sqrt, log,
    pi, E, and all standard math functions.

    Raises:
        ValueError: if the expression is empty or has invalid syntax.
    """
    if not expr.strip():
        raise ValueError("Expression must not be empty.")

    x = Symbol("x")
    try:
        symbolic = sympify(expr, locals={"x": x})
    except SympifyError as exc:
        raise ValueError(f"Invalid expression: {exc}") from exc

    return lambdify(x, symbolic, modules="math")
