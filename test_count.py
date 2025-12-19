from collections import Counter
import ast

# Initialize a counter
pair_counter = Counter()

# Open the file
with open('results_test.txt', 'r') as f:
    lines = f.readlines()

# Iterate over lines, only processing lines with lists of tuples
for line in lines:
    line = line.strip()
    if line.startswith('['):  # Only process the tuple lists
        pairs = ast.literal_eval(line)  # Safely convert string to Python list of tuples
        pair_counter.update(pairs)

# Print the counts
for pair, count in pair_counter.items():
    print(f"{pair}: {count}")
