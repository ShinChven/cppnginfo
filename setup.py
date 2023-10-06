from setuptools import setup, find_packages

setup(
    name="cppnginfo",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'cppnginfo = cppnginfo.main:main',
        ],
    },
    author="ShinChven",
    author_email="shinchven@gmail.com",
    description="A CLI tool to copy Stable Diffusion Web UI's pnginfo metadata from a source to a target.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/ShinChven/cppnginfo",
)
