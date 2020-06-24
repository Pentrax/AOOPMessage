from setuptools import setup, find_packages

setup(
    name='AOOPMessages',
    version='0.1',
    packages=find_packages(),
    url='https://localhost:PORT',
    # license='GPU',
    author='Pablo Pentreath',
    author_email='MyEmail@email.com',
    description='Ejemplo FLASK',
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
