from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(name='checkout_code',
      version='0.5',
      description='Tool to checkout a specific commit to a unique location',
      long_description=README,
      long_description_content_type="text/markdown",
      url='https://github.com/kanedo/checkout_code',
      author='Gabriel Bretschner',
      author_email='bretschner@i6.informatik.rwth-aachen.de',
      license='MIT',
      packages=['checkout_code'],
	  install_requires=[
            'GitPython',
            'filelock',
            'python-dotenv'
      ],
	scripts=['bin/checkout_code'],
      zip_safe=False)

