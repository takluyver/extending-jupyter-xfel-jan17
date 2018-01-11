import string

def shift_letter(c, shift):
    if c not in string.ascii_letters:
        return c
    
    z = 'z' if c in string.ascii_lowercase else 'Z'
    
    n = ord(c) + shift
    if n > ord(z):
        n -= 26
    return chr(n)

def caesar_cypher(line, cell):
    shift = 13
    if line:
        shift = int(line.strip())
    
    print(''.join(shift_letter(c, shift) for c in cell))

def load_ipython_extension(shell):
    shell.register_magic_function(caesar_cypher, magic_kind='cell')