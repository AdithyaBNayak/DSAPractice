# Featured Product/ Most Purchased Product
"""
Given the list of product names in a list of sold products
Find the product with max occurences(product sold most times)
If there are two products with similar occurences, 
order them in ascending order and choose the last name
"""

from collections import Counter
products = ['shirt', 'trouser', 'shirt', 'joggers', 'trouser']
products.sort() # Time Complexity is .sort() is O(nlogn)
# Convert the list into a dictionary with productNames and its count
product_count = dict(Counter(products)) 

# Select the value of maximum count
max = 0
for product in product_count:
    if product_count[product] > max:
        max = product_count[product]

# Get the list of product names with maximum occurences
rqd_product = []
for key,value in product_count.items():
    if max == value:
        rqd_product.append(key)

# Print the last proct name in the list        
print(rqd_product[-1])        
