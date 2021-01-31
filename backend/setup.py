import setuptools

setuptools.setup(
    name="apartment",
    description="",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=["flask", "flask_cors", "marshmallow", "redis", "celery[redis]"],
)
