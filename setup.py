from setuptools import setup, find_packages

setup(
    name="example_library",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example Python library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/chrismcmacken/example_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
