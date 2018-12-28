def score_of_last_ten_recipes(starting_recipes, after_recipe_count):
    def continue_while(recipes):
        return len(recipes) < after_recipe_count + 10

    return ''.join(str(i) for i in get_recipes(starting_recipes,
                                               continue_while)[
                                   after_recipe_count:after_recipe_count + 10])


def get_recipes(starting_recipes, continue_while):
    elf_locations = [0, 1]
    recipes = [int(s) for s in starting_recipes]
    while continue_while(recipes):
        new_recipes = [int(s) for s in list(str(recipes[elf_locations[0]] +
                                                recipes[elf_locations[1]]))]
        recipes.extend(new_recipes)
        elf_locations = list(map(lambda x: (x + recipes[x] + 1) % len(recipes),
                                 elf_locations))
    return recipes


def count_left_of_score_sequence(starting_recipes, sequence):
    sequence_list = [int(s) for s in sequence]

    def continue_while(recipes):
        last_subsequence = recipes[-len(sequence):]
        next_to_last_subsequence = recipes[ -len(sequence) - 1: -1]
        return sequence_list not in (last_subsequence,
                                     next_to_last_subsequence)

    recipes = get_recipes(starting_recipes, continue_while)
    s = ''.join(str(i) for i in recipes)
    return s.index(sequence)
