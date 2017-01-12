from setuptools import setup, find_packages

setup(name='keras_sequential_ascii',
      version='0.0.1',
      install_requires=['keras'],
      author="Piotr Migdal",
      author_email="pmigdal@gmail.com",
      url="https://github.com/stared/keras-sequential-ascii",
    #   download_url='https://github.com/stared/keras-sequential-ascii/tarball/v0.0.1',
      description="ASCII summary for simple sequential models in Keras",
      keywords=['keras', 'ascii'],
      license='MIT',
      classifiers=[
          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      packages=find_packages())
