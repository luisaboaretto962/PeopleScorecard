import random
from collections import defaultdict

random.seed(42)  # same data every run, so results are reproducible

FUNCTIONS = ["Finance", "Sales", "Engineering", "HR", "Operations", "Marketing"]
COUNTRIES = ["CH", "DE", "IT", "FR", "US"]
BANDS = ["Early", "Mid", "Senior"]


def make_employees(n=600):
    """Create n synthetic employee records."""
    rows = []
    for i in range(n):
        rows.append({
            "id": i,
            "function": random.choice(FUNCTIONS),
            "country": random.choice(COUNTRIES),
            "band": random.choices(BANDS, weights=[4, 3, 2])[0],
            "gender": random.choice(["F", "M"]),
            "hired_this_quarter": random.random() < 0.05,
            "promoted_this_quarter": random.random() < 0.04,
        })
    return rows


def share_women(rows):
    """Share of women in a list of records, or None if the list is empty."""
    if not rows:
        return None
    return sum(r["gender"] == "F" for r in rows) / len(rows)


def scorecard(rows):
    """The five headline indicators."""
    hires = [r for r in rows if r["hired_this_quarter"]]
    promotions = [r for r in rows if r["promoted_this_quarter"]]
    return {
        "Overall women share": share_women(rows),
        "Early/mid career women share": share_women(
            [r for r in rows if r["band"] in ("Early", "Mid")]),
        "Senior career women share": share_women(
            [r for r in rows if r["band"] == "Senior"]),
        "Women share of hires": share_women(hires),
        "Women share of promotions": share_women(promotions),
    }


def breakdown(rows, key):
    """Share of women for each value of a field, e.g. function or country."""
    groups = defaultdict(list)
    for r in rows:
        groups[r[key]].append(r)
    return {value: share_women(members) for value, members in sorted(groups.items())}


if __name__ == "__main__":
    employees = make_employees()

    print("Headline indicators")
    for name, value in scorecard(employees).items():
        print(f"  {name}: {value:.1%}")

    print("\nOverall women share by function")
    for value, share in breakdown(employees, "function").items():
        print(f"  {value}: {share:.1%}")