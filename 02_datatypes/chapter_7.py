masala_spices = ("cardamom", "cloves", "cinamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2,1  # values are assigned respectively
print(f"Ratio for Ginger: {ginger_ratio} and Cardamom : {cardamom_ratio}")

# Variable swapping doesn't need a third variable we can just do it like that
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio  # swapped the values, unique behavior of python
print(f"After Swapping Ratio for Ginger: {ginger_ratio} and Cardamom : {cardamom_ratio}")

# membership
print(f"Is ginger in masala spices ? {"ginger" in masala_spices}")
print(f"Is cinamon in masala spices ? {"cinamon" in masala_spices}")