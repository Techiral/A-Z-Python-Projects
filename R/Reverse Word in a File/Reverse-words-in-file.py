filename = input("Enter the filename to read: ")
output_filename = input("Enter the filename to write: ")

with open(filename) as file:
  text = file.read()

words = text.split()

with open(output_filename, "w") as file:
  for word in words[::-1]:
    file.write(word + " ")

print("Words in reverse order written to file successfully.")
