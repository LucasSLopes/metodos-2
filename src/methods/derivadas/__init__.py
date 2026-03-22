from src.core.function_parser import ScalarFunction

from .convergence import ConvergenceResult, convergence_study
from .selector import get_formula


def differentiate(
    f: ScalarFunction,
    x: float,
    h: float,
    derivative_order: int,
    method: str,
    error_order: int,
) -> float:
    """Compute a numerical derivative using finite differences.

    Args:
        f:                The function to differentiate.
        x:                Point of evaluation.
        h:                Step size (must not be zero).
        derivative_order: 1 or 2.
        method:           'forward', 'backward', or 'central'.
        error_order:      Desired truncation error order (1 - 4).

    Returns:
        Approximate derivative value.

    Raises:
        ValueError: if h is zero or the combination is unsupported.
    """
    if h == 0:
        raise ValueError("Step size h must not be zero.")
    formula = get_formula(derivative_order, method, error_order)
    return formula(f, x, h)


def study_convergence(
    f: ScalarFunction,
    x: float,
    h0: float,
    derivative_order: int,
    method: str,
    error_order: int,
    tol: float = 1e-8,
    max_iter: int = 50,
) -> ConvergenceResult:
    """Run a convergence study without manually selecting the formula.

    Args:
        f:                The function to differentiate.
        x:                Point of evaluation.
        h0:               Initial step size (must not be zero).
        derivative_order: 1 or 2.
        method:           'forward', 'backward', or 'central'.
        error_order:      Desired truncation error order (1 - 4).
        tol:              Relative error tolerance for stopping.
        max_iter:         Maximum number of iterations.

    Returns:
        ConvergenceResult with per-iteration data.
    """
    formula = get_formula(derivative_order, method, error_order)
    return convergence_study(f=f, x=x, h0=h0, formula=formula, tol=tol, max_iter=max_iter)


__all__ = [
    "ConvergenceResult",
    "convergence_study",
    "differentiate",
    "get_formula",
    "study_convergence",
]
