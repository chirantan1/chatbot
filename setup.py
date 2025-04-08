from setuptools import find_packages, setup

setup(
    name='chatbot',
    version='0.0.1',
    author='Chirantan Jana',
    author_email='chirantanjana43@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'langchain',
        'langchain-pinecone',
        'langchain-experimental',
        'langchain-community',
        'pinecone-client',
        'python-dotenv',
        'pypdf',
        'sentence-transformers',    
    ]
)