import hashlib

def createrequestdata(requestparams: dict) -> dict:
    """
    
    Parameters:
    -----------
    
    """

    privatekey = requestparams.pop('private_key')
    requesttype = requestparams.pop('request_type')

    signatureinputstring = F"{privatekey}|{requesttype}|Auth_GetUserToken|{requestparams['timestamp']}|{requestparams['nonce']}|"

    for key, value in sorted(requestparams.items()):
        signatureinputstring += F"&{key}={value}"

    sig = hashlib.sha1(signatureinputstring).hexdigest()

    requestparams["sig"] = sig

    return requestparams