from src.core.function_parser import ScalarFunction


def _first_forward_o1(f: ScalarFunction, x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h


def _first_forward_o2(f: ScalarFunction, x: float, h: float) -> float:
    return (-3.0 * f(x) + 4.0 * f(x + h) - f(x + 2.0 * h)) / (2.0 * h)


def _first_forward_o3(f: ScalarFunction, x: float, h: float) -> float:
    return (-11.0 * f(x) + 18.0 * f(x + h) - 9.0 * f(x + 2.0 * h) + 2.0 * f(x + 3.0 * h)) / (
        6.0 * h
    )


def _first_forward_o4(f: ScalarFunction, x: float, h: float) -> float:
    return (
        -25.0 * f(x)
        + 48.0 * f(x + h)
        - 36.0 * f(x + 2.0 * h)
        + 16.0 * f(x + 3.0 * h)
        - 3.0 * f(x + 4.0 * h)
    ) / (12.0 * h)


def _first_backward_o1(f: ScalarFunction, x: float, h: float) -> float:
    return (f(x) - f(x - h)) / h


def _first_backward_o2(f: ScalarFunction, x: float, h: float) -> float:
    return (3.0 * f(x) - 4.0 * f(x - h) + f(x - 2.0 * h)) / (2.0 * h)


def _first_backward_o3(f: ScalarFunction, x: float, h: float) -> float:
    return (11.0 * f(x) - 18.0 * f(x - h) + 9.0 * f(x - 2.0 * h) - 2.0 * f(x - 3.0 * h)) / (
        6.0 * h
    )


def _first_backward_o4(f: ScalarFunction, x: float, h: float) -> float:
    return (
        25.0 * f(x)
        - 48.0 * f(x - h)
        + 36.0 * f(x - 2.0 * h)
        - 16.0 * f(x - 3.0 * h)
        + 3.0 * f(x - 4.0 * h)
    ) / (12.0 * h)


def _first_central_o2(f: ScalarFunction, x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2.0 * h)


def _first_central_o4(f: ScalarFunction, x: float, h: float) -> float:
    return (-f(x + 2.0 * h) + 8.0 * f(x + h) - 8.0 * f(x - h) + f(x - 2.0 * h)) / (12.0 * h)
