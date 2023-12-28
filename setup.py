# Modified source for /PyHumor-v1.0.0/setup.py

import setuptools

setuptools.setup(
  name='pyhumor',
  version='1.0.0',
  description='A Python library for generating humorous python jokes.',
  long_description="A Python library for generating humorous python jokes",
  author='Srijal Dutta',
  author_email='srijaldutta.official+pyhumorv1.0.0@gmail.com',
  license='CC BY 4.0',
  url='https://github.com/SrijalCodes/PyHumor',
  
  packages=[],
  include_package_data=True,

  python_requires='>=3.6',
  classifiers=[
      'Development Status :: 1 - Planning',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Operating System :: OS Independent',
  ],
  
  # Specifying project dependencies
  install_requires=[],
  
  project_urls={
      'Bug Reports': 'https://github.com/SrijalCodes/PyHumor/issues',
  }
)
