RISC-V Assembler
================

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

  3. Hay un espacio entre el nombre de la instrucción y sus argumentos.
     Correcto:   add t0,t1,t2
     Incorrecto: add  t0,t1,t2  (doble espacio)


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


EJEMPLO DE FICHERO asmbl.csv
-----------------------------
loop:
addi t0,t0,1 incrementar t0
addi t1,t1,-1 decrementar t1
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
