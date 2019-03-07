from zenroom import zenroom
import json

print('01 - Creating citizen keypair')
with open('dddc-pilot-contracts/src/01-CITIZEN-credential-keygen.zencode') as file:
    keygen_script = file.read()

citizen_keypair, errs = zenroom.execute(keygen_script.encode())
print('Citizen\'s keypair:')
print('------------------------------')
print(json.dumps(json.loads(citizen_keypair.decode()), sort_keys=True, indent=4))
print('------------------------------')

print('\n02 - Creating citizen credential request')
with open('dddc-pilot-contracts/src/02-CITIZEN-credential-request.zencode') as file:
    credential_request_script = file.read()

print('Citizen\'s request:')
citizen_request, errs = zenroom.execute(credential_request_script.encode(), keys=citizen_keypair)

print('------------------------------')
print(json.dumps(json.loads(citizen_request.decode()), sort_keys=True, indent=4))
print('------------------------------')

print('\n03 - Creating issuer keypair')
with open('dddc-pilot-contracts/src/03-CREDENTIAL_ISSUER-keygen.zencode') as file:
    issuer_keygen_script = file.read()

issuer_keypair, errs = zenroom.execute(issuer_keygen_script.encode())
print('Issuer\'s keypair:')
print('------------------------------')
print(json.dumps(json.loads(issuer_keypair.decode()), sort_keys=True, indent=4))
print('------------------------------')


print('\n04 - Creating issuer public verification')
with open('dddc-pilot-contracts/src/04-CREDENTIAL_ISSUER-publish-verifier.zencode') as file:
    publish_verify_script = file.read()

issuer_public, errs = zenroom.execute(publish_verify_script.encode(), keys=issuer_keypair)
print('Issuer\'s public verification:')
print('------------------------------')
print(json.dumps(json.loads(issuer_public.decode()), sort_keys=True, indent=4))
print('------------------------------')

print('\n05 - Signing request for citizen')
with open('dddc-pilot-contracts/src/05-CREDENTIAL_ISSUER-credential-sign.zencode') as file:
    sign_script = file.read()

signed_credential, errs = zenroom.execute(sign_script.encode(), data=citizen_request, keys=issuer_keypair)
print('Signed credential:')
print('------------------------------')
print(json.dumps(json.loads(signed_credential.decode()), sort_keys=True, indent=4))
print('------------------------------')

print('\n06 - Citizen aggregate credential signature')
with open('dddc-pilot-contracts/src/06-CITIZEN-aggregate-credential-signature.zencode') as file:
    aggregate_signature_script = file.read()

aggregate_credential, errs = zenroom.execute(aggregate_signature_script.encode(), data=signed_credential, keys=citizen_keypair)
print('Aggregated credential:')
print('------------------------------')
print(json.dumps(json.loads(aggregate_credential.decode()), sort_keys=True, indent=4))
print('------------------------------')

print('\n07 - Create blind proof')
with open('dddc-pilot-contracts/src/07-CITIZEN-prove-credential.zencode') as file:
    blind_credential_script = file.read()

blind_credential, errs = zenroom.execute(blind_credential_script.encode(), data=issuer_public, keys=aggregate_credential)
print('Blind credential:')
print('------------------------------')
print(json.dumps(json.loads(blind_credential.decode()), sort_keys=True, indent=4))
print('------------------------------')

print('\n08 - Verify blind proof')
with open('dddc-pilot-contracts/src/08-VERIFIER-verify-credential.zencode') as file:
    verify_credential_script = file.read()

verify_response, errs = zenroom.execute(verify_credential_script.encode(), data=issuer_public, keys=blind_credential)
print('Verified credential:')
print('------------------------------')
print(verify_response.decode())
print('------------------------------')
