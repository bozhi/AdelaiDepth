import setuptools

setuptools.setup(
    name="LeReS",
    version="1.4.7",
    packages=["leres", "leres.test", "leres.test.lib", "leres.test.tools"],
    package_dir={
        "leres": "LeReS",
        "leres.test": "LeReS/Minist_Test",
        "leres.test.lib": "LeReS/Minist_Test/lib",
        "leres.test.tools": "LeReS/Minist_Test/tools",
    }
)
