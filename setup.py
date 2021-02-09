"""setup"""

from setuptools import setup, find_packages

setup(
    name="slack_python_logging_cameron_test",
    description="Module for logging to a Slack channel with webhooks",
    version="3.0.1-rc.2",
    python_requires='>=3.6',
    packages=find_packages(),
    # metadata
    author="theredcameron",
    author_email="redcamerontest@gmail.com",
    url="https://github.com/theredcameron/slack_python_logging",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords=["reddit", "slack python_logging"]
)
