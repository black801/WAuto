from setuptools import setup, find_packages

setup(
    name="waauto",
    version="0.1.0",
    author="Samir Essam",
    author_email="your-email@example.com",
    description="WAuto: WhatsApp automation via code login (no QR)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/WAuto",
    packages=find_packages(),
    install_requires=[
        "flask",
        "requests",
        "playwright",
        "rich",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)