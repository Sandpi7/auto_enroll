from setuptools import setup, find_packages

setup(
    name="enrollment_updater",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "openpyxl>=3.1.0",
    ],
    author="",
    author_email="",
    description="Tool to update enrollment data between Excel files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/enrollment-updater",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "enrollment_updater=enrollment_updater:main",
        ],
    },
)
