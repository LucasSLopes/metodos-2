from collections.abc import Callable

from .first_derivative import (
    _first_backward_o1,
    _first_backward_o2,
    _first_backward_o3,
    _first_backward_o4,
    _first_central_o2,
    _first_central_o4,
    _first_forward_o1,
    _first_forward_o2,
    _first_forward_o3,
    _first_forward_o4,
)
from .second_derivative import (
    _second_backward_o1,
    _second_backward_o2,
    _second_backward_o3,
    _second_backward_o4,
    _second_central_o2,
    _second_central_o4,
    _second_forward_o1,
    _second_forward_o2,
    _second_forward_o3,
    _second_forward_o4,
)

_FORMULAS: dict[tuple[int, str, int], Callable] = {
    (1, "forward", 1): _first_forward_o1,
    (1, "forward", 2): _first_forward_o2,
    (1, "forward", 3): _first_forward_o3,
    (1, "forward", 4): _first_forward_o4,
    (1, "backward", 1): _first_backward_o1,
    (1, "backward", 2): _first_backward_o2,
    (1, "backward", 3): _first_backward_o3,
    (1, "backward", 4): _first_backward_o4,
    (1, "central", 2): _first_central_o2,
    (1, "central", 4): _first_central_o4,
    (2, "forward", 1): _second_forward_o1,
    (2, "forward", 2): _second_forward_o2,
    (2, "forward", 3): _second_forward_o3,
    (2, "forward", 4): _second_forward_o4,
    (2, "backward", 1): _second_backward_o1,
    (2, "backward", 2): _second_backward_o2,
    (2, "backward", 3): _second_backward_o3,
    (2, "backward", 4): _second_backward_o4,
    (2, "central", 2): _second_central_o2,
    (2, "central", 4): _second_central_o4,
}

_VALID_METHODS = {"forward", "backward", "central"}
_VALID_ORDERS = {1, 2}
_VALID_ERROR_ORDERS = {1, 2, 3, 4}


def get_formula(derivative_order: int, method: str, error_order: int) -> Callable:
    """Return the finite difference formula for the given combination.

    Raises:
        ValueError: if any argument is invalid or the combination does not exist.
    """
    if derivative_order not in _VALID_ORDERS:
        raise ValueError(f"derivative_order must be 1 or 2, got {derivative_order}.")
    if method not in _VALID_METHODS:
        raise ValueError(f"method must be one of {sorted(_VALID_METHODS)}, got '{method}'.")
    if error_order not in _VALID_ERROR_ORDERS:
        raise ValueError(f"error_order must be 1 - 4, got {error_order}.")

    key = (derivative_order, method, error_order)
    if key not in _FORMULAS:
        raise ValueError(
            f"No formula for derivative_order={derivative_order}, "
            f"method='{method}', error_order={error_order}. "
            f"Central differences only support error orders 2 and 4."
        )
    return _FORMULAS[key]
