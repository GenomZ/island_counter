"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pkg_resources
import pathlib

pkg_resources.require(['pip >= 20'])

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="island_counter",
    version="0.0.1",
    author="Krzysztof Buzar",
    classifiers=[
        "Developement Status :: 5 - Production/Stable",
        "Intended Audience :: Recruitment",
        "Topic :: Python Developer Recruitment Task",
        "License :: MIT License",
        "Programming Language :: Python :: 3 Only",
    ],
    keywords="reqruitment, developement",
    package_dir={"": "."},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    # entry_points={  # Optional
    #     "console_scripts": [
    #         "sample=sample:main",
    #     ],
    # },
)
