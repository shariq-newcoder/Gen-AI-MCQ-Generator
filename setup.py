from setuptools import find_packages, setup

setup(
    name="MCQgenrator",
    version="0.0.1",
    author="Shariq Siraj",
    author_email="mshariq1718@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages(),
)
