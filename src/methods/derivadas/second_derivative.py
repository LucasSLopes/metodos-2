from src.core.function_parser import ScalarFunction


def _second_forward_o1(f: ScalarFunction, x: float, h: float) -> float:
    return (f(x + 2.0 * h) - 2.0 * f(x + h) + f(x)) / (h * h)


def _second_forward_o2(f: ScalarFunction, x: float, h: float) -> float:
    return (2.0 * f(x) - 5.0 * f(x + h) + 4.0 * f(x + 2.0 * h) - f(x + 3.0 * h)) / (h * h)


def _second_forward_o3(f: ScalarFunction, x: float, h: float) -> float:
    return (
        35.0 * f(x)
        - 104.0 * f(x + h)
        + 114.0 * f(x + 2.0 * h)
        - 56.0 * f(x + 3.0 * h)
        + 11.0 * f(x + 4.0 * h)
    ) / (12.0 * h * h)


def _second_forward_o4(f: ScalarFunction, x: float, h: float) -> float:
    return (
        45.0 * f(x)
        - 154.0 * f(x + h)
        + 214.0 * f(x + 2.0 * h)
        - 156.0 * f(x + 3.0 * h)
        + 61.0 * f(x + 4.0 * h)
        - 10.0 * f(x + 5.0 * h)
    ) / (12.0 * h * h)


def _second_backward_o1(f: ScalarFunction, x: float, h: float) -> float:
    return (f(x) - 2.0 * f(x - h) + f(x - 2.0 * h)) / (h * h)


def _second_backward_o2(f: ScalarFunction, x: float, h: float) -> float:
    return (2.0 * f(x) - 5.0 * f(x - h) + 4.0 * f(x - 2.0 * h) - f(x - 3.0 * h)) / (h * h)


def _second_backward_o3(f: ScalarFunction, x: float, h: float) -> float:
    return (
        35.0 * f(x)
        - 104.0 * f(x - h)
        + 114.0 * f(x - 2.0 * h)
        - 56.0 * f(x - 3.0 * h)
        + 11.0 * f(x - 4.0 * h)
    ) / (12.0 * h * h)


def _second_backward_o4(f: ScalarFunction, x: float, h: float) -> float:
    return (
        45.0 * f(x)
        - 154.0 * f(x - h)
        + 214.0 * f(x - 2.0 * h)
        - 156.0 * f(x - 3.0 * h)
        + 61.0 * f(x - 4.0 * h)
        - 10.0 * f(x - 5.0 * h)
    ) / (12.0 * h * h)


def _second_central_o2(f: ScalarFunction, x: float, h: float) -> float:
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)


def _second_central_o4(f: ScalarFunction, x: float, h: float) -> float:
    return (-f(x + 2.0 * h) + 16.0 * f(x + h) - 30.0 * f(x) + 16.0 * f(x - h) - f(x - 2.0 * h)) / (
        12.0 * h * h
    )
