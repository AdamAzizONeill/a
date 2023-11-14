#each input will either be false or will contain the non bool data.

def meant_to_be_characters(min_length: int | bool, max_length: int | bool, extra_invalid_inputs: list | bool):
    inputs =  ['1']

    if min_length:
        inputs += [min_length]

    if max_length:
        inputs += [max_length]

    if extra_invalid_inputs:
        inputs += extra_invalid_inputs
    
    return inputs

def meant_to_be_numbers(min: int | bool, max: int | bool, extra_invalid_inputs: str | bool):
    inputs = ['a']

    if min:
        inputs += [min]

    if max:
        inputs += [max]

    if extra_invalid_inputs:
        inputs += extra_invalid_inputs
    
    return inputs
