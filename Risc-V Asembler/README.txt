RISC-V Assembler
================
AUTOR: Eneko Jurado Varela
Ensamblador escrito en Python que traduce instrucciones RISC-V a código máquina binario.
Soporta el conjunto de instrucciones RV32I completo (incluyendo instrucciones CSR).


COMO USARLO
-----------
1. Escribe tus instrucciones en el fichero "asmbl.csv"
2. Ejecuta el script: python assembler.py
3. El resultado aparecerá en "riscv_bin.csv"


SINTAXIS
--------
¡ATENCIÓN! La sintaxis tiene algunas diferencias respecto al ensamblador estándar RISC-V:

  1. NO se usan espacios entre comas ni entre argumentos.
     Correcto:   addi s2,zero,-7
     Incorrecto: addi s2, zero, -7

  2. NO se soportan etiquetas (labels).
     Incorrecto: loop:
                     addi t0,t0,1
                     bne t0,t1,loop
     Los saltos y branches deben usar el inmediato numérico directamente.

  3. Hay exactamente un espacio entre el nombre de la instrucción y sus argumentos.
     Correcto:   add t0,t1,t2
     Incorrecto: add  t0,t1,t2  (doble espacio)


NOMENCLATURA DE REGISTROS
--------------------------
Puedes usar cualquiera de las dos nomenclaturas para referirte a los registros,
e incluso mezclarlas dentro del mismo fichero:

  Nomenclatura ABI (nombre):   zero, ra, sp, t0, s1, a0, ...
  Nomenclatura numérica:       x0,   x1, x2, x5, x9, x10, ...

  Ejemplos equivalentes:
     addi t0,zero,10
     addi x5,x0,10


NOMENCLATURA DE INMEDIATOS
---------------------------
Los inmediatos se pueden escribir en decimal o en hexadecimal:

  Decimal:      addi t0,zero,-7
  Hexadecimal:  addi t0,zero,0xFF

  El signo negativo solo aplica a la notación decimal.


LINEAS DE GUIA
--------------
Puedes escribir líneas de texto libre para organizarte, siempre que sean
de 6 caracteres o menos. Por ejemplo:

     while:
         addi t0,t0,1
         bne t0,t1,8
     end:

Estas líneas actúan como comentarios de bloque y son ignoradas por el ensamblador.


COMENTARIOS EN LINEA
--------------------
Puedes añadir comentarios al final de cualquier instrucción separados por un espacio:

     addi t0,zero,10 inicializar contador
     add t1,t1,t0 acumular resultado


asmbl.csv GUIA
--------------
El fichero 'asmbl.csv' debe de ser creado manualmente en el directorio donde se
encuentre el archivo .py
El archivo 'riscv_bin.csv' se creará automáticamente.


EJEMPLO DE FICHERO asmbl.csv
-----------------------------
loop:
addi t0,x0,1 inicializar t0 con nomenclatura mixta
addi x6,x6,-1 decrementar con nomenclatura numérica
end:
bne t1,zero,-8 volver a loop si t1 != 0
ecall


INSTRUCCIONES SOPORTADAS
-------------------------
Tipo U:  lui, auipc
Tipo J:  jal
Tipo I:  jalr, lb, lh, lw, lbu, lhu, addi, slti, sltiu, xori, ori, andi, slli, srli, srai
Tipo B:  beq, bne, blt, bge, bltu, bgeu
Tipo S:  sb, sh, sw
Tipo R:  add, sub, sll, slt, sltu, xor, srl, sra, or, and
Sistema: ecall, ebreak, csrrw, csrrs, csrrc, csrrwi, csrrsi, csrrci
Especiales: li, not









RISC-V Assembler
================
AUTHOR: Eneko Jurado Varela
Assembler written in Python that translates RISC-V instructions into binary machine code.
Supports the full RV32I instruction set (including CSR instructions).


HOW TO USE
----------
1. Write your instructions in the "asmbl.csv" file
2. Run the script: python assembler.py
3. The result will appear in "riscv_bin.csv"


SYNTAX
------
WARNING! The syntax has some differences from the standard RISC-V assembler:

  1. NO spaces between commas or arguments.
     Correct:   addi s2,zero,-7
     Incorrect: addi s2, zero, -7

  2. Labels are NOT supported.
     Incorrect: loop:
                    addi t0,t0,1
                    bne t0,t1,loop
     Jumps and branches must use the numeric immediate directly.

  3. There is exactly one space between the instruction name and its arguments.
     Correct:   add t0,t1,t2
     Incorrect: add  t0,t1,t2  (double space)


REGISTER NAMING
---------------
You can use either naming convention for registers, and even mix them
within the same file:

  ABI names:        zero, ra, sp, t0, s1, a0, ...
  Numeric names:    x0,   x1, x2, x5, x9, x10, ...

  Equivalent examples:
     addi t0,zero,10
     addi x5,x0,10


IMMEDIATE VALUES
----------------
Immediates can be written in decimal or hexadecimal:

  Decimal:      addi t0,zero,-7
  Hexadecimal:  addi t0,zero,0xFF

  The negative sign only applies to decimal notation.


GUIDE LINES
-----------
You can write free-text lines to organize your code, as long as they are
6 characters or fewer. For example:

     while:
         addi t0,t0,1
         bne t0,t1,8
     end:

These lines act as block comments and are ignored by the assembler.


INLINE COMMENTS
---------------
You can add comments at the end of any instruction, separated by a space:

     addi t0,zero,10 initialize counter
     add t1,t1,t0 accumulate result


asmbl.csv GUIDE
---------------
The file 'asmbl.csv' must be created manually in the same directory as
the .py file.
The file 'riscv_bin.csv' will be created automatically.


EXAMPLE asmbl.csv FILE
-----------------------
loop:
addi t0,x0,1 initialize t0 using mixed naming
addi x6,x6,-1 decrement using numeric naming
end:
bne t1,zero,-8 go back to loop if t1 != 0
ecall


SUPPORTED INSTRUCTIONS
-----------------------
Type U:  lui, auipc
Type J:  jal
Type I:  jalr, lb, lh, lw, lbu, lhu, addi, slti, sltiu, xori, ori, andi, slli, srli, srai
Type B:  beq, bne, blt, bge, bltu, bgeu
Type S:  sb, sh, sw
Type R:  add, sub, sll, slt, sltu, xor, srl, sra, or, and
System:  ecall, ebreak, csrrw, csrrs, csrrc, csrrwi, csrrsi, csrrci
Specials: li, not
