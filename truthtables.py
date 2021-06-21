# -*- coding: utf-8 -*-

'''
Intrucciones:
Variables a utilizar -> p y q
Use and en vez de ^
Use or en vez de v
Use not en vez de ~
'''
while True:
    expresion = input("ingresa expresion: ")
    if not expresion:
        print("Thaks...")
        break
    if('p' in expresion and 'q' in expresion):
        print( "p      q      %s"  % expresion)
        longitud = len( "p      q      %s"  % expresion)
        print( longitud*"=")
        for p in 1,0:
            for q in 1,0:
                print( "%-6s %-6s %-6s" % (p, q, eval(expresion)))
    if ('q' not in expresion):
        print( "p      %s"  % expresion)
        longitud = len(( "p      %s"  % expresion))
        print(longitud*"=")
        for p in 1,0:
            print( "%-6s %-6s" % (p, eval(expresion)))
    if ('p' not in expresion):
        print( "q      %s"  % expresion)
        longitud = len(( "q      %s"  % expresion))
        print(longitud*"=")
        for q in 1,0:
            print( "%-6s %-6s" % (q, eval(expresion)))
