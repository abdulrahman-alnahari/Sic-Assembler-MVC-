from .abstract import Model, Controller
from tkinter import filedialog
from . import read_file

import os


class SICAssemblerModel(Model):
    def __init__(self):
        pass


class ChooseAssemblyFileModel(Model):

    def open_file_dialog(self):
        filename = filedialog.askopenfilename(
            title="Open Assembly File",
            initialdir='/',
            filetypes=(
                ('Assembly Files', '*.asm'),
            )
        )
        return filename

    def execute_pass_one_code(self, input_path):
        try:
            # Opening SIC program
            inp = open(input_path, "r")
            # For output of PASS ONE
            out = open("Intermediatefile.txt", "w")
            # SYMBOLTAB
            symtab = open("SymbolTab.txt", "w")
            sym = {}
            optab = {
                "ADD": "18",
                "AND": "40",
                "COMP": "28",
                "DIV": "24",
                "J": "3C",
                "JEQ": "30",
                "JGT": "34",
                "JLT": "38",
                "JSUB": "48",
                "LDA": "00",
                "LDCH": "50",
                "LDL": "08",
                "LDX": "04",
                "MUL": "20",
                "OR": "44",
                "RD": "D8",
                "RSUB": "4C",
                "STA": "0C",
                "STCH": "54",
                "STL": "14",
                "STSW": "E8",
                "STX": "10",
                "SUB": "1C",
                "TD": "E0",
                "TIX": "2C",
                "WD": "DC"}

            # READING FIRST LINE
            first = inp.readline()
            out.write("---\t")
            out.write("".join(first))
            newl = first.strip().split()
            # OUTPUT into Intermediate file
            LOCCTR = newl[2]
            start = LOCCTR

            for i in inp.readlines():
                n = i.strip().split()

                if n[0] != '.':
                    out.write(hex(int(LOCCTR, 16)))
                    out.write("".join(i))
                    if n[0] != "-":
                        symtab.write(n[0] + " " + hex(int(LOCCTR, 16)) + "\n")
                        sym[n[0]] = str(hex(int(LOCCTR, 16)))
                    if n[1] in optab.keys() or n[1] == "WORD":
                        LOCCTR = str(hex(int(LOCCTR, 16) + (3)))
                    elif n[1] == "RESW":
                        temp = int(n[2], 16)
                        LOCCTR = str(hex(int(LOCCTR, 16) + (temp) * 3))
                    elif n[1] == "RESB":
                        LOCCTR = str(hex(int(LOCCTR, 16) + int(n[2])))
                    elif n[1] == "BYTE":
                        if n[2][0] == "X":
                            LOCCTR = str(hex(int(LOCCTR, 16) + (len(n[2]) - 3) % 2))
                        elif n[2][0] == "C":
                            LOCCTR = str(hex(int(LOCCTR, 16) + (len(n[2]) - 3)))

            inp.close()
            out.close()
            symtab.close()

            return {'sym': sym, 'optab': optab, 'LOCCTR': LOCCTR, 'start': start}

        except Exception as error:
            pass


class ShowGeneratedFilesModel(Model):
    def get_intermediate_data(self):
        return read_file('./Intermediatefile.txt', "Intermediate File Not Found")

    def get_symbol_tab_data(self):
        return read_file('./SymbolTab.txt', "Symbol Tab File Not Found")


class ShowObjectProgramFileModel(Model):
    def execute_pass_two_code(self, _sym, _optab, _LOCCTR, _start):
        try:
            sym, optab, LOCCTR, start = _sym, _optab, _LOCCTR, _start

            length = hex(int(LOCCTR, 16) - int(start, 16))

            objpgm = open("ObjectProgram.txt", "w")
            inter = open("Intermediatefile.txt", "r")
            symtab = open("SymbolTab.txt", "r")
            l = []

            addrlist = []
            for i in inter.readlines():
                ls = i.strip().split()
                add = ls[0][2:]
                if add != "-":
                    addrlist.append(add)
                label = ls[1]
                opcode = ls[2]
                if len(ls) == 4:
                    operand = ls[3]
                if ls[2] == "START":
                    objpgm.write("H^" + label + "^00" + start + "^00" + length[2:] + "\n")
                elif ls[2] == "END":
                    tempstr = "\nE^00" + start
                else:
                    if ls[2] in optab.keys():

                        # op = str(bin(int(optab[ls[2]],16)))
                        op = optab[ls[2]]
                        if ls[2] == "RSUB":
                            op += "0000"
                        elif operand in sym.keys():
                            op += sym[operand][2:]
                        l.append(op)
                    elif ls[2] == "WORD":
                        op = hex(int(operand))
                        op1 = str(op)
                        op1 = op1[2:]
                        if len(op1) < 6:
                            for i in range(6 - len(op1)):
                                op1 = "0" + op1

                        l.append(op1)
                    elif ls[2] == "BYTE":
                        temp = operand[2:len(operand) - 1]
                        if operand.find("X"):
                            l.append(temp)
                        elif operand.find("X"):
                            _str = null
                            for i in temp:
                                hexcode = hex(ord(i))
                                tmp = str(hexcode)
                                _str += tmp[2:]
                            l.append(_str)
                    else:
                        l.append("-")

            i = 0

            while i < len(l):
                if i == 0:
                    STRT = addrlist[1]
                else:
                    STRT = addrlist[i]
                cnt = 0

                if i < len(l) and l[i] != "-":
                    objpgm.write("\nT^00" + STRT + "^")
                    last_pas = objpgm.tell()
                    objpgm.write("  ^")
                while i < len(l) and l[i] != "-" and cnt < 10:
                    objpgm.write(l[i])
                    cnt += 1
                    i += 1
                objpgm.seek(last_pas)
                tempaddr = str(hex(int(addrlist[i], 16) - int(STRT, 16)))
                straddr = tempaddr[2:4]
                objpgm.write(straddr)
                objpgm.seek(0, 2)

                i += 1
            objpgm.write(tempstr)
            objpgm.close()
            inter.close()
            symtab.close()
            return True

        except:
            return False

    def get_object_code_data(self):
        return read_file('./ObjectProgram.txt', 'Object File Was Not Found')

