from setuptools import setup, find_packages

setup(name='keras_sequential_ascii',
      version='0.1.1',
      install_requires=['keras'],
      author="Piotr Migdał",
      author_email="pmigdal@gmail.com",
      url="https://github.com/stared/keras-sequential-ascii",
    #   download_url='https://github.com/stared/keras-sequential-ascii/tarball/v0.0.1',
      description="ASCII summary for simple sequential models in Keras",
      keywords=['keras', 'ascii'],
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Jupyter',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Visualization',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      packages=find_packages())
