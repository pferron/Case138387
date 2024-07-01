from setuptools import setup, find_packages

setup(
    name='leadcast-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'esri-arcgis-rest',
        'arcgis',
    ],
    entry_points={
        'console_scripts': [
            # If your SDK contains executable scripts
        ],
    },
    author_email='support@trinnex.io',
    description='A brief description of your SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/trinnex/leadcast-sdk',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='Proprietary',
    license_file='LICENSE.txt',
    keywords='SDK leadcast-sdk',
    include_package_data=True,
    zip_safe=False,
)
