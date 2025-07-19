from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="formlabs-mcp-bridge",
    version="1.0.0",
    author="Formlabs API MCP Team",
    author_email="developers@formlabs.com",
    description="Model-Context Protocol bridge for Formlabs 3D printer API integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kradriany/formlabs-api-mcp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "formlabs-mcp=formlabs_mcp_bridge.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "formlabs_mcp_bridge": ["*.json"],
    },
) 