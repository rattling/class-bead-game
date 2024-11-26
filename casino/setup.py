from setuptools import setup, find_packages

setup(
    name="casino",
    version="0.1",
    package_dir={"": "src"},  # Tell setuptools packages are under src/
    packages=find_packages(where="src"),  # Look for packages under src/
    install_requires=[
        # your dependencies here
    ],
)
