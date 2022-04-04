from distutils.core import setup

with open('requirements.txt', 'r', encoding='utf-8') as f:
    install_requires = f.readlines()

setup(
    name='rodri-sorter',
    version='1.0',
    description='Python imports sorter written for Comparaencasa utilities',
    author='Martin Nieva',
    author_email='martinjafactor@gmail.com',
    packages=['rodri_sorter'],
    install_requires=install_requires
)
