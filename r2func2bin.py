from binaryninja import *
from subprocess import check_output as co
# https://github.com/deadjakk
# overly simple script to use the resolved functions output 
# from the following command: rabin2 -sr <binary_name> into binja
# just run from tools/plugins 
def setfunc(bv):
    funclist = []
    if 'bndb' in bv.file.filename:
        print("will not work if you open binja with database file\
                try again opening the actual binary instead of the\
                database file")
        return

    rco = co("/usr/bin/rabin2 -sr "+bv.file.filename,shell=True)
    for line in rco.split('\n'):
        if line:
            if "f " in line:
                lines = line.split(" ")
                n,a = lines[1],lines[3]
                funclist.append({'name':n,'addr':a})
    for func in funclist:
        name=func['name']
        addr=func['addr']
        hexaddr=int(func['addr'],16)

        try:
            bv.define_user_symbol(Symbol(SymbolType.FunctionSymbol, hexaddr, name))
            print("set",name,"@",addr)
        except:
            continue

PluginCommand.register("import r2 function names", "binja has failed you, try stealing from radare2", setfunc)
