print("Filter out vowel using two lists")
# filter() method example
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = []
my_string = "Hello World"
for character in my_string:
    if character not in vowels:
        consonants.append(character)
print(consonants)

print("\nFilter out vowels using lambda and filter")
consonants_2 = filter(lambda x: x not in vowels, my_string)
print(f"The result of filter when converted to a string: "
      f"{list(consonants_2)}")

# filter returns an object of type filter, a special iterator. Since
# we have already printed it as a list once, we have exhausted the
# iterator. It will not print again.
print(f"\nFilter returns an object of type {type(consonants_2)}")
print(f"The result of filter when converted to a string: "
      f"{list(consonants_2)}")