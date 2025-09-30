class LoginException(Exception):
    """Exceptions pour erreurs dans le login qui ne doit contenir que des lettres minuscules."""
    pass

class PasswordException(Exception):
    """Exceptions pour erreurs dans le mot de passe qui doit ne doit contenir que des chiffres. """
    pass

def input_login():
    try:
        login = input("Entrez votre login (lettres minuscules uniquement) : ")
        if not login.islower() or not login.isalpha():
            raise LoginException("Le login doit contenir uniquement des lettres minuscules.")
    except Exception as ex:
        print("Le login propose a leve une exception:")
        print(ex)
        return -1
    else:
        print("Login valide et enregistre")
        return login

def input_password():
    try:
        password = input("Entrez votre mot de passe (chiffres uniquement) : ")
        if not password.isdigit():
            raise PasswordException("Le mot de passe doit contenir uniquement des chiffres.")
    except Exception as ex:
        print("Le mot de passe propose a leve une exception:")
        print(ex)
        return -1
    else:
        print("Mot de passe valide et enregistre")
        return password


if __name__ == "__main__":
    login = -1
    while login == -1:
        login = input_login()

    password = -1
    while password == -1:
        password = input_password()



