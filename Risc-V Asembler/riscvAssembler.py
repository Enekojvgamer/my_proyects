import os

# AUTOR: Eneko Jurado Varela

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_compiler = os.path.join(BASE_DIR, "riscv_bin.csv")
path_asmbl = os.path.join(BASE_DIR, "asmbl.csv")


def tokens(path:str) -> list[list[str]]:
    instrucciones:list[list[str]] = []
    if(os.path.exists(path)):
        fichero = open(path,"r",encoding="UTF-8")
        for linea in fichero:
            if(len(linea.strip())<=6):
                instrucciones.append([linea.strip()]) # Esto lo hago por las instrucciones ecall y ebreak
            else:
                datos:list[str] = linea.strip().split(" ")
                datos2:list[str] = datos[1].split(",")
                datos2.insert(0,datos[0])
                instrucciones.append(datos2)
        fichero.close()
    else:
        print("El fichero 'asmbl.csv' no existe o no se ha encontrado")
    return instrucciones

def hex_bin(hexadecimal:str) -> str:
    return hexa[hexadecimal]

def inicializarFichero(path) -> None:
    fichero = open(path,"w",encoding="UTF-8")
    fichero.close()

def escribirLinea(bin:str, path:str) -> None:
    if(os.path.exists(path)):
        fichero = open(path,"a",encoding="UTF-8")    
        if(len(bin) == 32):
            fichero.write(f"{bin}\n")
        else:
            fichero.write(f"{bin[0:32]}\n{bin[32:len(bin)]}\n")
        fichero.close()
    else:
        print("El fichero 'riscv_bin.csv' no existe o no se ha encontrado")

def assembler(lista:list[str]) -> str:
    bin:str = ""
    imm:str = ""
    rs1:str = ""
    shamt:str = ""

    ######
    # lui
    ######
    if(lista[0] == "lui"):
        bin += opCodes['lui']
        bin = registros[lista[1]] + bin
        imm = complemento_A2(lista[2])
        for i in range(20):
            bin = imm[19-i] + bin # Primer numero, donde empieza. range(x), cuantos quiero

    

    ######
    # auipc
    ######
    elif(lista[0] == "auipc"):
        bin += opCodes['auipc']
        bin = registros[lista[1]] + bin
        imm = complemento_A2(lista[2])
        for i in range(20):
            bin = imm[19-i] + bin



    ######
    # jal
    ######
    elif(lista[0] == "jal"):
        bin += opCodes['jal']
        bin = registros[lista[1]] + bin
        imm = complemento_A2(lista[2])
        for i in range(8):
            bin = imm[19-i] + bin
        bin = imm[20] + bin
        for i in range(10):
            bin = imm[30-i] + bin
        bin = imm[11] + bin

    

    ######
    # jalr
    ######
    elif(lista[0] == "jalr"):
        bin += opCodes['jalr']
        bin = registros[lista[1]] + bin
        bin = "000" + bin
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        bin = registros[rs1] + bin
        imm = complemento_A2(numeroDecimal)
        for i in range(12):
            bin = imm[31-i] + bin



    ######
    # beq
    ######
    elif(lista[0] == "beq"):
        bin += opCodes['beq']
        imm = complemento_A2(lista[3])
        bin = imm[20] + bin
        for i in range(4):
            bin = imm[30-i] + bin
        bin = "000" + bin # f3
        bin = registros[lista[1]] + bin # rs1
        bin = registros[lista[2]] + bin # rs2
        for i in range(6):
            bin = imm[26-i] + bin
        bin = imm[19] + bin



    ######
    # bne
    ######
    elif(lista[0] == "bne"):
        bin += opCodes['bne']
        imm = complemento_A2(lista[3])
        bin = imm[20] + bin
        for i in range(4):
            bin = imm[30-i] + bin
        bin = "001" + bin # f3
        bin = registros[lista[1]] + bin # rs1
        bin = registros[lista[2]] + bin # rs2
        for i in range(6):
            bin = imm[26-i] + bin
        bin = imm[19] + bin



    ######
    # blt
    ######
    elif(lista[0] == "blt"):
        bin += opCodes['blt']
        imm = complemento_A2(lista[3])
        bin = imm[20] + bin
        for i in range(4):
            bin = imm[30-i] + bin
        bin = "100" + bin # f3
        bin = registros[lista[1]] + bin # rs1
        bin = registros[lista[2]] + bin # rs2
        for i in range(6):
            bin = imm[26-i] + bin
        bin = imm[19] + bin



    ######
    # bge
    ######
    elif(lista[0] == "bge"):
        bin += opCodes['bge']
        imm = complemento_A2(lista[3])
        bin = imm[20] + bin
        for i in range(4):
            bin = imm[30-i] + bin
        bin = "101" + bin # f3
        bin = registros[lista[1]] + bin # rs1
        bin = registros[lista[2]] + bin # rs2
        for i in range(6):
            bin = imm[26-i] + bin
        bin = imm[19] + bin




    ######
    # bltu
    ######
    elif(lista[0] == "bltu"):
        bin += opCodes['bltu']
        imm = complemento_A2(lista[3])
        bin = imm[20] + bin
        for i in range(4):
            bin = imm[30-i] + bin
        bin = "110" + bin # f3
        bin = registros[lista[1]] + bin # rs1
        bin = registros[lista[2]] + bin # rs2
        for i in range(6):
            bin = imm[26-i] + bin
        bin = imm[19] + bin



    ######
    # bgeu
    ######
    elif(lista[0] == "bgeu"):
        bin += opCodes['bgeu']
        imm = complemento_A2(lista[3])
        bin = imm[20] + bin
        for i in range(4):
            bin = imm[30-i] + bin
        bin = "111" + bin # f3
        bin = registros[lista[1]] + bin # rs1
        bin = registros[lista[2]] + bin # rs2
        for i in range(6):
            bin = imm[26-i] + bin
        bin = imm[19] + bin



    ######
    # lb
    ######
    elif(lista[0] == "lb"):
        bin += opCodes['lb']
        bin = registros[lista[1]] + bin
        bin = "000" + bin
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        bin = registros[rs1] + bin
        imm = complemento_A2(numeroDecimal)
        for i in range(12):
            bin = imm[31-i] + bin



    ######
    # lh
    ######
    elif(lista[0] == "lh"):
        bin += opCodes['lh']
        bin = registros[lista[1]] + bin
        bin = "001" + bin
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        bin = registros[rs1] + bin
        imm = complemento_A2(numeroDecimal)
        for i in range(12):
            bin = imm[31-i] + bin



    ######
    # lw
    ######
    elif(lista[0] == "lw"):
        bin += opCodes['lw']
        bin = registros[lista[1]] + bin
        bin = "010" + bin
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        bin = registros[rs1] + bin
        imm = complemento_A2(numeroDecimal)
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # lbu
    ######
    elif(lista[0] == "lbu"):
        bin += opCodes['lbu']
        bin = registros[lista[1]] + bin
        bin = "100" + bin
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        bin = registros[rs1] + bin
        imm = complemento_A2(numeroDecimal)
        for i in range(12):
            bin = imm[31-i] + bin



    ######
    # lhu
    ######
    elif(lista[0] == "lhu"):
        bin += opCodes['lhu']
        bin = registros[lista[1]] + bin
        bin = "101" + bin
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        bin = registros[rs1] + bin
        imm = complemento_A2(numeroDecimal)
        for i in range(12):
            bin = imm[31-i] + bin



    ######
    # sb
    ######
    elif(lista[0] == "sb"):
        bin += opCodes['sb']
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        imm = complemento_A2(numeroDecimal)
        for i in range(5):
            bin = imm[31-i] + bin
        bin = "000" + bin
        bin = registros[rs1] + bin
        bin = registros[lista[1]] + bin # rs2
        for i in range(7):
            bin = imm[26-i] + bin
    


    ######
    # sh
    ######
    elif(lista[0] == "sh"):
        bin += opCodes['sh']
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        imm = complemento_A2(numeroDecimal)
        for i in range(5):
            bin = imm[31-i] + bin
        bin = "001" + bin
        bin = registros[rs1] + bin
        bin = registros[lista[1]] + bin # rs2
        for i in range(7):
            bin = imm[26-i] + bin
    


    ######
    # sw
    ######
    elif(lista[0] == "sw"):
        bin += opCodes['sw']
        n:int = 0 # conseguir el inmediato
        numeroDecimal:str = ""
        while(lista[2][n]!="("):
            numeroDecimal += lista[2][n]
            n += 1
        n += 1
        for i in range(n,len(lista[2])-1): # conseguir rs1 aprovechando n
            rs1 += lista[2][i]
        imm = complemento_A2(numeroDecimal)
        for i in range(5):
            bin = imm[31-i] + bin
        bin = "010" + bin
        bin = registros[rs1] + bin
        bin = registros[lista[1]] + bin # rs2
        for i in range(7):
            bin = imm[26-i] + bin
    


    ######
    # addi
    ######
    elif(lista[0] == "addi"):
        bin += opCodes['addi']
        bin = registros[lista[1]] + bin
        bin = "000" + bin
        bin = registros[lista[2]] + bin
        imm = complemento_A2(lista[3])
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # slti
    ######
    elif(lista[0] == "slti"):
        bin += opCodes['slti']
        bin = registros[lista[1]] + bin
        bin = "010" + bin
        bin = registros[lista[2]] + bin
        imm = complemento_A2(lista[3])
        for i in range(12):
            bin = imm[31-i] + bin



    ######
    # sltiu
    ######
    elif(lista[0] == "sltiu"):
        bin += opCodes['sltiu']
        bin = registros[lista[1]] + bin
        bin = "011" + bin
        bin = registros[lista[2]] + bin
        imm = complemento_A2(lista[3])
        for i in range(12):
            bin = imm[31-i] + bin

    

    ######
    # xori
    ######
    elif(lista[0] == "xori"):
        bin += opCodes['xori']
        bin = registros[lista[1]] + bin
        bin = "100" + bin
        bin = registros[lista[2]] + bin
        imm = complemento_A2(lista[3])
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # ori
    ######
    elif(lista[0] == "ori"):
        bin += opCodes['ori']
        bin = registros[lista[1]] + bin
        bin = "110" + bin
        bin = registros[lista[2]] + bin
        imm = complemento_A2(lista[3])
        for i in range(12):
            bin = imm[31-i] + bin



    ######
    # andi
    ######
    elif(lista[0] == "andi"):
        bin += opCodes['andi']
        bin = registros[lista[1]] + bin
        bin = "111" + bin
        bin = registros[lista[2]] + bin
        imm = complemento_A2(lista[3])
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # slli
    ######
    elif(lista[0] == "slli"):
        bin += opCodes['slli']
        bin = registros[lista[1]] + bin
        bin = "001" + bin
        bin = registros[lista[2]] + bin
        shamt = complemento_A2(lista[3])
        for i in range(5):
            bin = shamt[31-i] + bin
        bin = "0000000" + bin
    


    ######
    # srli
    ######
    elif(lista[0] == "srli"):
        bin += opCodes['srli']
        bin = registros[lista[1]] + bin
        bin = "101" + bin
        bin = registros[lista[2]] + bin
        shamt = complemento_A2(lista[3])
        for i in range(5):
            bin = shamt[31-i] + bin
        bin = "0000000" + bin
    


    ######
    # srai
    ######
    elif(lista[0] == "srai"):
        bin += opCodes['srai']
        bin = registros[lista[1]] + bin
        bin = "101" + bin
        bin = registros[lista[2]] + bin
        shamt = complemento_A2(lista[3])
        for i in range(5):
            bin = shamt[31-i] + bin
        bin = "0100000" + bin



    ######
    # add
    ######
    elif(lista[0] == "add"):
        bin += opCodes['add']
        bin = registros[lista[1]] + bin
        bin = "000" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin



    ######
    # sub
    ######
    elif(lista[0] == "sub"):
        bin += opCodes['sub']
        bin = registros[lista[1]] + bin
        bin = "000" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0100000" + bin
    


    ######
    # sll
    ######
    elif(lista[0] == "sll"):
        bin += opCodes['sll']
        bin = registros[lista[1]] + bin
        bin = "001" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin
    


    ######
    # slt
    ######
    elif(lista[0] == "slt"):
        bin += opCodes['slt']
        bin = registros[lista[1]] + bin
        bin = "010" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin
    


    ######
    # sltu
    ######
    elif(lista[0] == "sltu"):
        bin += opCodes['sltu']
        bin = registros[lista[1]] + bin
        bin = "011" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin



    ######
    # xor
    ######
    elif(lista[0] == "xor"):
        bin += opCodes['xor']
        bin = registros[lista[1]] + bin
        bin = "100" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin
    


    ######
    # srl
    ######
    elif(lista[0] == "srl"):
        bin += opCodes['srl']
        bin = registros[lista[1]] + bin
        bin = "101" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin



    ######
    # sra
    ######
    elif(lista[0] == "sra"):
        bin += opCodes['sra']
        bin = registros[lista[1]] + bin
        bin = "101" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0100000" + bin



    ######
    # or
    ######
    elif(lista[0] == "or"):
        bin += opCodes['or']
        bin = registros[lista[1]] + bin
        bin = "110" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin
    


    ######
    # and
    ######
    elif(lista[0] == "and"):
        bin += opCodes['and']
        bin = registros[lista[1]] + bin
        bin = "111" + bin
        bin = registros[lista[2]] + bin # rs1
        bin = registros[lista[3]] + bin # rs2
        bin = "0000000" + bin 



    ######
    # ecall
    ######
    elif(lista[0] == "ecall"):
        return "00000000000000000000000001110011"
    


    ######
    # ebreak
    ######
    elif(lista[0] == "ebreak"):
        return "00000000000100000000000001110011"
    


    ######
    # csrrw
    ######
    elif(lista[0] == "csrrw"):
        bin += opCodes['csrrw']
        bin = registros[lista[1]] + bin
        bin = "001" + bin
        bin = registros[lista[3]] + bin
        imm = complemento_A2(lista[2])
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # csrrs
    ######
    elif(lista[0] == "csrrs"):
        bin += opCodes['csrrs']
        bin = registros[lista[1]] + bin
        bin = "010" + bin
        bin = registros[lista[3]] + bin
        imm = complemento_A2(lista[2])
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # csrrc
    ######
    elif(lista[0] == "csrrc"):
        bin += opCodes['csrrc']
        bin = registros[lista[1]] + bin
        bin = "011" + bin
        bin = registros[lista[3]] + bin
        imm = complemento_A2(lista[2])
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # csrrwi
    ######
    elif(lista[0] == "csrrwi"):
        bin += opCodes['csrrwi']
        bin = registros[lista[1]] + bin
        bin = "101" + bin
        bin = registros[lista[3]] + bin
        imm = complemento_A2(lista[3]) # zimm
        for i in range(5):
            bin = imm[31-i] + bin
        imm = complemento_A2(lista[2]) # csr
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # csrrsi
    ######
    elif(lista[0] == "csrrsi"):
        bin += opCodes['csrrsi']
        bin = registros[lista[1]] + bin
        bin = "110" + bin
        bin = registros[lista[3]] + bin
        imm = complemento_A2(lista[3]) # zimm
        for i in range(5):
            bin = imm[31-i] + bin
        imm = complemento_A2(lista[2]) # csr
        for i in range(12):
            bin = imm[31-i] + bin
    


    ######
    # csrrci
    ######
    elif(lista[0] == "csrrci"):
        bin += opCodes['csrrci']
        bin = registros[lista[1]] + bin
        bin = "111" + bin
        bin = registros[lista[3]] + bin
        imm = complemento_A2(lista[3]) # zimm
        for i in range(5):
            bin = imm[31-i] + bin
        imm = complemento_A2(lista[2]) # csr
        for i in range(12):
            bin = imm[31-i] + bin


    
    # SPECIAL INSTRUCTIONS

    ######
    # li
    ######
    elif(lista[0] == "li"):
        bin2:str = ""
        bin += opCodes['lui']
        bin = registros[lista[1]] + bin
        imm = complemento_A2(lista[2])
        for i in range(20):
            bin = imm[19-i] + bin # Primer numero, donde empieza. range(x), cuantos quiero
        bin += opCodes['addi']
        bin = registros[lista[1]] + bin
        bin = "000" + bin
        bin = registros[lista[1]] + bin
        for i in range(12):
            bin = imm[31-i] + bin
        return bin + bin2
    


    ######
    # not
    ######
    elif(lista[0] == "not"):
        bin += opCodes['xori']
        bin = registros[lista[1]] + bin
        bin = "100" + bin
        bin = registros[lista[2]] + bin
        for i in range(12):
            bin = ("1"*32)[31-i] + bin



    return bin

def complemento_A2(decimal:str) -> str:
    potencia:int = 31
    bin:str = ""
    if(decimal[0:2] == "0x"):
        for hex in decimal[2:(len(decimal))]:
            bin += hex_bin(hex)
        while(len(bin)<32):
            bin = "0" + bin
        return bin
    else:
        numero:int = int(decimal)
    if(decimal == "0"):
        return "00000000000000000000000000000000"
    if(decimal[0] != "-"): # Decimal positivo
        for i in range(32):
            if(2**(potencia-i) <= numero):
                numero -= 2**(potencia-i)
                bin += "1"
            else:
                bin += "0"
    else: # Decimal negativo
        numero *= -1
        for i in range(32):
            if(2**(potencia-i) >= numero):
                bin += "1"
            else:
                numero -= 2**(potencia-i)
                bin += "0"
    return bin

#-----------------------------------------MAIN----------------------------------------

registros:dict[str,str] = {
    'zero': "00000",
    'ra': "00001",
    'sp': "00010",
    'gp': "00011",
    'tp': "00100",
    't0': "00101",
    't1': "00110",
    't2': "00111",
    's0': "01000",
    'fp': "01000",
    's1': "01001",
    'a0': "01010",
    'a1': "01011",
    'a2': "01100",
    'a3': "01101",
    'a4': "01110",
    'a5': "01111",
    'a6': "10000",
    'a7': "10001",
    's2': "10010",
    's3': "10011",
    's4': "10100",
    's5': "10101",
    's6': "10110",
    's7': "10111",
    's8': "11000",
    's9': "11001",
    's10': "11010",
    's11': "11011",
    't3': "11100",
    't4': "11101",
    't5': "11110",
    't6': "11111",
    'x0': "00000",
    'x1': "00001",
    'x2': "00010",
    'x3': "00011",
    'x4': "00100",
    'x5': "00101",
    'x6': "00110",
    'x7': "00111",
    'x8': "01000",
    'x9': "01001",
    'x10': "01010",
    'x11': "01011",
    'x12': "01100",
    'x13': "01101",
    'x14': "01110",
    'x15': "01111",
    'x16': "10000",
    'x17': "10001",
    'x18': "10010",
    'x19': "10011",
    'x20': "10100",
    'x21': "10101",
    'x22': "10110",
    'x23': "10111",
    'x24': "11000",
    'x25': "11001",
    'x26': "11010",
    'x27': "11011",
    'x28': "11100",
    'x29': "11101",
    'x30': "11110",
    'x31': "11111"
}

opCodes:dict[str,str] = {
    'lui': "0110111",
    'auipc': "0010111",
    'jal': "1101111",
    'jalr': "1100111",
    'beq': "1100011",
    'bne': "1100011",
    'blt': "1100011",
    'bge': "1100011",
    'bltu': "1100011",
    'bgeu': "1100011",
    'lb': "0000011",
    'lh': "0000011",
    'lw': "0000011",
    'lbu': "0000011",
    'lhu': "0000011",
    'sb': "0100011",
    'sh': "0100011",
    'sw': "0100011",
    'addi': "0010011",
    'slti': "0010011",
    'sltiu': "0010011",
    'xori': "0010011",
    'ori': "0010011",
    'andi': "0010011",
    'slli': "0010011",
    'srli': "0010011",
    'srai': "0010011",
    'add': "0110011",
    'sub': "0110011",
    'sll': "0110011",
    'slt': "0110011",
    'sltu': "0110011",
    'xor': "0110011",
    'srl': "0110011",
    'sra': "0110011",
    'or': "0110011",
    'and': "0110011",
    'ecall': "1110011",
    'ebreak': "1110011",
    'csrrw': "1110011",
    'csrrs': "1110011",
    'csrrc': "1110011",
    'csrrwi': "1110011",
    'csrrsi': "1110011",
    'csrrci': "1110011"
}

types:dict[str,str] = {
    '0110111': "U",
    '0010111': "U",
    '1101111': "J",
    '1100111': "I",
    '1100011': "B",
}

hexa:dict[str,str] = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
}

instrucciones = tokens(path_asmbl)

inicializarFichero(path_compiler)

for i in range(len(instrucciones)):
    escribirLinea(assembler(instrucciones[i]),path_compiler)
