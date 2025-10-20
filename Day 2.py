
paragraph = """
Python is a powerful programming language that is easy to learn.
This Python course covers the basics and advanced concepts,
helping students become confident Python developers.
"""


length = len(paragraph)
print("Length of paragraph:", length)


print("First character:", paragraph[0])
print("Last character:", paragraph[-1])


preview = paragraph[:50]
print("Preview (first 50 characters):")
print(preview)


updated_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:")
print(updated_paragraph)


lowercase_paragraph = updated_paragraph.lower()
print("\nLowercase version:")
print(lowercase_paragraph)


trimmed_paragraph = lowercase_paragraph.strip()


words = trimmed_paragraph.split()
print("\nList of words:")
print(words)


if "course" in words:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is not found in the paragraph.")


print("\nThe course description is {} characters long and has {} words."
      .format(len(trimmed_paragraph), len(words)))
