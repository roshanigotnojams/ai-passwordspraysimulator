FAKE_USERS = {
    "alice": "Welcome123",
    "bob": "Summer2026",
    "charlie": "Password123",
    "david": "Cyber2026",
    "eve": "Python123"
}


def authenticate(username, password):
    """
    Authenticate against the local fake-user database.
    This is completely synthetic and does not contact
    any external service.
    """

    if username not in FAKE_USERS:
        return False

    return FAKE_USERS[username] == password