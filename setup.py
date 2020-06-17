from distutils.core import setup

setup(name='StorageVet',
      version='2.1.0.2',
      description='model energy storage',
      packages=['storage_vet', 'storage_vet.Technology', 'storage_vet.ValueStreams', 'storage_vet.Tariff'],
      install_requires=[
          'cvxopt',
          'cvxpy',
          'ecos',
          'matplotlib',
          'mkl',
          'numpy',
          'pandas',
          'prettytable',
          'pytz',
          'rainflow',
          'requests',
          'scipy',
          'scs',
      ])
