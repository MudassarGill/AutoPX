from setuptools import setup, find_packages

setup(
    name="autopx",
    version="0.1.0",
    description="Automatic Preprocessing with eXplainability",
    author="AutoPX Team",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "pyyaml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
