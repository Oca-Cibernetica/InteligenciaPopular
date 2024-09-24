from setuptools import setup, find_packages

setup(
    name='inteligencia_popular',
    description='Inteligência Popular - biblioteca para acesso e análise de dados abertos sobre o Brasil',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['**/*.csv']},
    python_requires='>=3.7',
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'requests',
        'awesome-slugify',
    ],
)
