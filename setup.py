from setuptools import find_packages, setup

setup(
    name="Simulator",
    version="0.0.10",
    description="An Epidemic Simulator",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://github.com/arsh73552/Epidemic-Simulator",
    author="Arshdeep Singh, Mandeep Mahra",
    author_email="arsh.edu2002@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["manimgl>=1.6.1", "numpy>=1.23.5"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.8",
)
