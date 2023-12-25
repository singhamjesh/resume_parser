from fastapi import FastAPI, Depends, HTTPException
from fastapi_session import (
    SessionManager,
    Session,
    Depends as SessionDepends,
    IN_SESSION,
)


# Secret key used for session encryption
SECRET_KEY = "your_secret_key"

# Session manager instance
manager = SessionManager(SECRET_KEY)

# Dependency to get the current session


def get_session(session: Session = SessionDepends(manager.session)):
    return session
