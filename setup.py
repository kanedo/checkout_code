from setuptools import setup

setup(name='checkout_code',
      version='0.2',
      description='Tool to checkout a specific commit to a unique location',
      url='',
      author='Gabriel Bretschner',
      author_email='bretschner@i6.informatik.rwth-aachen.de',
      license='MIT',
      packages=['checkout_code'],
	  install_requires=[
      	'GitPython',
        'filelock'
      ],
	  scripts=['bin/checkout_code'],
      zip_safe=False)

