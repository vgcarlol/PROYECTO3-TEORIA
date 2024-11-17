import subprocess
import os

class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, blank_symbol,
                 initial_state, accept_states, transitions):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.blank_symbol = blank_symbol
        self.initial_state = initial_state
        self.accept_states = accept_states
        self.transitions = self._parse_transitions(transitions)
        self.tape = []
        self.head_position = 0
        self.current_state = initial_state

    def _parse_transitions(self, transitions):
        """
        Verifica la estructura de las transiciones.
        """
        if isinstance(transitions, dict):
            return transitions  # Ya está en el formato esperado
        else:
            parsed = {}
            for t in transitions:
                key = (t['from_state'], t['read_symbol'])
                value = (t['to_state'], t['write_symbol'], t['direction'])
                parsed[key] = value
            return parsed

    def reset(self, input_string):
        """
        Reinicia la máquina de Turing para una nueva entrada.
        """
        self.tape = list(input_string) + [self.blank_symbol]
        self.head_position = 0
        self.current_state = self.initial_state

    def step(self):
        """
        Realiza un paso de transición en la máquina de Turing.
        """
        try:
            read_symbol = self.tape[self.head_position]
            action = self.transitions.get((self.current_state, read_symbol))

            if action is None:
                print(f"Warning: No transition defined for ({self.current_state}, {read_symbol})")
                return False

            new_state, write_symbol, direction = action

            # Registro de la transición
            print(f"Transition: ({self.current_state}, {read_symbol}) -> ({new_state}, {write_symbol}, {direction})")

            # Escribir en la cinta y actualizar el estado y posición del cabezal
            self.tape[self.head_position] = write_symbol
            self.current_state = new_state
            self.head_position += 1 if direction == "R" else -1

            # Asegurarse de que la cinta crezca dinámicamente si el cabezal se mueve fuera de los límites
            if self.head_position < 0:
                self.head_position = 0
                self.tape.insert(0, self.blank_symbol)
            elif self.head_position >= len(self.tape):
                self.tape.append(self.blank_symbol)

        except Exception as e:
            print(f"Error during step execution: {e}")
            return False

        return True

    def run(self):
        """
        Ejecuta la máquina de Turing para una entrada completa.
        """
        steps = []
        while self.current_state not in self.accept_states:
            steps.append(self._description())
            if not self.step():  # Detenerse si no hay transición válida
                break
        steps.append(self._description())
        return steps, self.current_state in self.accept_states

    def _description(self):
        """
        Devuelve una descripción del estado actual de la máquina.
        """
        tape_str = "".join(self.tape)
        return f"State: {self.current_state}, Tape: {tape_str}, Head: {self.head_position}"

    def generate_diagram_local(self, output_file="turing_machine_diagram"):
        """
        Genera un diagrama de Graphviz para la máquina de Turing y lo guarda como un archivo PNG.
        """
        dot_file = f"{output_file}.dot"
        png_file = f"{output_file}.png"

        # Crear archivo DOT con codificación UTF-8
        with open(dot_file, "w", encoding="utf-8") as f:
            f.write("digraph TuringMachine {\n")
            f.write('  rankdir=LR;\n')  # Direccionamiento de izquierda a derecha

            # Añadir estados
            for state in self.states:
                shape = "doublecircle" if state in self.accept_states else "circle"
                f.write(f'  "{state}" [shape={shape}];\n')

            # Añadir transiciones
            for (from_state, read_symbol), (to_state, write_symbol, direction) in self.transitions.items():
                label = f"{read_symbol} → {write_symbol}, {direction}"
                f.write(f'  "{from_state}" -> "{to_state}" [label="{label}"];\n')

            f.write("}\n")

        # Llamar a Graphviz para generar el PNG
        try:
            graphviz_path = os.path.join(os.getcwd(), "Graphviz", "bin", "dot")  # Ruta local de Graphviz
            subprocess.run([graphviz_path, "-Tpng", dot_file, "-o", png_file], check=True)
            print(f"Diagram saved to {png_file}")
        except FileNotFoundError:
            print("Error: Graphviz binary not found. Ensure it is installed and accessible.")
        except Exception as e:
            print(f"Error generating diagram: {e}")

        # Eliminar archivo DOT temporal
        if os.path.exists(dot_file):
            os.remove(dot_file)
