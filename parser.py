import yaml

def load_yaml(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Procesar los estados
    states = data['q_states']['q_list']
    initial_state = data['q_states']['initial']
    accept_states = [data['q_states']['final']]

    # Procesar el alfabeto y símbolos de la cinta
    input_alphabet = data['alphabet']
    tape_alphabet = data['tape_alphabet'] + ["#"]  # Asegurar que el símbolo en blanco esté incluido
    blank_symbol = "#"

    # Procesar las transiciones (delta)
    transitions = {}
    for delta_item in data['delta']:
        params = delta_item['params']
        output = delta_item['output']
        transitions[(params['initial_state'], params['tape_input'])] = (
            output['final_state'],
            output['tape_output'],
            output['tape_displacement']
        )

    # Procesar las cadenas de simulación
    simulation_strings = data['simulation_strings']

    return {
        'states': states,
        'initial_state': initial_state,
        'accept_states': accept_states,
        'input_alphabet': input_alphabet,
        'tape_alphabet': tape_alphabet,
        'blank_symbol': blank_symbol,
        'transitions': transitions,
        'inputs': simulation_strings
    }
