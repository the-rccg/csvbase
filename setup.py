from setuptools import setup, find_packages


setup(
    name="csvbase",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click", "flask"],
    entry_points="""
        [console_scripts]
        csvbase=csvbase:main
    """,
)
