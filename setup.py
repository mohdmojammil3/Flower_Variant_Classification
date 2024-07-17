from setuptools import find_packages, setup

def get_requirements(file_path):
    """
    This function returns a list of requirements from a requirements file.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    return requirements

setup(
    name='Flower Variant Prediction',
    version='0.0.0.1',
    author='Md Mojammil',
    author_email='mohdmojammil3@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
