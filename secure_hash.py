import hashlib

python_program = '''for i in range(10)
print(i)
'''
print(python_program)

original_hash = hashlib.sha256(python_program.encode('utf-8'))
print("SHA256:{}".format(original_hash.hexdigest()))
print(len(original_hash.digest()))

python_program = "print('Code Changed!!')"
print(python_program)
new_hash = hashlib.sha256(python_program.encode('utf-8'))
print()
print("SHA256 : {}".format(new_hash.hexdigest()))
