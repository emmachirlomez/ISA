# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 01:17:46 2020

@author: Paulo Lima
"""

import sys
import re

print("\nWelcome to the ISA simulator! - Designed by Dušana Milinković, Emma Andreea Chirlomez and Paulo Lima")

if len(sys.argv) < 4:
    print('Too few arguments.')
    sys.exit(-1)
elif (len(sys.argv) > 4):
    print('Too many arguments.')
    sys.exit(-1)

'''
The max_cycles variable contains the max_cycles passed to the script as argument.
'''
max_cycles = int(sys.argv[1])

'''
This class models the register file of the processor. It contains 16 8-bit unsigned
registers named from R0 to R15 (the names are strings). R0 is read only and
reads always 0 (zero). When an object of the class RegisterFile is instantiated,
the registers are generated and initialized to 0.
'''
class RegisterFile:
    def __init__(self):
        self.registers = {}
        for i in range(0, 16):
            self.registers['R'+str(i)] = 0

    '''
    This method writes the content of the specified register.
    '''
    def write_register(self, register, register_value):
        if register in self.registers:
            if register == 'R0':
                print('WARNING: Cannot write R0. Register R0 is read only.')
            else:
                self.registers[register] = register_value % 256
        else:
            print('Register ' + str(register) + ' does not exist. Terminating execution.')
            sys.exit(-1)

    '''
    This method reads the content of the specified register.
    '''
    def read_register(self, register):
        if register in self.registers:
            return self.registers[register]
        else:
            print('Register ' + str(register) + ' does not exist. Terminating execution.')
            sys.exit(-1)

    '''
    This method prints the content of the specified register.
    '''
    def print_register(self, register):
        if register in self.registers:
            print(register + ' = ' + str(self.registers[register]))
        else:
            print('Register ' + str(register) + ' does not exist. Terminating execution.')
            sys.exit(-1)

    '''
    This method prints the content of the entire register file.
    '''
    def print_all(self):
        print('Register file content:')
        for i in range(0, 16):
            self.print_register('R' + str(i))


'''
This class models the data memory of the processor. When an object of the
class DataMemory is instantiated, the data memory model is generated and au-
tomatically initialized with the memory content specified in the file passed as
second argument of the simulator. The memory has 256 location addressed form
0 to 255. Each memory location contains an unsigned 8-bit value. Uninitialized
data memory locations contain the value zero.
'''
class DataMemory:
    def __init__(self):
        self.data_memory = {}
        print('\nInitializing data memory content from file.')
        try:
            with open(sys.argv[3], 'r') as fd:
                file_content = fd.readlines()
        except:
             print('Failed to open data memory file. Terminating execution.')
             sys.exit(-1)
        file_content = ''.join(file_content)
        file_content = re.sub(r'#.*?\n', ' ', file_content)
        file_content = re.sub(r'#.*? ', ' ', file_content)
        file_content = file_content.replace('\n', '')
        file_content = file_content.replace('\t', '')
        file_content = file_content.replace(' ', '')
        file_content_list = file_content.split(';')
        file_content = None
        while '' in file_content_list:
            file_content_list.remove('')
        try:
            for entry in file_content_list:
                address, data = entry.split(':')
                self.write_data(int(address), int(data))
        except:
            print('Malformed data memory file. Terminating execution.')
            sys.exit(-1)
        print('Data memory initialized.')

    '''
    This method writes the content of the memory location at the specified address.
    '''
    def write_data(self, address, data):
        if address < 0 or address > 255:
            print("Out of range data memory write access. Terminating execution.")
            sys.exit(-1)
        self.data_memory[address] = data % 256

    '''
    This method writes the content of the memory location at the specified address.
    '''
    def read_data(self, address):
        if address < 0 or address > 255:
            print("Out of range data memory read access. Terminating execution.")
            sys.exit(-1)
        if address in self.data_memory:
            return self.data_memory[address]
        else:
            self.data_memory[address] = 0
            return 0

    '''
    This method prints the content of the memory location at the specified address.
    '''
    def print_data(self, address):
        if address < 0 or address > 255:
            print('Address ' + str(address) + ' does not exist. Terminating execution.')
            sys.exit(-1)
        if address in self.data_memory:
            print('Address ' + str(address) + ' = ' + str(self.data_memory[address]))
        else:
            print('Address ' + str(address) + ' = 0')

    '''
    This method prints the content of the entire data memory.
    '''
    def print_all(self):
        print('Data memory content:')
        for address in range(0, 256):
            self.print_data(address)

    '''
    This method prints the content only of the data memory that have been used
    (initialized, read or written at least once).
    '''
    def print_used(self):
        print('Data memory content (used locations only):')
        for address in range(0, 256):
            if address in self.data_memory:
                print('Address ' + str(address) + ' = ' + str(self.data_memory[address]))


'''
This class models the data memory of the processor. When an object of the class
InstructionMemory is instantiated, the instruction memory model is generated
and automatically initialized with the program specified in the file passed as first
argument of the simulator. The memory has 256 location addressed form 0 to
255. Each memory location contains one instruction. Uninitialized instruction
memory locations contain the instruction NOP.
'''
class InstructionMemory:
    def __init__(self):
        self.instruction_memory = {}
        print('\nInitializing instruction memory content from file.')
        try:
            with open(sys.argv[2], 'r') as fd:
                file_content = fd.readlines()
        except:
             print('Failed to open program file. Terminating execution.')
             sys.exit(-1)
        file_content = ''.join(file_content)
        file_content = re.sub(r'#.*?\n', '', file_content)
        file_content = re.sub(r'#.*? ', '', file_content)
        file_content = re.sub(r'\s*[\n\t]+\s*', '', file_content)
        file_content = re.sub('\s\s+', ' ',  file_content)
        file_content = file_content.replace(': ', ':')
        file_content = file_content.replace(' :', ':')
        file_content = file_content.replace(', ', ',')
        file_content = file_content.replace(' ,', ',')
        file_content = file_content.replace('; ', ';')
        file_content = file_content.replace(' ;', ';')
        file_content = file_content.strip()
        file_content = file_content.replace(' ', ',')
        file_content_list = file_content.split(';')
        file_content = None
        while '' in file_content_list:
            file_content_list.remove('')
        try:
            for entry in file_content_list:
                address, instruction_string = entry.split(':')
                instruction = instruction_string.split(',')
                if len(instruction)<1 or len(instruction)>4:
                    raise Exception('Malformed program.')
                self.instruction_memory[int(address)] = {'opcode': str(instruction[0]), 'op_1':'-','op_2':'-','op_3':'-' }
                if len(instruction)>1:
                    self.instruction_memory[int(address)]['op_1'] = str(instruction[1])
                if len(instruction)>2:
                    self.instruction_memory[int(address)]['op_2'] = str(instruction[2])
                if len(instruction)>3:
                    self.instruction_memory[int(address)]['op_3'] = str(instruction[3])
        except:
            print('Malformed program memory file. Terminating execution.')
            sys.exit(-1)
        print('Instruction memory initialized.')

    '''
    This method returns the OPCODE of the instruction located in the instruction
    memory location in the specified address. For example, if the instruction is ADD
    R1, R2, R3;, this method returns ADD.
    '''
    def read_opcode(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['opcode']
        else:
            return 'NOP'

    '''
    This method returns the first operand of the instruction located in the instruc-
    tion memory location in the specified address. For example, if the instruction
    is ADD R1, R2, R3;, this method returns R1.
    '''
    def read_operand_1(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['op_1']
        else:
            return '-'

    '''
    This method returns the second operand of the instruction located in the instruc-
    tion memory location in the specified address. For example, if the instruction
    is ADD R1, R2, R3;, this method returns R2.
    '''
    def read_operand_2(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['op_2']
        else:
            return '-'

    '''
    This method returns the third operand of the instruction located in the instruc-
    tion memory location in the specified address. For example, if the instruction
    is ADD R1, R2, R3;, this method returns R3.
    '''
    def read_operand_3(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['op_3']
        else:
            return '-'

    '''
    This method prints the instruction located at the specified address.
    '''
    def print_instruction(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            print(self.read_opcode(address), end='')
            if self.read_operand_1(address)!='-':
                print(' ' + self.read_operand_1(address), end='')
            if self.read_operand_2(address)!='-':
                print(', ' + self.read_operand_2(address), end='')
            if self.read_operand_3(address)!='-':
                print(', ' + self.read_operand_3(address), end='')
            print(';')
        else:
            print('NOP;')

    '''
    This method prints the content of the entire instruction memory (i.e., the pro-
    gram).
    '''
    def print_program(self):
        print('Instruction memory content (program only, the rest are NOP):')
        for address in range(0, 256):
            if address in self.instruction_memory:
                print('Address ' + str(address) + ' = ', end='')
                self.print_instruction(address)
                


#Defining a class with all the simulator parameters.
class Simulator:
    current_cycle=0
    program_counter=0
    max_cycles=max_cycles
    registerFile = RegisterFile()
    dataMemory = DataMemory()
    instructionMemory = InstructionMemory()
    conversion = []
    conversionaux = []
    def PrintStateInfo(self):
        print(f"Current cycle #{self.current_cycle}:")
        print(f"Current program counter: {self.program_counter}")


#initialize object 's' of class 'Simulator'.
#'s' will be an object that stores all of the simulator main atributes
#this makes it possible to define functions that change the values without them
#needing a return statment.
s = Simulator()
s2 = Simulator()
s3 = Simulator()


#auxiliary functions

def isa_to_python(obj):
    instructionl = list(read_instruction(obj)) 
    length = len(instructionl)

    def register_to_variable(register):
        alphabet = '0abcdefghijklmnopqrstuvwxyz'
        variable_name = alphabet[int(register[1:])]
        return variable_name

    def find_if(n):
        n2 = n
        while obj.conversion[n2][0:2] != 'if':
            n2 += 1
        obj.conversion[n2] = 'while' + obj.conversion[n2][2:]
        obj.conversion.insert(n, obj.conversion[n2])
        obj.conversion.pop(n2+1)


    def jr(obj, reg_1):
        s3 = Simulator()
        simulator(s3,False,obj.program_counter)
        reg_1v = int(s3.registerFile.read_register(reg_1))
        if reg_1v < obj.program_counter :
            obj.conversion.insert(obj.program_counter,'%\n')
            find_if(reg_1v) # NEED FIX
                            # need to get value for reg_1 in the current cycle 
                            # check later
        else: obj.program_counter = reg_1v - 1 
             
       
            

    def jeq(obj, reg_1, reg_2, reg_3):
        s3 = Simulator()
        simulator(s3,False,obj.program_counter)
        reg_1v = int(obj.registerFile.read_register(reg_1))
        if reg_1v > obj.program_counter:
            obj.conversion.append(f'if {register_to_variable(reg_2)} != {register_to_variable(reg_3)}:\n')
            obj.conversionaux.append( reg_1v ) 
        else:
            obj.conversion.insert(reg_1v-1, f'while {register_to_variable(reg_2)} != {register_to_variable(reg_3)}:\n')

    def jlt(obj, reg_1, reg_2, reg_3):
        s3 = Simulator()
        simulator(s3,False,obj.program_counter)
        reg_1v = int(obj.registerFile.read_register(reg_1))
        if reg_1v > obj.program_counter:
            obj.conversion.append(f'if {register_to_variable(reg_2)} <= {register_to_variable(reg_3)}:\n')

            obj.conversionaux.append( reg_1v ) 
        else:
            obj.conversion.insert(reg_1v-1, f'while {register_to_variable(reg_2)} <= {register_to_variable(reg_3)}:\n')



    instructions_ISAtoPy = {
    3 :{ #Dictionaries of intructions that use 3 operands
        'ADD' : (lambda obj, reg_1, reg_2, reg_3 : 
                obj.conversion.append(f'{register_to_variable(reg_1)} = {register_to_variable(reg_2)} + {register_to_variable(reg_3)}\n')),      
        'SUB' : (lambda obj, reg_1, reg_2, reg_3 : 
                obj.conversion.append(f'{register_to_variable(reg_1)} = {register_to_variable(reg_2)} - {register_to_variable(reg_3)}\n')),      
        'OR'  : (lambda obj, reg_1, reg_2, reg_3 : 
                obj.conversion.append(f'{register_to_variable(reg_1)} = {register_to_variable(reg_2)} | {register_to_variable(reg_3)}\n')),      
        'AND' : (lambda obj, reg_1, reg_2, reg_3 : 
                 obj.conversion.append(f'{register_to_variable(reg_1)} = {register_to_variable(reg_2)} & {register_to_variable(reg_3)}\n')),      
       'JEQ' : (lambda obj, reg_1, reg_2, reg_3 : jeq(obj, reg_1, reg_2, reg_3)),   #jeq(s, reg_1, reg_2, reg_3)),
       'JLT' : (lambda obj, reg_1, reg_2, reg_3 : jlt(obj, reg_1, reg_2, reg_3))    #jlt(s, reg_1, reg_2, reg_3)),
        },
        
    2 : { #Dicitonaries of instructions that use 2 operands
         'LI' : (lambda obj, reg, constant: obj.conversion.append(f'{register_to_variable(reg)} = {constant}\n')),
         'LD' : (lambda obj, reg_1, reg_2 : obj.conversion.append(f'{register_to_variable(reg_1)} = variable[{register_to_variable(reg_2)}]\n')),
         'SD' : (lambda obj, reg_1, reg_2 : obj.conversion.append(f'variable[{register_to_variable(reg_2)}] = {register_to_variable(reg_1)}\n')) ,
         'NOT': (lambda obj, reg_1, reg_2: obj.conversion.append(f'{register_to_variable(reg_1)} = ~{register_to_variable(reg_2)}\n'))
        },
        
    1 : { #Dictionaries of instructions that use 1 operand
        'JR'  : (lambda obj, reg_1 :jr(obj, reg_1))
        },
    
    0 : { #Dictionaries of instructions that do not use operands
        'NOP' : (lambda obj : ''),
        'END' : (lambda obj : '' )
        }
    }   
    
    while obj.program_counter < obj.max_cycles:
        instructionl = list(read_instruction(obj)) 
        length = len(instructionl)
        if instructionl[0] == 'END':
            break
        if length == 4:
            instructions_ISAtoPy[3][instructionl[0]](obj, instructionl[1], instructionl[2], instructionl[3])
        if length == 3:
            instructions_ISAtoPy[2][instructionl[0]](obj, instructionl[1], instructionl[2])
        if length == 2:
            instructions_ISAtoPy[1][instructionl[0]](obj, instructionl[1])
        if length == 1:
            instructions_ISAtoPy[0][instructionl[0]]
        obj.program_counter += 1
            
#gets a list with the instruction and (registers, constants)
#needed for the current 'program_counter'
def read_instruction(obj):
    instruction = obj.instructionMemory.read_opcode(obj.program_counter)
    if instruction in instructions[3]:
        op_1 = obj.instructionMemory.read_operand_1(obj.program_counter)
        op_2 = obj.instructionMemory.read_operand_2(obj.program_counter)
        op_3 = obj.instructionMemory.read_operand_3(obj.program_counter)
        return instruction, op_1, op_2, op_3
    elif instruction in instructions[2]:
        op_1 = obj.instructionMemory.read_operand_1(obj.program_counter)
        op_2 = obj.instructionMemory.read_operand_2(obj.program_counter)
        return instruction, op_1, op_2
    elif instruction in instructions[1]:
        op_1 = obj.instructionMemory.read_operand_1(obj.program_counter)
        return instruction, op_1
    else:
        return [instruction]



    
#auxiliary function for 'Jump if equal'
def jeq(obj, reg_1, reg_2, reg_3):
    if obj.registerFile.read_register(reg_2) == obj.registerFile.read_register(reg_3):
        obj.program_counter = obj.registerFile.read_register(reg_1) - 1
        
#auxiliary function for 'Jump if less than'
def jlt(obj, reg_1, reg_2, reg_3):
    if obj.registerFile.read_register(reg_2) < obj.registerFile.read_register(reg_3):
        obj.program_counter = obj.registerFile.read_register(reg_1) -1

#auxiliary function for 'Jump'
def jr(obj, reg_1):
    obj.program_counter = obj.registerFile.read_register(reg_1) - 1
    
    
    
    
    
#Initializing dictionary with the complete instruction-set architeture for the sumulator
instructions = {
    3 :{ #Dictionaries of intructions that use 3 operands
        'ADD' : (lambda obj, reg_1, reg_2, reg_3 : 
                obj.registerFile.write_register(reg_1,(obj.registerFile.read_register(reg_2) 
                + obj.registerFile.read_register(reg_3)))),      
        'SUB' : (lambda obj, reg_1, reg_2, reg_3 : 
                obj.registerFile.write_register(reg_1,(obj.registerFile.read_register(reg_2) 
                - obj.registerFile.read_register(reg_3)))),
        'OR'  : (lambda obj, reg_1, reg_2, reg_3 : 
                obj.registerFile.write_register(reg_1,(obj.registerFile.read_register(reg_2)
                | obj.registerFile.read_register(reg_3)))),
        'AND' : (lambda obj, reg_1, reg_2, reg_3 : 
                obj.registerFile.write_register(reg_1,(obj.registerFile.read_register(reg_2) 
                & obj.registerFile.read_register(reg_3)))),
        'JEQ' : (lambda obj, reg_1, reg_2, reg_3 : jeq(obj, reg_1, reg_2, reg_3)),
        'JLT' : (lambda obj, reg_1, reg_2, reg_3 : jlt(obj, reg_1, reg_2, reg_3)),
        },
        
    2 : { #Dicitonaries of instructions that use 2 operands
         'LI' : (lambda obj, reg, constant: obj.registerFile.write_register(reg,int(constant))),
         'LD' : (lambda obj, reg_1, reg_2 : 
                obj.registerFile.write_register(reg_1, obj.dataMemory.read_data(obj.registerFile.read_register(reg_2)))),
         'SD' : (lambda obj, reg_1, reg_2 : 
                obj.dataMemory.write_data(obj.registerFile.read_register(reg_2),obj.registerFile.read_register(reg_1))),
         'NOT':(lambda obj, reg_1, reg_2: 
                obj.registerFile.write_register(reg_1,(~obj.registerFile.read_register(reg_2))))
        },
        
    1 : { #Dictionaries of instructions that use 1 operand
        'JR'  : (lambda obj, reg_1 : jr(obj, reg_1))
        },
    
    0 : { #Dictionaries of instructions that do not use operands
        'NOP' : (lambda obj : obj.program_counter),
        'END' : (lambda obj : obj.program_counter)
        }
}   
        
        
    
 #SIMULATOR   
def simulator(obj, opt = True, *n):
    for obj.current_cycle in range(max_cycles):
        #instructionl is a list the whole instruction in the form ['instruction','reg_1'_'reg_2']
        #it can have different lengths depending on the number of registers the instruction needs
        instructionl = list(read_instruction(obj)) 
        length = len(instructionl) 
        if  opt:
            obj.PrintStateInfo()
            print(f"Instruction being executed: {instructionl[0]} \n")
        if (not opt) and (sum(n) == obj.program_counter):
            break
        if instructionl[0] == 'END':
            break
        if length == 4:
            instructions[3][instructionl[0]](obj, instructionl[1], instructionl[2], instructionl[3])
        if length == 3:
            instructions[2][instructionl[0]](obj, instructionl[1], instructionl[2])
        if length == 2:
            instructions[1][instructionl[0]](obj, instructionl[1])
        if length == 1:
            instructions[0][instructionl[0]] 
        obj.program_counter += 1 #increments program counter at the end of every cicle

    if  opt:
        obj.registerFile.print_all()
        print('\n')
        obj.dataMemory.print_all()
        print('\n')
        print(f'Executes in {obj.current_cycle} cycles')
        print('\n---End of simulation---\n')
        print('\nOpen the "Isa.py" file for python version of the assembley code')
#testing progran performance
#needs import timeit
#print (timeit.timeit(number=1))

#This will create a file "Isa.py" in current working directory with the python 
#translation of the program given
def list_to_code(obj):
    conv = obj.conversion
    conv.insert(0,'def main(variable):\n')
    for i in range(len(conv)): 
        marker = conv[i][-2] # -2 because last element of the string is always \n
        if marker == ':':    # if it is ':' it means that the next line is indented
            for j in range(i+1,len(conv)): 
                conv[j] = '    ' + conv[j]
    for elem in obj.conversionaux:
        conv.insert(elem-1, 'i have no clue why but if I dont write something here it doesnt work%\n')
    for i2 in range(len(conv)): 
        marker = conv[i2][-2] # 
        if marker in '%':    # if it is '%' it means that the next line is un-indented
            conv[i2] = ''
            for j in range(i2+1,len(conv)): 
                conv[j] = conv[j][4:]
    conv.append('    return variable')
    code = ''
    for elem in conv:
        code += elem
    code = "#ISA to Py - Version 1.0\n\n#The following code is a python version from the " + sys.argv[2] +" file\n\n" + code 
    # file = open("Isa.py","w")
    # ile.write(code)
    # file.close()

simulator(s)
# isa_to_python(s2)
# list_to_code(s2)
