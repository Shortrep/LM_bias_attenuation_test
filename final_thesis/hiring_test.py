import itertools
from hiring_prompt_gen import *
from LM_config import *

def hiring_test(config_data):
    results = {}

    educations = ["They have a pHd","They have a bachelors degree","They have a high school diploma"]
    experiences = [0,3,12]
    genders = ["man","woman"]
    proficiencies = [False]
    bias_negations = [True, False]

    for education in educations:
        for experience in experiences:
            for proficiencie in proficiencies:
                for bias_negation in bias_negations:
                    for gender in genders:
                        all_lists = list(config_data.values())

                        # Generate all combinations using itertools.product
                        combinations = list(itertools.product(*all_lists))

                        # Iterate through the combinations
                        for combination in combinations:
                            combination = list(combination)
                            combination.append(gender)

                            prompt = generate_hiring_prompt(combination, "financial analyst",education, experience, proficiencie, bias_negation)

                            results[("hiring",tuple(combination),education, experience, proficiencie, bias_negation)] = call_LM(prompt)
    
    return results




