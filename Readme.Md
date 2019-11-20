# Introduction


## Project description:
### Description
This Project is converts XHTML markup Language to HTML and QML
### Goal
To enable Users connect to the chatbot through any channel irrespective of the rendering implementation of the channel

## Getting Started
**Base Language**: XHTML
**Test Language**: HTML, QML

### To get Started:
    pip install -r requirements.txt

    python adapter.py (command)

## Example

### Convert From CML to HTML:

    python adapter.py base_html

- Result: Generates a new file in the Test folder: **default**: cml_html.html
- Error: If the base file does not exist or the Test folder does not exist
#### More Information
**File Type**: HTML document text- HTML document text
- HTML document text
- exported SGML document text
- HTML document, ASCII text
MIME Type: text/html
Suggested file extension(s): sgml
**Source:** <http://checkfiletype.com/>

### Convert HTML to CML:
Command: `python adapter.py html_base PATH/to/base_file PATH/to/html_file PATH/to/output`

    python adapter.py html_base

- Result: generates a new file in the Test folder, **default**: html_cml.xhtml
- Error: if html file to be converted does exist or the Test folder doesn't exist

### Convert CML To QML:
Command: `python adapter.py base_qml PATH/to/base_file PATH/to/output`

    python adapter.py base_qml

- Result: Generates a new file in the Test folder; **default**: base_qml.qml
- Error: "Could not load QT platform" Solution: pyside2 is not properly install or in a wrong environment, create virtual env and pip install

**Note: Pops up a window from generated QML file**

### Convert QMl To CML:
Command: `python adapter.py base_qml PATH/to/base_file PATH/to/output`

    python adapter.py qml_base

- Result: Generates a new file in the Test Folder; **default**: qml_base.xhtml
- Error: FilenotFoundError if output folder does not exist or the base file doesnot exist


## Files:
**adapter.py:** This is the main formatting script
**index.xhtml:** The base file used for the convertion, also for testing 

Support For Emojis, ChatBot Message Display, ChatBot Actions
Demo will be presented



