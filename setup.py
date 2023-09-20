from setuptools import setup

setup(
    name="common_fastapi",
    description="My customized library for using FastAPI framework",
    version="v1.0.0",
    author="Alexander Andryukov",
    author_email='andryukov@gmail.com',
    install_requires=[
        'fastapi==0.103.0',
        'uvicorn==0.23.2',
        # Fork for fastapi-utils bcz not compatible with SQLAlchemy higher than 1.4.47
        'fastapi-utils @ git+https://github.com/flameai/fastapi-utils.git@aandryukov_fork#fastapi_utils'
    ]
)
