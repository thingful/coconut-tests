from zenroom import zenroom

with open('dddc-pilot-contracts/src/01-CITIZEN-credential-keygen.zencode') as file:
    script = file.read()

result, errs = zenroom.execute(script.encode())
print(result.decode())
