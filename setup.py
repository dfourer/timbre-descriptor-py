 from setuptools import setup, find_packages

setup(
    name="timbretoolbox",
    version="0.1.0",
    author="Dominique Fourer",
    author_email="dominique@fourer.fr",
    description="Toolbox for automatic timbre classification and instrument recognition",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/dfourer/timbre-descriptor-py",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy"
        # autres dépendances
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
)
