"""Simple finance calculator application."""

from __future__ import annotations

import argparse


def _require_non_negative(value: float, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _require_positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def simple_interest(principal: float, annual_rate_percent: float, years: float) -> float:
    _require_non_negative(principal, "principal")
    _require_non_negative(annual_rate_percent, "annual_rate_percent")
    _require_non_negative(years, "years")
    return principal * annual_rate_percent * years / 100


def compound_amount(
    principal: float,
    annual_rate_percent: float,
    compounds_per_year: int,
    years: float,
) -> float:
    _require_non_negative(principal, "principal")
    _require_non_negative(annual_rate_percent, "annual_rate_percent")
    _require_positive(compounds_per_year, "compounds_per_year")
    _require_non_negative(years, "years")

    rate = annual_rate_percent / 100
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)


def loan_emi(principal: float, annual_rate_percent: float, months: int) -> float:
    _require_non_negative(principal, "principal")
    _require_non_negative(annual_rate_percent, "annual_rate_percent")
    _require_positive(months, "months")

    monthly_rate = annual_rate_percent / (12 * 100)
    if monthly_rate == 0:
        return principal / months

    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Finance Calculator Application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    simple = subparsers.add_parser("simple-interest", help="Calculate simple interest")
    simple.add_argument("principal", type=float)
    simple.add_argument("annual_rate_percent", type=float)
    simple.add_argument("years", type=float)

    compound = subparsers.add_parser("compound-amount", help="Calculate compound amount")
    compound.add_argument("principal", type=float)
    compound.add_argument("annual_rate_percent", type=float)
    compound.add_argument("compounds_per_year", type=int)
    compound.add_argument("years", type=float)

    emi = subparsers.add_parser("loan-emi", help="Calculate monthly EMI")
    emi.add_argument("principal", type=float)
    emi.add_argument("annual_rate_percent", type=float)
    emi.add_argument("months", type=int)

    return parser


def main() -> None:
    parser = _create_parser()
    args = parser.parse_args()

    if args.command == "simple-interest":
        result = simple_interest(args.principal, args.annual_rate_percent, args.years)
    elif args.command == "compound-amount":
        result = compound_amount(
            args.principal,
            args.annual_rate_percent,
            args.compounds_per_year,
            args.years,
        )
    else:
        result = loan_emi(args.principal, args.annual_rate_percent, args.months)

    print(f"{result:.2f}")


if __name__ == "__main__":
    main()
