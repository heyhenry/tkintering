import json
import random

# Open the JSON file with the correct encoding
with open('quotes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  # Use json.load() to read from the file
    quotes = data['quotes']
    
    # # Loop through each quote in the quotes list and print it
    # for quote in quotes:
    #     print(f"Quote: {quote['quote']}, Author: {quote['author']}")
    the_quote = random.choice(quotes)
    print(f'{the_quote['quote']} - {the_quote['author']}')