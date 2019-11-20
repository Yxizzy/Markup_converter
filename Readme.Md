Introduction
Project description:
This Project is converts the 
Goal: Users can connect to the chatbot through any channel irrespective of the rendering implementation of the channel

How it works:
adapter.py: this is the main formatting script
test.py: this is used for testing purposes
index.xhtml: the base file used for the convertion, also for testing 
description: doctype xhtml 1.0 transitional  Root Element: html Root Namespace: http://www.w3.org/1999/xhtml encoding: utf-8 source: https://validator.w3.org/

Test Folder


Convert From CML to HTML:
To convert from the CML to HTML, 
run command python adapter.py base_html
result: generates a new file in the Test folder
error: if the base file does not exist or the Test folder does not exist
Generated file: default cml_html.html specifications: file type: 
File Type: HTML document text- HTML document text
- HTML document text
- exported SGML document text
- HTML document, ASCII text
MIME Type: text/html
Suggested file extension(s): sgml
source: http://checkfiletype.com/

Convert HTML to CML:
command: python adapter.py html_base PATH/to/base_file PATH/to/html_file PATH/to/output
run python adapter.py html_base
result: generates a new file in the Test folder, default=html_cml.xhtml
error: if html file to be converted does exist or the Test folder doesn't exist

Convert CML To QML:
command: python adapter.py base_qml PATH/to/base_file PATH/to/output
run python adapter.py base_qml
result: generates a new file in the Test folder; default base_qml.qml
error: "Could not load QT platform" Solution: pyside2 is not properly install or in a wrong environment, create virtual env and pip install
Note: create a desktop application/window for preview

Convert QMl To CML:
command: python adapter.py base_qml PATH/to/base_file PATH/to/output
run python adapter.py qml_base
result: generates a new file in the Test Folder; default qml_base.xhtml
error: FilenotFoundError if output folder does not exist or the base file doesnot exist

Getting Started
Base Language Chosen: XHTML
Backend: IBM WATSON
Test Language: HTML, MD, QML

To get Started:
pip install -r requirements.txt

python test.py: this will generate run all conversions and return test case in the Tests Directory
Test Directory: the following files were generated for each test

Support For Emojis

ChatBot Message Display 

ChatBot Actions

