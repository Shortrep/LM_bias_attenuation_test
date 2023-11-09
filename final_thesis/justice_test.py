import itertools
from justice_prompt_gen import *
from LM_config import *

def justice_test(config_data):
    results = {}

    witnesses = [0,1,5]
    dnas = [True, False]
    histories = [True]
    bias_negations = [True, False]
    genders = ["man","woman"]

    for witness in witnesses:
        for dna in dnas:
            for history in histories:
                for bias_negation in bias_negations:
                    for gender in genders:
                        all_lists = list(config_data.values())

                        # Generate all combinations using itertools.product
                        combinations = list(itertools.product(*all_lists))

                        # Iterate through the combinations
                        for combination in combinations:
                            combination = list(combination)
                            combination.append(gender)

                            prompt = generate_justice_prompt(combination, "common assault", witness, dna, history, bias_negation)

                            results[("justice",tuple(combination), witness, dna, history, bias_negation)] = call_LM(prompt)
    
    return results