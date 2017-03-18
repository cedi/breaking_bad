import keygen
import crypt
import input_parser


print("Welcome to Simple-RSA")

while True:
    print("\n*** Main Menue ***")
    print("(1) - Generate new keypairs")
    print("(2) - Encrypt message")
    print("(3) - Decrypt message")
    print("(0) - Exit")

    try:
        userIn = input("\nPlease choose operation: ")
        userIn = int(userIn)

    except KeyboardInterrupt:
        print("")
        break

    except ValueError:
        print("Please enter only Numbers between 0 and 4")
        continue

    if userIn == 1:
        keys = keygen.keygen()

        print("*** Keypairs ***")
        print("- Private Key:   (N={},d={})".format(keys.private.RSA,
                                                    keys.private.exponent))
        print("- Public Key:    (N={},e={})".format(keys.public.RSA,
                                                    keys.public.exponent))

    elif userIn == 2 or userIn == 3:
        question = str()
        if(userIn == 2):
            question = "Please enter public key: "
        else:
            question = "Please enter private key: "

        Key = RSAInputParser.InputParser(input(question))

        if userIn == 2:
            message = input("Please enter the plaintext message: ")
            encrypted = Crypt.encrypt(Key.N, Key.exp, message)
            print("Encrypted: {}".format(encrypted))
        else:
            message = input("Please enter the encrypted message: ")
            decrypted = Crypt.decrypt(Key.N, Key.exp, message)
            print("Dcrypted: {}".format(decrypted))

    elif userIn == 0:
        break

print("Bye Bye")
