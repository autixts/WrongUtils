import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WrongUtils", # Replace with your own username
    version="0.0.1",
    author="autixts",
    author_email="author@example.com",
    description="A package to make life easier with discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zeqxc/WrongUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["discord.py", "asyncio"]
)
