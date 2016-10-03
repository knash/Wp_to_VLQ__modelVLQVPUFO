# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Mon 3 Oct 2016 13:50:57



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
KWuBPL = Parameter(name = 'KWuBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWuBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 1 ])

KWcBPL = Parameter(name = 'KWcBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWcBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 2 ])

KWtBPL = Parameter(name = 'KWtBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWtBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 3 ])

KZdBPL = Parameter(name = 'KZdBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZdBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 4 ])

KZsBPL = Parameter(name = 'KZsBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZsBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 5 ])

KZbBPL = Parameter(name = 'KZbBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZbBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 6 ])

KHdBPL = Parameter(name = 'KHdBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHdBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 7 ])

KHsBPL = Parameter(name = 'KHsBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHsBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 8 ])

KHbBPL = Parameter(name = 'KHbBPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHbBPL}',
                   lhablock = 'KBSM',
                   lhacode = [ 9 ])

KWuBPR = Parameter(name = 'KWuBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWuBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 10 ])

KWcBPR = Parameter(name = 'KWcBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWcBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 11 ])

KWtBPR = Parameter(name = 'KWtBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWtBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 12 ])

KZdBPR = Parameter(name = 'KZdBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZdBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 13 ])

KZsBPR = Parameter(name = 'KZsBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZsBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 14 ])

KZbBPR = Parameter(name = 'KZbBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZbBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 15 ])

KHdBPR = Parameter(name = 'KHdBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHdBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 16 ])

KHsBPR = Parameter(name = 'KHsBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHsBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 17 ])

KHbBPR = Parameter(name = 'KHbBPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHbBPR}',
                   lhablock = 'KBSM',
                   lhacode = [ 18 ])

KWdTPL = Parameter(name = 'KWdTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWdTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 1 ])

KWsTPL = Parameter(name = 'KWsTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWsTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 2 ])

KWbTPL = Parameter(name = 'KWbTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWbTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 3 ])

KZuTPL = Parameter(name = 'KZuTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZuTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 4 ])

KZcTPL = Parameter(name = 'KZcTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZcTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 5 ])

KZtTPL = Parameter(name = 'KZtTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZtTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 6 ])

KHuTPL = Parameter(name = 'KHuTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHuTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 7 ])

KHcTPL = Parameter(name = 'KHcTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHcTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 8 ])

KHtTPL = Parameter(name = 'KHtTPL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHtTPL}',
                   lhablock = 'KTSM',
                   lhacode = [ 9 ])

KWdTPR = Parameter(name = 'KWdTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWdTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 10 ])

KWsTPR = Parameter(name = 'KWsTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWsTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 11 ])

KWbTPR = Parameter(name = 'KWbTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWbTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 12 ])

KZuTPR = Parameter(name = 'KZuTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZuTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 13 ])

KZcTPR = Parameter(name = 'KZcTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZcTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 14 ])

KZtTPR = Parameter(name = 'KZtTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZtTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 15 ])

KHuTPR = Parameter(name = 'KHuTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHuTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 16 ])

KHcTPR = Parameter(name = 'KHcTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHcTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 17 ])

KHtTPR = Parameter(name = 'KHtTPR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHtTPR}',
                   lhablock = 'KTSM',
                   lhacode = [ 18 ])

KWPudL = Parameter(name = 'KWPudL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPudL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 1 ])

KWPusL = Parameter(name = 'KWPusL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPusL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 2 ])

KWPubL = Parameter(name = 'KWPubL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPubL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 3 ])

KWPcdL = Parameter(name = 'KWPcdL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcdL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 4 ])

KWPcsL = Parameter(name = 'KWPcsL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcsL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 5 ])

KWPcbL = Parameter(name = 'KWPcbL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcbL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 6 ])

KWPtdL = Parameter(name = 'KWPtdL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtdL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 7 ])

KWPtsL = Parameter(name = 'KWPtsL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtsL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 8 ])

KWPtbL = Parameter(name = 'KWPtbL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtbL}',
                   lhablock = 'KWPSM',
                   lhacode = [ 9 ])

KWPudR = Parameter(name = 'KWPudR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPudR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 10 ])

KWPusR = Parameter(name = 'KWPusR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPusR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 11 ])

KWPubR = Parameter(name = 'KWPubR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPubR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 12 ])

KWPcdR = Parameter(name = 'KWPcdR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcdR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 13 ])

KWPcsR = Parameter(name = 'KWPcsR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcsR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 14 ])

KWPcbR = Parameter(name = 'KWPcbR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcbR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 15 ])

KWPtdR = Parameter(name = 'KWPtdR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtdR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 16 ])

KWPtsR = Parameter(name = 'KWPtsR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtsR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 17 ])

KWPtbR = Parameter(name = 'KWPtbR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtbR}',
                   lhablock = 'KWPSM',
                   lhacode = [ 18 ])

KWPuXL = Parameter(name = 'KWPuXL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPuXL}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 1 ])

KWPcXL = Parameter(name = 'KWPcXL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcXL}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 2 ])

KWPtXL = Parameter(name = 'KWPtXL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtXL}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 3 ])

KWPdTPL = Parameter(name = 'KWPdTPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPdTPL}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 4 ])

KWPsTPL = Parameter(name = 'KWPsTPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPsTPL}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 5 ])

KWPbTPL = Parameter(name = 'KWPbTPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPbTPL}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 6 ])

KWPuBPL = Parameter(name = 'KWPuBPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPuBPL}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 7 ])

KWPcBPL = Parameter(name = 'KWPcBPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPcBPL}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 8 ])

KWPtBPL = Parameter(name = 'KWPtBPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPtBPL}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 9 ])

KWPdYL = Parameter(name = 'KWPdYL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPdYL}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 10 ])

KWPsYL = Parameter(name = 'KWPsYL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPsYL}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 11 ])

KWPbYL = Parameter(name = 'KWPbYL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPbYL}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 12 ])

KWPuXR = Parameter(name = 'KWPuXR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPuXR}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 13 ])

KWPcXR = Parameter(name = 'KWPcXR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPcXR}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 14 ])

KWPtXR = Parameter(name = 'KWPtXR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPtXR}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 15 ])

KWPdTPR = Parameter(name = 'KWPdTPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPdTPR}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 16 ])

KWPsTPR = Parameter(name = 'KWPsTPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPsTPR}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 17 ])

KWPbTPR = Parameter(name = 'KWPbTPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPbTPR}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 18 ])

KWPuBPR = Parameter(name = 'KWPuBPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPuBPR}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 19 ])

KWPcBPR = Parameter(name = 'KWPcBPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPcBPR}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 20 ])

KWPtBPR = Parameter(name = 'KWPtBPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPtBPR}',
                    lhablock = 'KWPSMVLQ',
                    lhacode = [ 21 ])

KWPdYR = Parameter(name = 'KWPdYR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPdYR}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 22 ])

KWPsYR = Parameter(name = 'KWPsYR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPsYR}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 23 ])

KWPbYR = Parameter(name = 'KWPbYR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KWPbYR}',
                   lhablock = 'KWPSMVLQ',
                   lhacode = [ 24 ])

KWPXTPL = Parameter(name = 'KWPXTPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPXTPL}',
                    lhablock = 'KWPVLQ',
                    lhacode = [ 1 ])

KWPTPBPL = Parameter(name = 'KWPTPBPL',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KWPTPBPL}',
                     lhablock = 'KWPVLQ',
                     lhacode = [ 2 ])

KWPBPYL = Parameter(name = 'KWPBPYL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPBPYL}',
                    lhablock = 'KWPVLQ',
                    lhacode = [ 3 ])

KWPXTPR = Parameter(name = 'KWPXTPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPXTPR}',
                    lhablock = 'KWPVLQ',
                    lhacode = [ 4 ])

KWPTPBPR = Parameter(name = 'KWPTPBPR',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KWPTPBPR}',
                     lhablock = 'KWPVLQ',
                     lhacode = [ 5 ])

KWPBPYR = Parameter(name = 'KWPBPYR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KWPBPYR}',
                    lhablock = 'KWPVLQ',
                    lhacode = [ 6 ])

KWuXL = Parameter(name = 'KWuXL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWuXL}',
                  lhablock = 'KXSM',
                  lhacode = [ 1 ])

KWcXL = Parameter(name = 'KWcXL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWcXL}',
                  lhablock = 'KXSM',
                  lhacode = [ 2 ])

KWtXL = Parameter(name = 'KWtXL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWtXL}',
                  lhablock = 'KXSM',
                  lhacode = [ 3 ])

KWuXR = Parameter(name = 'KWuXR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWuXR}',
                  lhablock = 'KXSM',
                  lhacode = [ 4 ])

KWcXR = Parameter(name = 'KWcXR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWcXR}',
                  lhablock = 'KXSM',
                  lhacode = [ 5 ])

KWtXR = Parameter(name = 'KWtXR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWtXR}',
                  lhablock = 'KXSM',
                  lhacode = [ 6 ])

KWdYL = Parameter(name = 'KWdYL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWdYL}',
                  lhablock = 'KYSM',
                  lhacode = [ 1 ])

KWsYL = Parameter(name = 'KWsYL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWsYL}',
                  lhablock = 'KYSM',
                  lhacode = [ 2 ])

KWbYL = Parameter(name = 'KWbYL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWbYL}',
                  lhablock = 'KYSM',
                  lhacode = [ 3 ])

KWdYR = Parameter(name = 'KWdYR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWdYR}',
                  lhablock = 'KYSM',
                  lhacode = [ 4 ])

KWsYR = Parameter(name = 'KWsYR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWsYR}',
                  lhablock = 'KYSM',
                  lhacode = [ 5 ])

KWbYR = Parameter(name = 'KWbYR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KWbYR}',
                  lhablock = 'KYSM',
                  lhacode = [ 6 ])

KZTTL = Parameter(name = 'KZTTL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZTTL}',
                  lhablock = 'KZFFL',
                  lhacode = [ 1 ])

KZTTR = Parameter(name = 'KZTTR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZTTR}',
                  lhablock = 'KZFFL',
                  lhacode = [ 2 ])

KZBBL = Parameter(name = 'KZBBL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZBBL}',
                  lhablock = 'KZFFL',
                  lhacode = [ 3 ])

KZBBR = Parameter(name = 'KZBBR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZBBR}',
                  lhablock = 'KZFFL',
                  lhacode = [ 4 ])

KZXXL = Parameter(name = 'KZXXL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZXXL}',
                  lhablock = 'KZFFL',
                  lhacode = [ 5 ])

KZXXR = Parameter(name = 'KZXXR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZXXR}',
                  lhablock = 'KZFFL',
                  lhacode = [ 6 ])

KZYYL = Parameter(name = 'KZYYL',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZYYL}',
                  lhablock = 'KZFFL',
                  lhacode = [ 7 ])

KZYYR = Parameter(name = 'KZYYR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KZYYR}',
                  lhablock = 'KZFFL',
                  lhacode = [ 8 ])

KZPuuL = Parameter(name = 'KZPuuL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPuuL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 1 ])

KZPucL = Parameter(name = 'KZPucL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPucL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 2 ])

KZPutL = Parameter(name = 'KZPutL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPutL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 3 ])

KZPccL = Parameter(name = 'KZPccL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPccL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 4 ])

KZPctL = Parameter(name = 'KZPctL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPctL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 5 ])

KZPttL = Parameter(name = 'KZPttL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPttL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 6 ])

KZPddL = Parameter(name = 'KZPddL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPddL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 7 ])

KZPdsL = Parameter(name = 'KZPdsL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPdsL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 8 ])

KZPdbL = Parameter(name = 'KZPdbL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPdbL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 9 ])

KZPssL = Parameter(name = 'KZPssL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPssL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 10 ])

KZPsbL = Parameter(name = 'KZPsbL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPsbL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 11 ])

KZPbbL = Parameter(name = 'KZPbbL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPbbL}',
                   lhablock = 'KZPSM',
                   lhacode = [ 12 ])

KZPuuR = Parameter(name = 'KZPuuR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPuuR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 13 ])

KZPucR = Parameter(name = 'KZPucR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPucR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 14 ])

KZPutR = Parameter(name = 'KZPutR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPutR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 15 ])

KZPccR = Parameter(name = 'KZPccR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPccR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 16 ])

KZPctR = Parameter(name = 'KZPctR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPctR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 17 ])

KZPttR = Parameter(name = 'KZPttR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPttR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 18 ])

KZPddR = Parameter(name = 'KZPddR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPddR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 19 ])

KZPdsR = Parameter(name = 'KZPdsR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPdsR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 20 ])

KZPdbR = Parameter(name = 'KZPdbR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPdbR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 21 ])

KZPssR = Parameter(name = 'KZPssR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPssR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 22 ])

KZPsbR = Parameter(name = 'KZPsbR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPsbR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 23 ])

KZPbbR = Parameter(name = 'KZPbbR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPbbR}',
                   lhablock = 'KZPSM',
                   lhacode = [ 24 ])

KZPuTPL = Parameter(name = 'KZPuTPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPuTPL}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 1 ])

KZPcTPL = Parameter(name = 'KZPcTPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPcTPL}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 2 ])

KZPtTPL = Parameter(name = 'KZPtTPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPtTPL}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 3 ])

KZPdBPL = Parameter(name = 'KZPdBPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPdBPL}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 4 ])

KZPsBPL = Parameter(name = 'KZPsBPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPsBPL}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 5 ])

KZPbBPL = Parameter(name = 'KZPbBPL',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPbBPL}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 6 ])

KZPuTPR = Parameter(name = 'KZPuTPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPuTPR}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 7 ])

KZPcTPR = Parameter(name = 'KZPcTPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPcTPR}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 8 ])

KZPtTPR = Parameter(name = 'KZPtTPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPtTPR}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 9 ])

KZPdBPR = Parameter(name = 'KZPdBPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPdBPR}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 10 ])

KZPsBPR = Parameter(name = 'KZPsBPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPsBPR}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 11 ])

KZPbBPR = Parameter(name = 'KZPbBPR',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KZPbBPR}',
                    lhablock = 'KZPSMVLQ',
                    lhacode = [ 12 ])

KZPTPTPL = Parameter(name = 'KZPTPTPL',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KZPTPTPL}',
                     lhablock = 'KZPVLQ',
                     lhacode = [ 1 ])

KZPBPBPL = Parameter(name = 'KZPBPBPL',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KZPBPBPL}',
                     lhablock = 'KZPVLQ',
                     lhacode = [ 2 ])

KZPXXL = Parameter(name = 'KZPXXL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPXXL}',
                   lhablock = 'KZPVLQ',
                   lhacode = [ 3 ])

KZPYYL = Parameter(name = 'KZPYYL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPYYL}',
                   lhablock = 'KZPVLQ',
                   lhacode = [ 4 ])

KZPTPTPR = Parameter(name = 'KZPTPTPR',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KZPTPTPR}',
                     lhablock = 'KZPVLQ',
                     lhacode = [ 5 ])

KZPBPBPR = Parameter(name = 'KZPBPBPR',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KZPBPBPR}',
                     lhablock = 'KZPVLQ',
                     lhacode = [ 6 ])

KZPXXR = Parameter(name = 'KZPXXR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPXXR}',
                   lhablock = 'KZPVLQ',
                   lhacode = [ 7 ])

KZPYYR = Parameter(name = 'KZPYYR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KZPYYR}',
                   lhablock = 'KZPVLQ',
                   lhacode = [ 8 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MX = Parameter(name = 'MX',
               nature = 'external',
               type = 'real',
               value = 600,
               texname = '\\text{MX}',
               lhablock = 'MASS',
               lhacode = [ 6000005 ])

MTP = Parameter(name = 'MTP',
                nature = 'external',
                type = 'real',
                value = 600,
                texname = '\\text{MTP}',
                lhablock = 'MASS',
                lhacode = [ 6000006 ])

MBP = Parameter(name = 'MBP',
                nature = 'external',
                type = 'real',
                value = 600,
                texname = '\\text{MBP}',
                lhablock = 'MASS',
                lhacode = [ 6000007 ])

MY = Parameter(name = 'MY',
               nature = 'external',
               type = 'real',
               value = 600,
               texname = '\\text{MY}',
               lhablock = 'MASS',
               lhacode = [ 6000008 ])

MZP = Parameter(name = 'MZP',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MZP}',
                lhablock = 'MASS',
                lhacode = [ 6000023 ])

MWP = Parameter(name = 'MWP',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MWP}',
                lhablock = 'MASS',
                lhacode = [ 6000024 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WX = Parameter(name = 'WX',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{WX}',
               lhablock = 'DECAY',
               lhacode = [ 6000005 ])

WTP = Parameter(name = 'WTP',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WTP}',
                lhablock = 'DECAY',
                lhacode = [ 6000006 ])

WBP = Parameter(name = 'WBP',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WBP}',
                lhablock = 'DECAY',
                lhacode = [ 6000007 ])

WY = Parameter(name = 'WY',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{WY}',
               lhablock = 'DECAY',
               lhacode = [ 6000008 ])

WZP = Parameter(name = 'WZP',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WZP}',
                lhablock = 'DECAY',
                lhacode = [ 6000023 ])

WWP = Parameter(name = 'WWP',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WWP}',
                lhablock = 'DECAY',
                lhacode = [ 6000024 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

KHqBPL1 = Parameter(name = 'KHqBPL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHdBPL',
                    texname = '\\text{KHqBPL1}')

KHqBPL2 = Parameter(name = 'KHqBPL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHsBPL',
                    texname = '\\text{KHqBPL2}')

KHqBPL3 = Parameter(name = 'KHqBPL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHbBPL',
                    texname = '\\text{KHqBPL3}')

KHqBPR1 = Parameter(name = 'KHqBPR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHdBPR',
                    texname = '\\text{KHqBPR1}')

KHqBPR2 = Parameter(name = 'KHqBPR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHsBPR',
                    texname = '\\text{KHqBPR2}')

KHqBPR3 = Parameter(name = 'KHqBPR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHbBPR',
                    texname = '\\text{KHqBPR3}')

KHqTPL1 = Parameter(name = 'KHqTPL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHuTPL',
                    texname = '\\text{KHqTPL1}')

KHqTPL2 = Parameter(name = 'KHqTPL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHcTPL',
                    texname = '\\text{KHqTPL2}')

KHqTPL3 = Parameter(name = 'KHqTPL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHtTPL',
                    texname = '\\text{KHqTPL3}')

KHqTPR1 = Parameter(name = 'KHqTPR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHuTPR',
                    texname = '\\text{KHqTPR1}')

KHqTPR2 = Parameter(name = 'KHqTPR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHcTPR',
                    texname = '\\text{KHqTPR2}')

KHqTPR3 = Parameter(name = 'KHqTPR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHtTPR',
                    texname = '\\text{KHqTPR3}')

KWPqBPL1 = Parameter(name = 'KWPqBPL1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPuBPL',
                     texname = '\\text{KWPqBPL1}')

KWPqBPL2 = Parameter(name = 'KWPqBPL2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPcBPL',
                     texname = '\\text{KWPqBPL2}')

KWPqBPL3 = Parameter(name = 'KWPqBPL3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPtBPL',
                     texname = '\\text{KWPqBPL3}')

KWPqBPR1 = Parameter(name = 'KWPqBPR1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPuBPR',
                     texname = '\\text{KWPqBPR1}')

KWPqBPR2 = Parameter(name = 'KWPqBPR2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPcBPR',
                     texname = '\\text{KWPqBPR2}')

KWPqBPR3 = Parameter(name = 'KWPqBPR3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPtBPR',
                     texname = '\\text{KWPqBPR3}')

KWPqqL1x1 = Parameter(name = 'KWPqqL1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL1x1}')

KWPqqL1x2 = Parameter(name = 'KWPqqL1x2',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL1x2}')

KWPqqL1x3 = Parameter(name = 'KWPqqL1x3',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL1x3}')

KWPqqL2x1 = Parameter(name = 'KWPqqL2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL2x1}')

KWPqqL2x2 = Parameter(name = 'KWPqqL2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL2x2}')

KWPqqL2x3 = Parameter(name = 'KWPqqL2x3',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL2x3}')

KWPqqL3x1 = Parameter(name = 'KWPqqL3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL3x1}')

KWPqqL3x2 = Parameter(name = 'KWPqqL3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL3x2}')

KWPqqL3x3 = Parameter(name = 'KWPqqL3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqL3x3}')

KWPqqR1x1 = Parameter(name = 'KWPqqR1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR1x1}')

KWPqqR1x2 = Parameter(name = 'KWPqqR1x2',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR1x2}')

KWPqqR1x3 = Parameter(name = 'KWPqqR1x3',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR1x3}')

KWPqqR2x1 = Parameter(name = 'KWPqqR2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR2x1}')

KWPqqR2x2 = Parameter(name = 'KWPqqR2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR2x2}')

KWPqqR2x3 = Parameter(name = 'KWPqqR2x3',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR2x3}')

KWPqqR3x1 = Parameter(name = 'KWPqqR3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR3x1}')

KWPqqR3x2 = Parameter(name = 'KWPqqR3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR3x2}')

KWPqqR3x3 = Parameter(name = 'KWPqqR3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '1',
                      texname = '\\text{KWPqqR3x3}')

KWPqTPL1 = Parameter(name = 'KWPqTPL1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPdTPL',
                     texname = '\\text{KWPqTPL1}')

KWPqTPL2 = Parameter(name = 'KWPqTPL2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPsTPL',
                     texname = '\\text{KWPqTPL2}')

KWPqTPL3 = Parameter(name = 'KWPqTPL3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPbTPL',
                     texname = '\\text{KWPqTPL3}')

KWPqTPR1 = Parameter(name = 'KWPqTPR1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPdTPR',
                     texname = '\\text{KWPqTPR1}')

KWPqTPR2 = Parameter(name = 'KWPqTPR2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPsTPR',
                     texname = '\\text{KWPqTPR2}')

KWPqTPR3 = Parameter(name = 'KWPqTPR3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KWPbTPR',
                     texname = '\\text{KWPqTPR3}')

KWPqXL1 = Parameter(name = 'KWPqXL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPuXL',
                    texname = '\\text{KWPqXL1}')

KWPqXL2 = Parameter(name = 'KWPqXL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPcXL',
                    texname = '\\text{KWPqXL2}')

KWPqXL3 = Parameter(name = 'KWPqXL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPtXL',
                    texname = '\\text{KWPqXL3}')

KWPqXR1 = Parameter(name = 'KWPqXR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPuXR',
                    texname = '\\text{KWPqXR1}')

KWPqXR2 = Parameter(name = 'KWPqXR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPcXR',
                    texname = '\\text{KWPqXR2}')

KWPqXR3 = Parameter(name = 'KWPqXR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPtXR',
                    texname = '\\text{KWPqXR3}')

KWPqYL1 = Parameter(name = 'KWPqYL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPdYL',
                    texname = '\\text{KWPqYL1}')

KWPqYL2 = Parameter(name = 'KWPqYL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPsYL',
                    texname = '\\text{KWPqYL2}')

KWPqYL3 = Parameter(name = 'KWPqYL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPbYL',
                    texname = '\\text{KWPqYL3}')

KWPqYR1 = Parameter(name = 'KWPqYR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPdYR',
                    texname = '\\text{KWPqYR1}')

KWPqYR2 = Parameter(name = 'KWPqYR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPsYR',
                    texname = '\\text{KWPqYR2}')

KWPqYR3 = Parameter(name = 'KWPqYR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWPbYR',
                    texname = '\\text{KWPqYR3}')

KWqBPL1 = Parameter(name = 'KWqBPL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWuBPL',
                    texname = '\\text{KWqBPL1}')

KWqBPL2 = Parameter(name = 'KWqBPL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWcBPL',
                    texname = '\\text{KWqBPL2}')

KWqBPL3 = Parameter(name = 'KWqBPL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWtBPL',
                    texname = '\\text{KWqBPL3}')

KWqBPR1 = Parameter(name = 'KWqBPR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWuBPR',
                    texname = '\\text{KWqBPR1}')

KWqBPR2 = Parameter(name = 'KWqBPR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWcBPR',
                    texname = '\\text{KWqBPR2}')

KWqBPR3 = Parameter(name = 'KWqBPR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWtBPR',
                    texname = '\\text{KWqBPR3}')

KWqTPL1 = Parameter(name = 'KWqTPL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWdTPL',
                    texname = '\\text{KWqTPL1}')

KWqTPL2 = Parameter(name = 'KWqTPL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWsTPL',
                    texname = '\\text{KWqTPL2}')

KWqTPL3 = Parameter(name = 'KWqTPL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWbTPL',
                    texname = '\\text{KWqTPL3}')

KWqTPR1 = Parameter(name = 'KWqTPR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWdTPR',
                    texname = '\\text{KWqTPR1}')

KWqTPR2 = Parameter(name = 'KWqTPR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWsTPR',
                    texname = '\\text{KWqTPR2}')

KWqTPR3 = Parameter(name = 'KWqTPR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KWbTPR',
                    texname = '\\text{KWqTPR3}')

KWqXL1 = Parameter(name = 'KWqXL1',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWuXL',
                   texname = '\\text{KWqXL1}')

KWqXL2 = Parameter(name = 'KWqXL2',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWcXL',
                   texname = '\\text{KWqXL2}')

KWqXL3 = Parameter(name = 'KWqXL3',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWtXL',
                   texname = '\\text{KWqXL3}')

KWqXR1 = Parameter(name = 'KWqXR1',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWuXR',
                   texname = '\\text{KWqXR1}')

KWqXR2 = Parameter(name = 'KWqXR2',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWcXR',
                   texname = '\\text{KWqXR2}')

KWqXR3 = Parameter(name = 'KWqXR3',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWtXR',
                   texname = '\\text{KWqXR3}')

KWqYL1 = Parameter(name = 'KWqYL1',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWdYL',
                   texname = '\\text{KWqYL1}')

KWqYL2 = Parameter(name = 'KWqYL2',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWsYL',
                   texname = '\\text{KWqYL2}')

KWqYL3 = Parameter(name = 'KWqYL3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{KWqYL3}')

KWqYR1 = Parameter(name = 'KWqYR1',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWdYR',
                   texname = '\\text{KWqYR1}')

KWqYR2 = Parameter(name = 'KWqYR2',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWsYR',
                   texname = '\\text{KWqYR2}')

KWqYR3 = Parameter(name = 'KWqYR3',
                   nature = 'internal',
                   type = 'real',
                   value = 'KWbYR',
                   texname = '\\text{KWqYR3}')

KZPdqdqL1x1 = Parameter(name = 'KZPdqdqL1x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPddL',
                        texname = '\\text{KZPdqdqL1x1}')

KZPdqdqL1x2 = Parameter(name = 'KZPdqdqL1x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdsL',
                        texname = '\\text{KZPdqdqL1x2}')

KZPdqdqL1x3 = Parameter(name = 'KZPdqdqL1x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdbL',
                        texname = '\\text{KZPdqdqL1x3}')

KZPdqdqL2x1 = Parameter(name = 'KZPdqdqL2x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdsL',
                        texname = '\\text{KZPdqdqL2x1}')

KZPdqdqL2x2 = Parameter(name = 'KZPdqdqL2x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPssL',
                        texname = '\\text{KZPdqdqL2x2}')

KZPdqdqL2x3 = Parameter(name = 'KZPdqdqL2x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPsbL',
                        texname = '\\text{KZPdqdqL2x3}')

KZPdqdqL3x1 = Parameter(name = 'KZPdqdqL3x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdbL',
                        texname = '\\text{KZPdqdqL3x1}')

KZPdqdqL3x2 = Parameter(name = 'KZPdqdqL3x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPsbL',
                        texname = '\\text{KZPdqdqL3x2}')

KZPdqdqL3x3 = Parameter(name = 'KZPdqdqL3x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPbbL',
                        texname = '\\text{KZPdqdqL3x3}')

KZPdqdqR1x1 = Parameter(name = 'KZPdqdqR1x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPddR',
                        texname = '\\text{KZPdqdqR1x1}')

KZPdqdqR1x2 = Parameter(name = 'KZPdqdqR1x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdsR',
                        texname = '\\text{KZPdqdqR1x2}')

KZPdqdqR1x3 = Parameter(name = 'KZPdqdqR1x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdbR',
                        texname = '\\text{KZPdqdqR1x3}')

KZPdqdqR2x1 = Parameter(name = 'KZPdqdqR2x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdsR',
                        texname = '\\text{KZPdqdqR2x1}')

KZPdqdqR2x2 = Parameter(name = 'KZPdqdqR2x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPssR',
                        texname = '\\text{KZPdqdqR2x2}')

KZPdqdqR2x3 = Parameter(name = 'KZPdqdqR2x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPsbR',
                        texname = '\\text{KZPdqdqR2x3}')

KZPdqdqR3x1 = Parameter(name = 'KZPdqdqR3x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPdbR',
                        texname = '\\text{KZPdqdqR3x1}')

KZPdqdqR3x2 = Parameter(name = 'KZPdqdqR3x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPsbR',
                        texname = '\\text{KZPdqdqR3x2}')

KZPdqdqR3x3 = Parameter(name = 'KZPdqdqR3x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPbbR',
                        texname = '\\text{KZPdqdqR3x3}')

KZPqBPL1 = Parameter(name = 'KZPqBPL1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPdBPL',
                     texname = '\\text{KZPqBPL1}')

KZPqBPL2 = Parameter(name = 'KZPqBPL2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPsBPL',
                     texname = '\\text{KZPqBPL2}')

KZPqBPL3 = Parameter(name = 'KZPqBPL3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPbBPL',
                     texname = '\\text{KZPqBPL3}')

KZPqBPR1 = Parameter(name = 'KZPqBPR1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPdBPR',
                     texname = '\\text{KZPqBPR1}')

KZPqBPR2 = Parameter(name = 'KZPqBPR2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPsBPR',
                     texname = '\\text{KZPqBPR2}')

KZPqBPR3 = Parameter(name = 'KZPqBPR3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPbBPR',
                     texname = '\\text{KZPqBPR3}')

KZPqTPL1 = Parameter(name = 'KZPqTPL1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPuTPL',
                     texname = '\\text{KZPqTPL1}')

KZPqTPL2 = Parameter(name = 'KZPqTPL2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPcTPL',
                     texname = '\\text{KZPqTPL2}')

KZPqTPL3 = Parameter(name = 'KZPqTPL3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPtTPL',
                     texname = '\\text{KZPqTPL3}')

KZPqTPR1 = Parameter(name = 'KZPqTPR1',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPuTPR',
                     texname = '\\text{KZPqTPR1}')

KZPqTPR2 = Parameter(name = 'KZPqTPR2',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPcTPR',
                     texname = '\\text{KZPqTPR2}')

KZPqTPR3 = Parameter(name = 'KZPqTPR3',
                     nature = 'internal',
                     type = 'real',
                     value = 'KZPtTPR',
                     texname = '\\text{KZPqTPR3}')

KZPuquqL1x1 = Parameter(name = 'KZPuquqL1x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPuuL',
                        texname = '\\text{KZPuquqL1x1}')

KZPuquqL1x2 = Parameter(name = 'KZPuquqL1x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPucL',
                        texname = '\\text{KZPuquqL1x2}')

KZPuquqL1x3 = Parameter(name = 'KZPuquqL1x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPutL',
                        texname = '\\text{KZPuquqL1x3}')

KZPuquqL2x1 = Parameter(name = 'KZPuquqL2x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPucL',
                        texname = '\\text{KZPuquqL2x1}')

KZPuquqL2x2 = Parameter(name = 'KZPuquqL2x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPccL',
                        texname = '\\text{KZPuquqL2x2}')

KZPuquqL2x3 = Parameter(name = 'KZPuquqL2x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPctL',
                        texname = '\\text{KZPuquqL2x3}')

KZPuquqL3x1 = Parameter(name = 'KZPuquqL3x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPutL',
                        texname = '\\text{KZPuquqL3x1}')

KZPuquqL3x2 = Parameter(name = 'KZPuquqL3x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPctL',
                        texname = '\\text{KZPuquqL3x2}')

KZPuquqL3x3 = Parameter(name = 'KZPuquqL3x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPttL',
                        texname = '\\text{KZPuquqL3x3}')

KZPuquqR1x1 = Parameter(name = 'KZPuquqR1x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPuuR',
                        texname = '\\text{KZPuquqR1x1}')

KZPuquqR1x2 = Parameter(name = 'KZPuquqR1x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPucR',
                        texname = '\\text{KZPuquqR1x2}')

KZPuquqR1x3 = Parameter(name = 'KZPuquqR1x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPutR',
                        texname = '\\text{KZPuquqR1x3}')

KZPuquqR2x1 = Parameter(name = 'KZPuquqR2x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPucR',
                        texname = '\\text{KZPuquqR2x1}')

KZPuquqR2x2 = Parameter(name = 'KZPuquqR2x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPccR',
                        texname = '\\text{KZPuquqR2x2}')

KZPuquqR2x3 = Parameter(name = 'KZPuquqR2x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPctR',
                        texname = '\\text{KZPuquqR2x3}')

KZPuquqR3x1 = Parameter(name = 'KZPuquqR3x1',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPutR',
                        texname = '\\text{KZPuquqR3x1}')

KZPuquqR3x2 = Parameter(name = 'KZPuquqR3x2',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPctR',
                        texname = '\\text{KZPuquqR3x2}')

KZPuquqR3x3 = Parameter(name = 'KZPuquqR3x3',
                        nature = 'internal',
                        type = 'real',
                        value = 'KZPttR',
                        texname = '\\text{KZPuquqR3x3}')

KZqBPL1 = Parameter(name = 'KZqBPL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZdBPL',
                    texname = '\\text{KZqBPL1}')

KZqBPL2 = Parameter(name = 'KZqBPL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZsBPL',
                    texname = '\\text{KZqBPL2}')

KZqBPL3 = Parameter(name = 'KZqBPL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZbBPL',
                    texname = '\\text{KZqBPL3}')

KZqBPR1 = Parameter(name = 'KZqBPR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZdBPR',
                    texname = '\\text{KZqBPR1}')

KZqBPR2 = Parameter(name = 'KZqBPR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZsBPR',
                    texname = '\\text{KZqBPR2}')

KZqBPR3 = Parameter(name = 'KZqBPR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZbBPR',
                    texname = '\\text{KZqBPR3}')

KZqTPL1 = Parameter(name = 'KZqTPL1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZuTPL',
                    texname = '\\text{KZqTPL1}')

KZqTPL2 = Parameter(name = 'KZqTPL2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZcTPL',
                    texname = '\\text{KZqTPL2}')

KZqTPL3 = Parameter(name = 'KZqTPL3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZtTPL',
                    texname = '\\text{KZqTPL3}')

KZqTPR1 = Parameter(name = 'KZqTPR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZuTPR',
                    texname = '\\text{KZqTPR1}')

KZqTPR2 = Parameter(name = 'KZqTPR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZcTPR',
                    texname = '\\text{KZqTPR2}')

KZqTPR3 = Parameter(name = 'KZqTPR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KZtTPR',
                    texname = '\\text{KZqTPR3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I1a33}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I4a33}')

