import csv

def save_summary_to_csv(summary_data, file_path):
    with open(file_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Kategoria', 'Wartość'])
        for key, value in summary_data.items():
            writer.writerow([key, value])

def calculation_percent(amount, downed):
    percent = (downed / amount) * 100
    percent = round(percent, 2)
    return percent

def calculation_amount(amount, downed):
    downed_amount = amount - downed
    return downed_amount

def feed_amount(feed, downed_amount):
    feed_waste = feed / downed_amount
    feed_waste = round(feed_waste, 2)
    return feed_waste
