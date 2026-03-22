from collections.abc import Callable
from dataclasses import dataclass, field

from src.core.function_parser import ScalarFunction

DerivativeFormula = Callable[[ScalarFunction, float, float], float]


@dataclass
class ConvergenceResult:
    iterations: list[int] = field(default_factory=list)
    steps: list[float] = field(default_factory=list)
    f_values: list[float] = field(default_factory=list)
    derivatives: list[float] = field(default_factory=list)
    errors: list[float] = field(default_factory=list)


def convergence_study(
    f: ScalarFunction,
    x: float,
    h0: float,
    formula: DerivativeFormula,
    tol: float = 1e-8,
    max_iter: int = 50,
) -> ConvergenceResult:
    """Repeatedly halve h and recompute the derivative until convergence.

    Args:
        f:        The function to differentiate.
        x:        Point of evaluation.
        h0:       Initial step size.
        formula:  A finite difference formula callable (f, x, h) -> float.
        tol:      Relative error tolerance for stopping.
        max_iter: Maximum number of iterations.

    Returns:
        ConvergenceResult with per-iteration data.
    """
    if h0 == 0:
        raise ValueError("Initial step h0 must not be zero.")

    result = ConvergenceResult()
    fx = f(x)
    h = h0
    prev: float | None = None

    for k in range(1, max_iter + 1):
        current = formula(f, x, h)
        result.iterations.append(k)
        result.steps.append(h)
        result.f_values.append(fx)
        result.derivatives.append(current)

        if prev is not None:
            error = abs((current - prev) / current) if current != 0 else abs(current - prev)
            result.errors.append(error)
            if error < tol:
                break
        else:
            result.errors.append(float("nan"))

        prev = current
        h /= 2

    return result
