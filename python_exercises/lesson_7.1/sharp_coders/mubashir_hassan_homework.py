filename = "1375SacadatHasanMantaw.Yazid.FASDH2025012-urd1"

with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()


matching_lines = [line.strip() for line in lines if "###" in line]

print("All lines with '###':")
for heading in matching_lines:
    print(heading)

print("\nFirst three headings:")
for heading in matching_lines[:3]:
    print(heading)

first_level_heading = []

print("\nWord count and first-level heading detection:")
for heading in matching_lines:
    words = heading.replace("###", "").strip().split()
    count_words = len(words)

    print(f"\nHeading: {heading}")
    print(f"Count of words in this heading: {count_words}")

    pipe_count = heading.count("|")
    if pipe_count == 1:
        first_level_heading.append(heading)

print("\nFirst-level headings:")
for heading in first_level_heading:
    print(heading)
