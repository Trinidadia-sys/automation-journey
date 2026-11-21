HOT_BUDGET = 5000
HOT_TIMELINE_DAYS = 30


def grade_lead(budget, days_until_start):
	"""Classify a lead as hot, warm, or cold."""
	has_good_budget = budget >= HOT_BUDGET
	has_short_timeline = days_until_start <= HOT_TIMELINE_DAYS

	if has_good_budget and has_short_timeline:
		return "hot"
	if has_good_budget or has_short_timeline:
		return "warm"
	return "cold"


def main():
	leads = {"hot": [], "warm": [], "cold": []}

	while True:
		name = input("Lead name: ").strip()
		if name.lower() == "done":
			break
		if not name:
			print("Please enter a lead name.")
			continue

		try:
			budget = float(input("Budget: ").replace("$", "").replace(",", ""))
			days_until_start = int(input("Days until start: "))
			if budget < 0 or days_until_start < 0:
				raise ValueError
		except ValueError:
			print("Enter a valid non-negative budget and number of days; try again.")
			continue

		leads[grade_lead(budget, days_until_start)].append(name)

	print("\nSummary")
	for category in ("hot", "warm", "cold"):
		names = leads[category]
		detail = f" ({', '.join(names)})" if names else ""
		print(f"{category.capitalize()}: {len(names)}{detail}")


if __name__ == "__main__":
	main()
