# easedate

## Description
A python package for easy date use and conversions.

Generate build

python setup.py sdist bdist_wheel

Upload build TEST

python -m twine upload --repository testpypi dist/* (TEST)

username = __token__
  password = pypi-AgENdGVzdC5weXBpLm9yZwIkMzliY2QzYTEtZjQ0Ny00MTViLTg3N2EtNzBkMGQ1ODA2NTljAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDko3zmYOXOAedPIhkmBCXK6r2MY2gGYWkJw-Dkse9mig


https://test.pypi.org/project/pkgname/0.0.1/

To install

py -3.8 -m pip install -i https://test.pypi.org/simple/ pkgname==0.0.1 (TEST)

Upload build PRD
python setup.py sdist bdist_wheel

python -m twine upload dist/* (PRD)

username = brworkit
password = Vwrmb@113342

py -3.8 -m pip install pkgname (PRD)

TO PRODUCTION

When you are ready to upload a real package to the Python Package Index you can do much the same as you did in this tutorial, but with these important differences:
Choose a memorable and unique name for your package. You don’t have to append your username as you did in the tutorial.
Register an account on https://pypi.org - note that these are two separate servers and the login details from the test server are not shared with the main server.

Use twine upload dist/* to upload your package and enter your credentials for the account you registered on the real PyPI. Now that you’re uploading the package in production, you don’t need to specify --repository; the package will upload to https://pypi.org/ by default.

Install your package from the real PyPI using pip install [your-package].

At this point if you want to read more on packaging Python libraries here are some things you can do:

Read more about using setuptools to package libraries in Packaging and distributing projects.

Read about Packaging binary extensions.

Consider alternatives to setuptools such as flit, hatch, and poetry.



