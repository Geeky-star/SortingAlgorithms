import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

    
setuptools.setup(
    name = "SortingAlgos",
    version = "0.0.1",
    author = "Nimrat Kaur",
    author_email="nimratkaur540@gmail.com",
    description = "Sorting algorithms for sorting",
    long_description = "Sorting techniques for optimizing the sorting and making the use of sorting algorithms easier.",
    long_description_content_type = "text/markdown",
    url = "https://github.com/Geeky-star/SortingAlgorithms",
    license= "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        ],
    packages = ["SortingAlgos"],
    include_package_data=True,
    
    python_requires = '>=3.0',
    )