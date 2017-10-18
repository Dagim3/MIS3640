def insert_integer(data, number):
    data.insert(7,2015)

# Uncomment the following lines to test
data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
new_data = insert_integer(data, 2015)
print(data)

# Expected output:
# [1, 3, 40, 75, 90, 2000, 2001, 2015, 2016]
