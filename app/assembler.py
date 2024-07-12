import re

class Assembler:
    def __init__(self):
        self.opcodes = {
            'ADD': '0001',
            'SUB': '0010',
            'LOAD': '0011',
            'STORE': '0100',
            'JUMP': '0101'
        }

    def assemble(self, assembly_code):
        machine_code = []
        lines = assembly_code.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'):
                continue
            parts = re.split(r'\s+', line)
            opcode = self.opcodes.get(parts[0])
            if not opcode:
                raise ValueError(f"Unknown instruction: {parts[0]}")
            operands = ''
            for operand in parts[1:]:
                if operand.startswith('R'):
                    # Register operand
                    operands += format(int(operand[1:]), '04b')
                else:
                    # Immediate value
                    operands += format(int(operand), '08b')
            machine_code.append(opcode + operands)
        return machine_code
