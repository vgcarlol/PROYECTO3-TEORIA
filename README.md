
# Proyecto No. 3: Simulador de Máquina de Turing

Este proyecto consiste en un simulador de Máquina de Turing desarrollado en Python. Permite cargar configuraciones desde archivos YAML, simular su comportamiento y generar diagramas de estado utilizando Graphviz.

## Video de explicación y demostración
- He grabado un pequeño video demostrando y explicando brevemente el programa, puedes verlo en YouTube: [Haciendo clic en este video](https://)

## Instrucciones de Uso

### Requisitos Previos

1. **Python 3.8 o superior**: Asegúrese de tener instalado Python en su sistema.
2. **Librerías de Python**: Instale las librerías necesarias ejecutando:
    ```bash
    pip install pyyaml
    ```
3. **Graphviz**: Descargue e instale Graphviz desde su [sitio oficial](https://graphviz.org/download/). Asegúrese de agregarlo a las variables de entorno del sistema. Por defecto, en el proyecto se añadió de manera local en el repositorio Raiz.

### Archivos Incluidos

- `main.py`: Archivo principal para ejecutar el simulador.
- `parser.py`: Modulo para cargar y procesar archivos YAML.
- `turing_machine.py`: Implementación de la Máquina de Turing.
- `config/`: Carpeta que contiene ejemplos de configuración YAML.
  - `simple.yaml`: Máquina de Turing reconocedora con cadenas aceptadas y rechazadas.
  - `alteradora.yaml`: Máquina de Turing alteradora.
  - `invalid.yaml`: Ejemplo con cadenas rechazadas.
- `output/simulation_output.txt`: Archivo de salida con los resultados de las simulaciones.
- `output/diagrama.png`: Diagramas generados en formato PNG después de ejecutar el programa.

### Ejecución

1. Coloque su archivo YAML de configuración en la carpeta `config/`.
2. Ejecute el simulador utilizando el siguiente comando en la terminal:
    ```bash
    python main.py ./config/<archivo_config>.yaml
    ```
    Reemplace `<archivo_config>` con el nombre de su archivo YAML.

### Ejemplo de Uso

Para simular la configuración del archivo `simple.yaml`, use el comando:
```bash
python main.py ./config/simple.yaml
```

El programa generará:
- Una salida detallada en la terminal.
- Un archivo `simulation_output.txt` con los resultados.
- Un diagrama del estado en un archivo PNG (por ejemplo, `simple_diagram.png`).

### Funcionalidades

1. **Simulación de Cadenas**:
   - Procesa cadenas especificadas en los archivos YAML.
   - Determina si las cadenas son aceptadas o rechazadas.

2. **Generación de Diagramas**:
   - Genera diagramas visuales del comportamiento de la máquina en formato PNG.

3. **Máquinas Incluidas**:
   - Máquina reconocedora (`simple.yaml`): Verifica si las cadenas pertenecen a un lenguaje específico.
   - Máquina alteradora (`alteradora.yaml`): Realiza modificaciones en la cinta.
   - Prueba con cadenas rechazadas (`invalid.yaml`).

### Estructura de un Archivo YAML

Un archivo YAML incluye:
- Estados de la máquina (`q_states`).
- Alfabeto de entrada (`alphabet`).
- Alfabeto de la cinta (`tape_alphabet`).
- Funciones de transición (`delta`).
- Cadenas a simular (`simulation_strings`).

Ejemplo:
```yaml
q_states:
  q_list:
    - '0'
    - '1'
    - '2'
    - '3'
    - '4'
    - '5'
  initial: '0'
  final: '5'
alphabet:
  - a
  - b
tape_alphabet:
  - '#'
  - X
delta:
  - params:
      initial_state: '0'
      tape_input: a
    output:
      final_state: '1'
      tape_output: X
      tape_displacement: R
simulation_strings:
  - abbab
  - aaaab
```

### Resultados Esperados

- Ejecución con múltiples ejemplos de cadenas aceptadas y rechazadas.
- Generación de diagramas para comprender visualmente la lógica de las máquinas.

### Créditos

Este simulador fue desarrollado como parte del Proyecto No. 3 para el curso de Teoría de la Computación.

| ![Foto de Perfil](https://avatars.githubusercontent.com/u/115051589?v=4) | **Carlos Valladares**  
|:-------------------------------------------------:|------------------------  
| **Rol:** Desarrollador principal                 | 📚 Estudiante de Ciencias de la Computación en UVG  
| **Contacto:** [GitHub](https://github.com/vgcarlol) | ✨ Pasión por resolver problemas computacionales  
