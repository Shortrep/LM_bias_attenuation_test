import pickle
import sys

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

def load_pickle_to_dict(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}

if __name__ == "__main__":
    demographic = sys.argv[2]
    base = sys.argv[3]

    if len(sys.argv) < 2:
        print("Please provide the filename as a command line argument.")
    else:
        filename = sys.argv[1]
        result_dict = load_pickle_to_dict(filename)
        
    print("DEMOGRAPHIC CATEGORY:",demographic,"- base",base)
    print("level of bias", calculate_difference(base,demographic,0,result_dict))
    print("level of bias with bias attenuation", calculate_difference(base,demographic,1,result_dict))
    print("\n")


