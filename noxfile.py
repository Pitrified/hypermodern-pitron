import nox


@nox.session(python=["3.9", "3.8"])
def tests(session):
    # to pass additional options to pytest
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
