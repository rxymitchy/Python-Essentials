

#Dictionaries = maps a key to a value
customer = {
    "name": "John Smith",
    "age": 30,
    "its_verified": True
}
print("Dictionaries are used in this section:")
print(customer["name"])
print(customer["age"])
print(customer.get("birthdate", "Jan 1 1960"))
customer["name"] = "Jack Smith"
print(customer["name"])

del customer["age"]
print(customer)


#phone number example
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"

}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#emojis
message = input(">")
words = message.split(' ')
emojis = { }

print(words)



