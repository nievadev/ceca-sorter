from distutils.core import setup

setup(
    name='rodri-sorter',
    version='1.0',
    description='Python imports sorter written for Comparaencasa utilities',
    author='Martin Nieva',
    author_email='martinjafactor@gmail.com',
    packages=['rodri_sorter'],
    install_requires=('click', ),
    entry_points={
        'console_scripts': ['rodri-sorter=rodri_sorter.__main__:_main']
    }
)
