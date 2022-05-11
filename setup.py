import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytabchen",
    version="0.0.0",
    author="TabChen",
    author_email="2808581543@qq.com",
    description="Finder papers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meta-tabchen/py-tabchen",
    project_urls={
        "Bug Tracker": "https://github.com/meta-tabchen/py-tabchen/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.1",
    include_package_data=True,
    install_requires=['numpy','pandas','tqdm'],
)