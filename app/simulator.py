class Simulator:
    def __init__(self):
        self.registers = [0] * 16
        self.memory = [0] * 256
        self.pc = 0  # Program counter

    def load_program(self, machine_code):
        self.memory[:len(machine_code)] = [int(x, 2) for x in machine_code]

    def step(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        opcode = (instruction >> 12) & 0xF
        r1 = (instruction >> 8) & 0xF
        r2 = (instruction >> 4) & 0xF
        r3 = instruction & 0xF
        if opcode == 1:  # ADD
            self.registers[r3] = self.registers[r1] + self.registers[r2]
        elif opcode == 2:  # SUB
            self.registers[r3] = self.registers[r1] - self.registers[r2]
        elif opcode == 3:  # LOAD
            self.registers[r1] = self.memory[r2]
        elif opcode == 4:  # STORE
            self.memory[r2] = self.registers[r1]
        elif opcode == 5:  # JUMP
            self.pc = r1

    def run(self):
        while self.pc < len(self.memory):
            self.step()
