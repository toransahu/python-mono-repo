from setuptools import find_packages, setup


# get the dependencies and installs
with open("requirements.txt", encoding="utf-8") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)

setup(
    name="package1",
    version="0.1",
    packages=find_packages(include=["package1"]),
    install_requires=requires,
    extras_require={},
)
