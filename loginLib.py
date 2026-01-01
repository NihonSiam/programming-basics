import hashlib

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    # TODO: Implement password hashing
    pass


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    # TODO: Count existing users to assign a new ID
    # TODO: Hash the password
    # TODO: Write the new user to the file
    pass


def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    # TODO: Hash the input password
    # TODO: Read the file and compare credentials
    pass


def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    # TODO: Read the file and return the matching profile
    pass


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    # TODO: Read all lines, update the password for the matching user
    # TODO: Write the updated lines back to the file
    pass
