from setuptools import setup

setup(
    name='basic_argparse',
    version='1.0',
    #url= insert github link?
    py_modules=['basic_argparse'],
    include_package_data=True,

    #Metadata
    description='A helper function for setting up an argparse parser.',
    long_description=(open('readme.rst').read() + '\n\n' +
                      open('CHANGELOG.rst').read()),
    license='http://opensource.org/licenses/MIT',
    author='Matthew Darling',
    author_email='matthewjdarling@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering'],
)