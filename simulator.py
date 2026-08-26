import time
from datetime import datetime

from auth_server import authenticate, FAKE_USERS


PASSWORDS = [
    "Welcome123",
    "Summer2026",
    "Password123",
    "Cyber2026",
    "Python123"
]


def password_spray(delay=1.0):

    logs = []

    for round_number, password in enumerate(
        PASSWORDS,
        start=1
    ):

        print()
        print(f"--- Round {round_number} ---")
        print(f"Password: {password}")

        for username in FAKE_USERS:

            result = authenticate(
                username,
                password
            )

            status = (
                "SUCCESS"
                if result
                else "FAILED"
            )

            log = {
                "timestamp":
                    datetime.now().strftime(
                        "%H:%M:%S"
                    ),

                "username":
                    username,

                "result":
                    status,

                "round":
                    round_number
            }

            logs.append(log)

            print(
                f"{log['timestamp']} | "
                f"{username} | "
                f"{status}"
            )

            time.sleep(delay)

    return logs