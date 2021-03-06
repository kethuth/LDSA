#!/usr/bin/env python3
import json
import sys
import re
"""Mapping occurances of Swedish pronouns in tweets"""

count = 0  # Number of total unique tweets read from process.
nouns = ['han', 'hon', 'det', 'den', 'denne', 'denna', 'hen']  # Designated words to map


for line in sys.stdin:
    if not line == '\n':
        json_line = json.loads(line)
        try:  # Using error when searching with a missing key
            json_line['retweeted_status']
        except KeyError:
            clean_text = re.sub(r'[^\w\s]', ' ', json_line['text']) # Remove punctuations
            for word in clean_text.lower().split():
                if word in nouns:
                    print('%s\t%s' % (word, 1))  # Printing out touples to std.in
            count += 1
print("count\t", (count))
