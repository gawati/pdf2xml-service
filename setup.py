from setuptools import setup

setup(
	name='pdf2xml',
	version='1.0.0',
	description='Extracts text from PDF',
	packages=['pdf2xml'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'Flask==1.0.2'
	],
)