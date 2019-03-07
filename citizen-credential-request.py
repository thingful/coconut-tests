from zenroom import zenroom
import sys

with open('dddc-pilot-contracts/src/01-CITIZEN-credential-keygen.zencode') as file:
    keygen_script = file.read()

keypair, errs = zenroom.execute(keygen_script.encode())

with open('dddc-pilot-contracts/src/02-CITIZEN-credential-request.zencode') as file:
    credential_request_script = file.read()

request, errs = zenroom.execute(credential_request_script.encode(), keys=keypair)
print(request.decode())
