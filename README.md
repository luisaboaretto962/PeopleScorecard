# People Scorecard Demo

A small Python script that computes gender representation indicators for a people scorecard, using **synthetic data only**.

This is a personal demo project built in 2026 to illustrate how a quarterly people scorecard can be structured. It does not contain, and was not built from, any real company data.

## What it computes

Five headline indicators:

- Overall women share
- Women share in early and mid career
- Women share in senior career
- Women share of hires
- Women share of promotions

It also shows the women share broken down by function.

## How it works

- `make_employees()` generates a list of synthetic employee records with a fixed random seed, so results are reproducible.
- `scorecard()` calculates the five headline indicators.
- `breakdown()` calculates the women share for any field, such as function or country.

The script uses only the Python standard library.

## How to run

Requires Python 3.8 or later.


## Notes

- All data is randomly generated. Results have no business meaning.
- The indicator definitions are a simplified model, not a reference implementation.
