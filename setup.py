from setuptools import setup, find_packages

setup(
    name="common_fastapi",
    description="My customized library for using FastAPI framework",
    version="v1.0.0",
    author="Alexander Andryukov",
    author_email='andryukov@gmail.com',
    install_requires=[
        'fastapi==0.103.0',
        'uvicorn==0.23.2',
        'fastapi-utils==0.2.1'
    ]
)