from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    
    description='A simple math quiz game.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vivitar39/dsss_hw2',
    license='Apache License 2.0',
)
