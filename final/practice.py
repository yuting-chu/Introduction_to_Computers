import csv
from collections import defaultdict

# Function to read the CSV file and return a list of dictionaries
def read_csv(filename):
    singers = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['popularity(millions)'] = int(row['popularity(millions)'])
            row['debut'] = int(row['debut'])
            row['guests'] = row['guests'].split('|')
            singers.append(row)
    return singers

# Function to get popular singers after 2000
def get_popular_singers(singers):
    result = []
    for singer in singers:
        if singer['debut'] >= 2000:
            result.append(singer)
    result.sort(key=lambda x: x['popularity(millions)'], reverse=True)
    return result

# Function to find the most frequent guest singer
def most_frequent_guest(singers):
    guest_count = defaultdict(int)
    for singer in singers:
        for guest in singer['guests']:
            guest_count[guest] += 1
    most_frequent = max(guest_count.items(), key=lambda x: x[1])
    return most_frequent

# Function to find co-guest singer pairs
def co_guest_singer_pairs(singers):
    guest_dict = {singer['singer']: set(singer['guests']) for singer in singers}
    pairs = set()
    for singer, guests in guest_dict.items():
        for guest in guests:
            if singer in guest_dict.get(guest, set()):
                pairs.add(tuple(sorted([singer, guest])))
    return pairs

# Main function to read the file and print the results
def main():
    filename = 'taiwan_popular_singer.csv'
    singers = read_csv(filename)

    # (1) Popular singers after 2000
    popular_singers = get_popular_singers(singers)
    print("(1) popular singers after 2000:")
    for singer in popular_singers:
        print(f"{singer['singer']}: {singer['popularity(millions)']}")

    # (2) Most frequently-appeared guest
    most_frequent = most_frequent_guest(singers)
    print("\n(2) frequently-appeared guest:")
    print(f"{most_frequent[0]}: {most_frequent[1]}")

    # (3) List of co-guest singer pairs
    co_guest_pairs = co_guest_singer_pairs(singers)
    print("\n(3) list of co-guest singer pairs:")
    for pair in sorted(co_guest_pairs):
        print(f"{pair[0]} = {pair[1]}")

# Run the main function
if __name__ == "__main__":
    main()
