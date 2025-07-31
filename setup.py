from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="video-downloader-bot",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Telegram bot that downloads videos from YouTube, Instagram, TikTok, and Twitter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/video-downloader-bot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "video-downloader-bot=main:main",
        ],
    },
) 