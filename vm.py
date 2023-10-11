import pickle

code = b'\x80\x04\x95<\x00\x00\x00\x00\x00\x00\x00C\x14d\x00Z\x00e\x01e\x00d\x01\x17\x00\x83\x01\x01\x00d\x02S\x00\x94\x8c\nhello worl\x94\x8c\x01d\x94N\x87\x94\x8c\x01v\x94\x8c\x05print\x94\x86\x94\x87\x94.'

class ops:
 LOAD_CONST    = 100
 LOAD_NAME     = 101
 BINARY_ADD    = 23
 CALL_FUNCTION = 131
 POP_TOP       = 1
 STORE_NAME    = 90

def vmCall(code, consts, names):
 Stk  = []
 push = Stk.append
 pop  = Stk.pop
 ecx  = 0
 varp = vars(__builtins__)

 while ecx < len(code):
  opc = code[ecx]
  opa = code[ecx +1]

  match opc:
   case ops.LOAD_CONST:
    kst = consts[opa]
    push(kst)

   case ops.LOAD_NAME:
    name = names[opa]
    name = varp[name]
    push(name)

   case ops.BINARY_ADD:
    b = pop()
    a = pop()
    push(a + b)

   case ops.CALL_FUNCTION:
    stdcargs = []
    for cx in range(opa):
     stdcargs.insert(0, pop())

    function = pop()
    push(function(*stdcargs))
  
   case ops.POP_TOP:
    pop()

   case ops.STORE_NAME:
    v = pop()
    name = names[opa]
    varp[name] = v

  ecx += 2


vmCall(*pickle.loads(code))