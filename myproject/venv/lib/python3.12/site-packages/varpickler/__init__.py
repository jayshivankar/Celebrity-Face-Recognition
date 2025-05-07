import pickle
import codecs
from typing import Any

import dill


def encode_var(
    obj: Any,
    pickle_or_dill: str = "dill",
    base: str = "base64",
    str_encode: str | None = None,
) -> str | bytes:
    """
    Encode a Python object using either the 'pickle' or 'dill' library, and then encode the result using baseXX encoding.

    Parameters:
        obj (object): The object to be encoded.
        pickle_or_dill (str, optional): The library to be used for encoding.
            Valid options are 'pickle' or 'dill'. Defaults to 'dill'.
        base (str, optional): The base encoding to be used.
            Defaults to 'base64'.
        str_encode (str, optional): The string encoding to be used after baseXX encoding.
            If None, no additional string encoding is performed. Defaults to None.

    Returns:
        str or bytes: The encoded object. If 'str_encode' is None, a bytes object is returned.
            Otherwise, a string object is returned.

    Example:
        obj = np.array([23, 34, 4])
        >>> a1 = encode_var(obj, pickle_or_dill="dill", base="base64", str_encode=None)
        >>> print(a1)
        b'gAWVtgAAAAAAAACMCmRpbGwuX2RpbGyUjA1fY3JlYXRlX2FycmF5lJOUKIwVbnVtcHkuY29yZS5t\ndWx0aWFycmF5lIwMX3JlY29uc3RydWN0lJOUjAVudW1weZSMB25kYXJyYXmUk5RLAIWUQwFilIeU\nKEsBSwOFlGgGjAVkdHlwZZSTlIwCaTSUiYiHlFKUKEsDjAE8lE5OTkr/////Sv////9LAHSUYolD\nDBcAAAAiAAAABAAAAJR0lE50lFKULg==\n'

        >>> a2 = encode_var(obj, pickle_or_dill="dill", base="base64", str_encode="utf-8")
        >>> print(a2)
        'gAWVtgAAAAAAAACMCmRpbGwuX2RpbGyUjA1fY3JlYXRlX2FycmF5lJOUKIwVbnVtcHkuY29yZS5t
        dWx0aWFycmF5lIwMX3JlY29uc3RydWN0lJOUjAVudW1weZSMB25kYXJyYXmUk5RLAIWUQwFilIeU
        KEsBSwOFlGgGjAVkdHlwZZSTlIwCaTSUiYiHlFKUKEsDjAE8lE5OTkr/////Sv////9LAHSUYolD
        DBcAAAAiAAAABAAAAJR0lE50lFKULg=='
    """
    if pickle_or_dill == "pickle":
        pickler = pickle
    else:
        pickler = dill
    v = codecs.encode(pickler.dumps(obj, protocol=pickler.HIGHEST_PROTOCOL), base)
    if not str_encode:
        return v
    return v.decode(str_encode)


def decode_var(
    obj: Any,
    pickle_or_dill: str = "dill",
    base: str = "base64",
    str_decode: str | None = None,
) -> Any:
    """
    Decode a Python object that was encoded using either the 'pickle' or 'dill' library,
    and then decode the baseXX encoded result.

    Parameters:
        obj (str or bytes): The encoded object to be decoded.
        pickle_or_dill (str, optional): The library to be used for decoding.
            Valid options are 'pickle' or 'dill'. Defaults to 'dill'.
        base (str, optional): The base encoding used in the encoded object.
            Defaults to 'base64'.
        str_decode (str, optional): The string encoding used after baseXX encoding.
            If None, no additional string decoding is performed. Defaults to None.

    Returns:
        object: The decoded object.

    Example:
        import numpy as np
        obj = np.array([23, 34, 4])
        a1 = encode_var(obj, pickle_or_dill="dill", base="base64", str_encode=None)
        a2 = encode_var(obj, pickle_or_dill="dill", base="base64", str_encode="utf-8")
        a3 = decode_var(a1, pickle_or_dill="dill", base="base64", str_decode=None)
        print(a3)
        a4 = decode_var(a2, pickle_or_dill="dill", base="base64", str_decode="utf-8")
        print(a4)

        [23 34  4]
        [23 34  4]"""
    if pickle_or_dill == "pickle":
        pickler = pickle
    else:
        pickler = dill

    if not str_decode:
        return pickler.loads(codecs.decode(obj, base))
    return pickler.loads(codecs.decode(obj.encode(str_decode), base))
