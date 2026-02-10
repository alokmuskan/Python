essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "pepper"}

# union 
all_spices = essential_spices | optional_spices
print(f"All spices : {all_spices}")

# intersection
common_spices = essential_spices & optional_spices
print(f"Common spices : {common_spices}")

# differences
only_in_essential = essential_spices - optional_spices
print(f"Only Essential : {only_in_essential}")

# membership

print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")