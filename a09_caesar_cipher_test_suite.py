from a09_caesar_cipher import *
import sys

def testit(did_pass):
    """  Prints the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def CaesarCipher_test_suite():
    """
    A test suite for testing the encrypt and decrypt methods of the class

    NOTE:
    Typically, a test suite for a Class would be written into a second class entirely.
    However, to keep the complexity low, I chose to incorporate the test suite in a familiar way.
    In the future, we will explore how to properly write a test suite as a separate class.
    """

    # tests encrypting a normal string
    caesar = CaesarCipher()
    caesar.key = 3
    caesar.message = "A test string"

    testit(caesar.encrypt() == "D WHVW VWULQJ")


    # tests encrypting a string with punctuation
    caesar.key = 13
    caesar.message = "It's a so-so kind of day!"

    testit(caesar.encrypt() == "VG'F N FB-FB XVAQ BS QNL!")


    # tests decrypting a normal string
    caesar.key = 3
    caesar.cipher = "D WHVW VWULQJ"
    caesar.crypt_type = "decrypt"

    testit(caesar.decrypt() == "A TEST STRING")


    # tests decrypting a string with punctuation
    caesar.key = 6
    caesar.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"

    testit(caesar.decrypt() == "IT'S A SO-SO KIND OF DAY!")


    # what other tests should you add?

    #Test decrypting a string with a number
    caesar.key = 25
    caesar.cipher = "3 ZMSR"

    testit(caesar.decrypt() == "3 ANTS")

    #Tests decrypting a string with lowercase letters
    caesar.key = 2
    caesar.cipher = "jgnnq"   #Doesn't work with lower case letters

    testit(caesar.decrypt() == "hello")

   #Tests decrypting the same string as above but with capital letters, to make sure the only reason it failed above was because it doesn't work with lower case letters
    caesar.key = 2
    caesar.cipher = "JGNNQ"

    testit(caesar.decrypt() == "HELLO")

CaesarCipher_test_suite()
