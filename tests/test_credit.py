import pytest

from credit import calculate_risk


@pytest.mark.parametrize(
    ("income", "debt", "expected"),
    [
        (1000, 700, "HIGH"),
        (1000, 400, "MEDIUM"),
        (1000, 100, "LOW"),
    ],
)
def test_standard_risk_cases(income, debt, expected):
    assert calculate_risk(income, debt, 30) == expected


@pytest.mark.parametrize("income", [0, -1000])
def test_invalid_income(income):
    assert calculate_risk(income, 100, 30) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0, 30) == "LOW"


def test_ratio_exactly_zero_point_three():
    assert calculate_risk(1000, 300, 30) == "LOW"


def test_ratio_exactly_zero_point_six():
    assert calculate_risk(1000, 600, 30) == "MEDIUM"
