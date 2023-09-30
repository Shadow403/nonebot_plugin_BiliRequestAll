from setuptools import setup, find_packages
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Shadow403",
    version="0.2.5",
    author="Shadow403",
    author_email="anonymous_hax@foxmail.com",
    description="Use Medal Support Join QQ Group",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shadow403/nonebot_plugin_BiliRequestAll",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "nonebot2 >= 2.0.0",
        "nonebot-adapter-onebot >= 2.2.3",
        "requests >= 2.31.0"
        ],
    python_requires='>=3.10',
)