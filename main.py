import sys
import os
from parser import load_yaml
from turing_machine import TuringMachine

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]  # Archivo YAML como argumento
    base_name = os.path.splitext(os.path.basename(config_file))[0]  # Extraer el nombre base sin extensión
    output_file = f"./output/{base_name}_output.txt"  # Crear el nombre del archivo

    config = load_yaml(config_file)
    tm = TuringMachine(
        states=config['states'],
        input_alphabet=config['input_alphabet'],
        tape_alphabet=config['tape_alphabet'],
        blank_symbol=config['blank_symbol'],
        initial_state=config['initial_state'],
        accept_states=config['accept_states'],
        transitions=config['transitions']
    )

    # Procesar simulaciones y guardar resultados
    with open(output_file, "w", encoding="utf-8") as f:
        for input_string in config['inputs']:
            f.write(f"Simulating input: {input_string}\n")
            print(f"\nSimulating input: {input_string}")
            tm.reset(input_string)
            steps, accepted = tm.run()

            for step in steps:
                f.write(step + "\n")
                print(step)

            result = "Accepted" if accepted else "Rejected"
            f.write(f"Result: {result}\n")
            print("Result:", result)

    print(f"Simulation output saved to {output_file}")

    
    # Generar el diagrama de la máquina de Turing usando Graphviz local
    base_name = os.path.splitext(os.path.basename(config_file))[0]  # Extrae solo el nombre base sin la extensión
    diagram_name = f"./output/{base_name}_diagram"
    tm.generate_diagram_local(diagram_name)


if __name__ == "__main__":
    main()
