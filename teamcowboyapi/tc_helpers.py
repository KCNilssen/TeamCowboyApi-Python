import hashlib

def createrequestdata(requestparams: dict) -> dict:
    """
    
    Parameters:
    -----------
    
    """

    privatekey = requestparams.pop('private_key')
    requesttype = requestparams.pop('request_type')

    signatureinputstring = F"{privatekey}|{requesttype}|{requestparams['method']}|{requestparams['timestamp']}|{requestparams['nonce']}|" 

    for key, value in sorted(requestparams.items()):
        signatureinputstring += F"{key.lower()}={value.lower() if type(value) == str else value}&"

    sig = hashlib.sha1(signatureinputstring[:-1].encode('UTF-8')).hexdigest()

    # requestparams.pop('request_type')

    requestparams["sig"] = sig

    return requestparams