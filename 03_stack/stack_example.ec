FF: 55  # 255 in hex
FE: 34
FE: 00
FC: 00
FB: 00
FA: 00
F9: 00
F8: 00
# -
# -
# -
05: 00
04: 00
03: 00
02: XX
01: XX
00: XX < - PC

R0: 34
R1: 12
R2: 55

PUSH instruction
e.g.
PUSH R0
PUSH R1

POP instruction
e.g.
POP R0
POP R1

PUSH R0  # FF: 34
PUSH R1  # FF: 12
POP R0
POP R1
PUSH R2  # overwrites FF value
