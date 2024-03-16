# type: ignore
from fabric import task


@task
def doc(context):
    context.run("./env/bin/sphinx-build " "docs " "docs/_build/html")


@task
def publish(context):
    context.run("./env/bin/python setup.py sdist bdist_wheel")
    context.run("./env/bin/twine upload dist/*")
    context.run("rm -rf dist")


@task
def develop(context):
    context.run(
        "[ -d env ] || python3 -m venv env", replace_env=False, pty=True
    )
    context.run(
        "./env/bin/pip install -e .[dev,test,doc]", replace_env=False, pty=True
    )
