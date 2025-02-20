from socketPot import socketPot, globalMemory

gv = globalMemory.GlobalVariableT24
# gv = globalMemory.GlobalVariableT26
dc = globalMemory.GlobalDataContainer

def readNANDYB1(pot):
    # PC MODE
    pot.writeTransferMono(cmd = gv.CMD_SET_PCMODE)
    # Bridge Reset
    pot.writeTransferMono(cmd = gv.CMD_YB_DDR_BRIDGE_RESET)
    # POT command
    pot.readTransferBurst(cmd = gv.CMD_RD_NAND_YB1, dataType = 'comp')
    # PC MODE clear
    pot.writeTransferMono(cmd = gv.CMD_CLR_PCMODE)


def writeNANDYB1(pot):
    # PC MODE
    pot.writeTransferMono(cmd = gv.CMD_SET_PCMODE)
    # Erase
    pot.writeTransferMono(cmd = gv.CMD_ER_NAND_YB1)
    # Bridge Reset
    pot.writeTransferMono(cmd = gv.CMD_YB_DDR_BRIDGE_RESET)
    # POT command
    pot.writeTransferBurst(cmd = gv.CMD_WR_NAND_YB1, dataType = 'comp')
    # PC MODE clear
    pot.writeTransferMono(cmd = gv.CMD_CLR_PCMODE)


def eraseNANDYB1(pot):
    # PC MODE
    pot.writeTransferMono(cmd = gv.CMD_SET_PCMODE)
    # POT command
    pot.writeTransferMono(cmd = gv.CMD_ER_NAND_YB1)
    # PC MODE clear
    pot.writeTransferMono(cmd = gv.CMD_CLR_PCMODE)


def readNANDLGDVparam(pot):
    # PC MODE
    pot.writeTransferMono(cmd = gv.CMD_SET_PCMODE)
    # POT command
    if not gv.ASIC_MODEL in ['T26']:
        pot.readTransferBurst(cmd = gv.CMD_RD_NAND_LGD_VPARAM, dataType = 'setting')
    else:
        pot.readTransferLine(cmd = gv.CMD_RD_NAND_LGD_VPARAM, lineNumber = 0, dataType = 'setting')
    # PC MODE clear
    pot.writeTransferMono(cmd = gv.CMD_CLR_PCMODE)


def writeNANDLGDVparam(pot):
    # PC MODE
    pot.writeTransferMono(cmd = gv.CMD_SET_PCMODE)
    # POT command
    pot.writeTransferMono(cmd = gv.CMD_ER_NAND_LGD_VPARAM)
    # POT command
    if not gv.ASIC_MODEL in ['T26']:
        pot.writeTransferBurst(cmd = gv.CMD_WR_NAND_LGD_VPARAM, dataType = 'setting')
    else:
        pot.writeTransferLine(cmd = gv.CMD_WR_NAND_LGD_VPARAM, lineNumber = 0, dataType = 'setting')
    # PC MODE clear
    pot.writeTransferMono(cmd = gv.CMD_CLR_PCMODE)


def eraseNANDLGDVparam(pot):
    # PC MODE
    pot.writeTransferMono(cmd = gv.CMD_SET_PCMODE)
    # POT command
    pot.writeTransferMono(cmd = gv.CMD_ER_NAND_LGD_VPARAM)
    # PC MODE clear
    pot.writeTransferMono(cmd = gv.CMD_CLR_PCMODE)


if __name__ == '__main__':
    pot = socketPot.PotConnection()
    pot.connect()
    # test1 : NAND YB1 read
    #readNANDYB1(pot)
    #print(f"dc.rPhiContainer[0][0]: {dc.rPhiContainer[0][0]}")
    #print(f"dc.rAlphaContainer[0][0]: {dc.rAlphaContainer[0][0]}")

    # test2 : NAND Vparam read
    readNANDLGDVparam(pot)

    
    print(f"dc.lut[0][0]: {dc.lut[0][0]}") # T24
    # print(f"dc.vParam[0]: {dc.vParam[0]}") # T26
