from setuptools import setup, find_packages

setup(
    name="casino",
    version="0.1.0",
    description="A casino game package with dice and scoring.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],  # Add runtime dependencies here if needed
    python_requires=">=3.8",
)
