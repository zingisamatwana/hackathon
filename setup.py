from setuptools import setup, find_packages

setup(
    name='hackathon',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<zingm>/<hackathon>',
    author='<zingisa>',
    author_email='<Your Email>'
)
