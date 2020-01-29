
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    4: "April",
}

print(monthConversions["Jan"])
print(monthConversions.get("Mar"))
print(monthConversions.get(4))

# if the key is not found, we can use get and set the second parameter to a default printed value if the key is not found
print(monthConversions.get("Dec", "No key found"))