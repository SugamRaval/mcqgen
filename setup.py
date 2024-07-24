from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='SugamRaval',
    author_email='sugam14jatin@gmail.com',
    install_requries = ['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)