my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

count_of_o = 0
for i in my_string:
    if i == "o":
        count_of_o = count_of_o + 1

print("Count of 'o' in above string is {}".format(count_of_o))

# print(my_string.count("o"))
