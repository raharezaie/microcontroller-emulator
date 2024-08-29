class Microcontroller:
    def __init__(self, id, network):
        self.memory = [0] * 256  
        self.registers = [0] * 4  
        self.stack = []
        self.id = id  
        self.network = network  

    def send_message(self, destination_id, message):
        self.network.send(self.id, destination_id, message)

    def receive_message(self, source_id, message):
        print(f"MCU {self.id} received from {source_id}: {message}")
       
    def load_program(self, program):
        for i in range(len(program)):
            self.memory[i] = program[i]

    def run(self):
        pc = 0  
        while pc < len(self.memory):
            instruction = self.memory[pc]
            pc = self.execute(instruction, pc)

    def execute(self, instruction, pc):
        opcode = instruction >> 4
        operand = instruction & 0x0F
        if opcode == 1:  
            self.registers[0] += 1
        elif opcode == 2: 
            print(self.registers[0])
        elif opcode == 3: 
            self.registers[0] += self.registers[1]
        elif opcode == 4:  
            self.registers[1] = self.memory[pc + 1]
            return pc + 2  
        elif opcode == 5:  
            if self.registers[0] == 0:
                return operand
        elif opcode == 6: 
            self.registers[0] = self.memory[operand]
        elif opcode == 7:  
            self.registers[0] -= self.registers[1]
        elif opcode == 8: 
            self.stack.append(pc + 2)
            return operand
        elif opcode == 9:  
            return self.stack.pop()
        elif opcode == 0xA:  
            self.stack.append(self.registers[0])
        elif opcode == 0xB: 
            self.registers[0] = self.stack.pop()
        elif opcode == 0xC:  
            self.registers[0] = self.read_sensor()
        return pc + 1  


class Network:
    def __init__(self):
        self.microcontrollers = {}

    def add_microcontroller(self, mcu):
        self.microcontrollers[mcu.id] = mcu

    def send(self, source_id, destination_id, message):
        if destination_id in self.microcontrollers:
            self.microcontrollers[destination_id].receive_message(source_id, message)
        else:
            print(f"MCU {destination_id} not found on the network")

    def broadcast(self, source_id, message):
        for mcu_id in self.microcontrollers:
            if mcu_id != source_id:
                self.microcontrollers[mcu_id].receive_message(source_id, message)


if __name__ == "__main__":
    network = Network()

    mcu1 = Microcontroller(1, network)
    mcu2 = Microcontroller(2, network)

    network.add_microcontroller(mcu1)
    network.add_microcontroller(mcu2)

    program1 = [1, 1, 4, 10, 3, 2]
    mcu1.load_program(program1)
    mcu1.run()

    print(f"MCU 1 Registers: {mcu1.registers}")

    mcu1.send_message(2, "Hello from MCU 1")

    mcu2.run()
    print(f"MCU 2 Registers: {mcu2.registers}")

