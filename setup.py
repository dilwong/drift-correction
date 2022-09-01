import setuptools

if __name__ == "__main__":

    with open('requirements.txt', 'r') as f:
        requirements = f.readlines()
        requirements = [line.strip() for line in requirements if line.strip()]

    setuptools.setup(name = 'drift-correction',
    version = '1.0.0',
    author = 'Dillon Wong and Ryan Lee',
    author_email = '',
    description = 'Correct drift in STM images',
    url = '',
    install_requires = requirements,
    packages=['drift-correction'],
    )