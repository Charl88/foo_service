from nameko.rpc import rpc
from dahuffman import load_shakespeare
import base64


class FooService:
    name = "foo"

    @rpc
    def square_odd(self, numbers: list) -> list:
        """Squares all the odd numbers in a given list of integers.

        If a float is included in the list of integers, then the function will round the float
        to the nearest integer.

        Parameters:
            numbers (list): A list of integers

        Returns:
            list: A list of integers
        """
        return [round(num)**2 if round(num) % 2 != 0 else round(num) for num in numbers]

    @rpc
    def encode(self, strings: list) -> dict:
        """Compresses a list of strings by applying Huffman and base64 encoding on each string.

        Parameters:
            strings (list): A list of strings we wish to compress

        Returns
            dict: A dictionary of the compressed strings, where the keys are the original string
                  and the values are the encoded strings.
        """
        # we use the precompiled huffman table provided by the dahuffman library
        codec = load_shakespeare()
        encoded = {}
        for string in strings:
            huff_bytes = codec.encode(string)
            # we need to encode the binary output to a base64 string so that
            # the service can serialize it with json
            b64_bytes = base64.b64encode(huff_bytes)
            encoded[string] = b64_bytes.decode()
        return encoded


    @rpc
    def decode(self, string: str) -> str:
        """Decodes a given Huffman and base64 encoded string.

        Parameters:
            string (str): A string we wish to decode

        Returns
            str: The decoded string
        """
        codec = load_shakespeare()
        b64_bytes = string.encode()
        string_bytes = base64.b64decode(b64_bytes)
        return codec.decode(string_bytes)