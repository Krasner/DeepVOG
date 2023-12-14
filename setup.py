import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepvog",
    version="1.1.4",
    author="Yuk-Hoi Yiu et al.",
    author_email="h.yiu@campus.lmu.de",
    description="Deep VOG for gaze estimation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pydsgz/DeepVOG",
    license="GNU General Public License v3.0",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    package_data={
        "deepvog": ["model/*.py", "model/*.h5"],
        #'model_weights':['model/*.h5'],
    },
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "scikit-image",
        "tensorflow>=2.13.0",
        "opencv-python",
        "matplotlib",
        "git+https://github.com/scikit-video/scikit-video.git@master",
        "tqdm",
    ],
)
