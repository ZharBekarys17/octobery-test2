## Strings

# Mandatory problems:


# String Concatenation:
# Concatenate the strings 'Python', 'is', 'a', 'powerful', 'language' to create a single string, 'Python is a powerful language.'
first_word = 'Python '
secound_word = 'is '
third_word = 'a '
fourth_word = 'powerful '
final_word =  'language'
print(first_word + secound_word+ third_word + fourth_word +final_word)
# Variable Declaration:
# Declare a variable named topic and assign it the value "strings in Python."
topic = "strings in Python."
print(topic)
# Printing with Escape Symbols:
# Print the following sentence, including the double quotes: "Learning about "Python" strings is fun."
topic = "Learning about \"Python\" strings is fun."
print(topic)
# String Length and Character Count:
# Calculate and print the length of the topic string. Also, count and print how many times the letter 's' appears in the string.
topic = "Learning about Python strings is fun."
print(f"{len(topic)} is integer lens and 's' appears in the string {topic.count('s')}")
# Uppercase and Lowercase Conversion:
# Create a new variable called upper_topic by converting the topic string to uppercase. Then, create another variable called lower_topic by converting the topic string to lowercase.
topic = "Learning about Python strings is fun."
lower_topic = topic.lower()
upper_topic = topic.upper()
print(f'{lower_topic} ,\n{upper_topic}')
# String Formatting:
# Use f-strings to format the topic string in the following way: "Let's learn about {topic}."
topic = "Learning about Python strings is fun."
print(f"Let's learn about {topic}.")
# Substring Extraction:
# Extract and print the word 'Python' from the topic string.
topic = "Learning about Python strings is fun."
print(topic[14:21])


## Bonus problems


# Substring Search:
# Check if the topic string contains the word 'Python' using the in keyword.
topic = "Learning about Python strings is fun."
print('Python' in topic)
# String Replacement:
# Replace the word 'Python' in the topic string with 'programming' and print the modified string.
topic = "Learning about Python strings is fun."
print(topic.replace('Python', 'programming'))
# String Splitting:
# Split the string 'Python,Java,C++,Ruby' into a list of programming languages using a comma as the separator.
IT_languages = 'Python,Java,C++,Ruby'
print(IT_languages.split(' ,'))
# Character at Index:
# Find and print the character at index 4 in the topic string.
topic = "Learning about Python strings is fun."
print(topic[4])
# String Repetition:
# Create a new string that repeats the word 'Python' three times, separated by hyphens.
topic2  = "Python " * 3
print(topic2) 
# Escape Symbols in String:
# Create a string that contains a newline character to print the following text on separate lines:
# Hello,
# World!
topic3 = 'Hello,\nWorld!'
print(topic3)
# String Capitalization:
# Capitalize the first letter of each word in the string 'python programming is amazing.'
top4 = 'python programming is amazing.'
print(top4.title())
# String Removal and Trimming:
# Remove any leading or trailing whitespace from the string '  Python For All ' and print the trimmed result.
final_topic = '  Python For All '
print(final_topic.strip())


