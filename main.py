import pandas as pd
from src.core.function_parser import parse_function
from src.methods.derivadas import study_convergence


def main():
    f = parse_function("sqrt(exp(3*x) + 4*x**2)")
    result = study_convergence(
        f, x=2, h0=0.5, derivative_order=2, method="backward", error_order=4
    )
    df = pd.DataFrame(
        {
            "Δ(k)": result.steps,
            "f(x)": result.f_values,
            "f''(x)": result.derivatives,
            "e(x)": result.errors,
        }
    )
    print(df)


if __name__ == "__main__":
    main()
