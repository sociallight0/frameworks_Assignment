from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cord19-analysis",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive analysis of the CORD-19 research dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/CORD-19-Analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="covid-19, research, data-analysis, streamlit, visualization",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/CORD-19-Analysis/issues",
        "Source": "https://github.com/yourusername/CORD-19-Analysis",
        "Documentation": "https://github.com/yourusername/CORD-19-Analysis/blob/main/README.md",
    },
)
