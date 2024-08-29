# Microcontroller Emulator

A Python-based emulator for simulating microcontroller operations and networking between multiple microcontrollers. This project demonstrates basic memory management, register operations, stack handling, and inter-microcontroller communication.

## Features

- **Microcontroller Simulation**: Emulates a simple microcontroller with 256 bytes of memory, four general-purpose registers, and a stack.
- **Instruction Set**: Supports basic operations including arithmetic, memory access, stack operations, and control flow instructions.
- **Network Communication**: Enables message passing and broadcasting between multiple microcontroller instances via a simulated network.
- **Program Execution**: Loads and executes programs written in a simple instruction set within the microcontroller's memory.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/raharezaie/microcontroller-emulator.git
    cd microcontroller-emulator
    ```

2. (Optional) Create a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install any necessary dependencies (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the Emulator**:

    ```bash
    python emulator.py
    ```

2. **Example Program**:

    Here's an example of how to load a program and run it on a microcontroller instance:

    ```python
    # Example program for MCU 1: Increment, set register 1, add, print
    program1 = [1, 1, 4, 10, 3, 2]
    mcu1.load_program(program1)
    mcu1.run()

    # Check registers after execution
    print(f"MCU 1 Registers: {mcu1.registers}")
    ```

3. **Communication Between Microcontrollers**:

    The emulator supports sending messages between microcontroller instances:

    ```python
    # Example of MCU 1 sending a message to MCU 2
    mcu1.send_message(2, "Hello from MCU 1")

    # Run MCU 2 to process the message
    mcu2.run()
    print(f"MCU 2 Registers: {mcu2.registers}")
    ```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you find a bug or have a feature request.


