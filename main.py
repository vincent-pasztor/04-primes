
"""
On cherche les nombres premiers
"""


def isprime(p):
    """
    returne si "n" est prmier

    args: valeur entiere positive
    """
    premier = True
    if p == 1:
        return premier is False

    for i in range(2, p):
        if p % i == 0:
            return premier is False
    return premier is True

def main():
    """
    parcour n entre 1 et 99 

    appele la fonction isprime et envoie true si n est premier

    si n est premier, print le n en question
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()

if __name__ == "__main__":
    main()
