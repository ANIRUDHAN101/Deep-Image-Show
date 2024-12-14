from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='deepImageShow',
    version="0.0.10",
    author='Anirudhan K S',
    author_email='anirudhan0ks@gmail.com',
    description='A flexible toolkit for tensor processing and visualization',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ANIRUDHAN101/Deep-Image-Show.git',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'einops',
        # 'torch',  # Optional: specify version if needed
        # 'tensorflow',  # Optional: specify version if needed
        # 'jax',  # Optional: specify version if needed
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
    keywords='tensor processing visualization deep-learning',
    project_urls={
        'Bug Reports': 'https://github.com/ANIRUDHAN101/Deep-Image-Show.git/issues',
        'Source': 'https://github.com/ANIRUDHAN101/Deep-Image-Show.git',
    },
)
