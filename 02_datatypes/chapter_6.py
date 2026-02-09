chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type}, please!")

chai_description = "Aromatic and Bold"
print(f"First Word: {chai_description[0:7]}")  # last number is not inclusive in python
print(f"First Word: {chai_description[0:8]}")
print(f"First Word: {chai_description[0:8:2]}")  # it means every second character
print(f"First Word: {chai_description[12:]}")
print(f"First Word: {chai_description[::-1]}")  # reverses the whole string 


label_text = "Chai Spécial"
encode_label = label_text.encode("utf-8")
print(f"Non encode label: {label_text}")
print(f"Encoded label: {encode_label}")
decoded_label = encode_label.decode("utf-8")
print(f"Decoded label : {decoded_label}")