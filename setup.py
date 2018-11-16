from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='eclipseChallenge',
    version='0.1.0',
    description='Direction Controller',
    long_description=readme,
    author='Sajj Farahani',
    author_email='sajjfarahni@outlook.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'directioncontroller=directioncontroller.sender:main',
        ]
    }

)
