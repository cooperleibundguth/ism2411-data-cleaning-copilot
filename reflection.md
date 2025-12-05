What Copilot generated
"I used GitHub Copilot to generate the skeleton for `load_data` and `clean_column_names`. I wrote descriptive comments above the function signatures (what and why) which prompted Copilot to generate suggested code for `pd.read_csv` and string replacements."

What I modified
"I changed Copilot’s suggestions to include `low_memory=False` in `read_csv`, added `.str.replace('-', '_')` to the column cleaning, and wrapped operations with `df = df.copy()` for safety purposes. For missing values Copilot proposed filling with 0 I changed that to a configurable strategy and used drop by default to preserve data quality."

What I learned about data cleaning
"I learned the importance of coercing numeric columns with `pd.to_numeric(..., errors='coerce')` before dropping and the trade-offs between dropping vs imputing missing values I also learned how inconsistent column names and trailing whitespace cause subtle bugs."

What I learned about Copilot
"Copilot is great for boilerplate but it sometimes assumes ideal column names or an ideal dataset structure.Copilot suggested `df['price']` directly; I adjusted it to search among candidate column names because my CSV used `Unit Price` sometimes. This demonstrates Copilot’s value as a productivity tool but not a drop in replacement for code review."
