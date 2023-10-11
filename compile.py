import pickle

code = r'''
v = "hello worl"
print(v + "d")
'''

code = compile(code, "", "exec")

code = (
code.co_code,
code.co_consts,
code.co_names,
)

print(pickle.dumps(code))