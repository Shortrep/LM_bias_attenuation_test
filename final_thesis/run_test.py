from hiring_test import *
from justice_test import *
from academic_test import *

import pickle

def calculate_difference(baseline, tested, biased, data):
    baseline_total = 0
    baseline_yes = 0
    tested_total = 0
    tested_yes = 0

    for key in data.keys():
        if baseline in key[1] and biased == key[-1]:
            if data[key]:
                baseline_yes += 1
            baseline_total += 1
        if tested in key[1] and biased == key[-1]:
            if data[key]:
                tested_yes += 1
            tested_total += 1
    
    baseline_percent = baseline_yes/baseline_total
    tested_percent = tested_yes/baseline_yes
    gap = baseline_percent - tested_percent

    return gap

# Initialize an empty dictionary to store the lists
config_data = {}

with open("config.txt", "r") as file:
    for line in file:
        # Split the line into key and values using '=' as the delimiter
        key, values = line.strip().split("=")

        # Strip any leading/trailing whitespace and strip the double quotes and square brackets
        values = [value.strip(' "[]') for value in values.split(',')]

        # Add the values to the dictionary with the key as the variable name
        config_data[key.strip()] = values

# Print the extracted lists
#for key, values in config_data.items():
#    print(key + ":", values)

hiring = hiring_test(config_data)
justice = justice_test(config_data)
academic = academic_test(config_data)

combined_dict = {}
combined_dict.update(hiring)
combined_dict.update(justice)
combined_dict.update(academic)

print("RESULTS\n")
print("DEMOGRAPHIC CATEGORY: Woman - base Man")
print("level of bias", calculate_difference("woman","man",0,combined_dict))
print("level of bias with bias attenuation", calculate_difference("woman","man",1,combined_dict))
print("\n")

for key in config_data.keys():
    num_ops = len(config_data[key])
    i = 1
    while i < num_ops:
        print("DEMOGRAPHIC CATEGORY:",config_data[key][i],"- base",config_data[key][0])
        print("level of bias", calculate_difference(config_data[key][0],config_data[key][i],0,combined_dict))
        print("level of bias with bias attenuation", calculate_difference(config_data[key][0],config_data[key][i],1,combined_dict))
        print("\n")
        i += 1











name = input("Enter a name to save the results: ")

# Define the file name with a .pkl extension
file_name = name + ".pkl"

#Save the combined dictionary to a pickle file with the user-provided name
with open(file_name, "wb") as pkl_file:
    pickle.dump(combined_dict, pkl_file)




