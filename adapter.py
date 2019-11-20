import os
from lxml import html, etree

# Base Language is XHTML
#This Script converts between the CML and two selected markup languages
__author__ = "Sylvia Onwukwe"
__version__ = "1.0"
__all__ = []

def base_html(base_file, output):
    """Converts CML to HTML for older-browser rendering
    :param str base_file: Unicode string or bytes(path to the source xhtml file)
    :param str output: output will be written to this specified path in html format
    :returns: converted html file
    :rtype: unicode
    :raises FileNotFoundError: if the base file is not found
    :raises ModuleNotFoundError: if the required dependency is not found
    """
    try:
        new_file = html.fromstring(open(base_file).read())
    except FileNotFoundError:
        print("Base File doesn't exist")
    except ModuleNotFoundError:
        print("LXML not installed")
    output = open(output, 'wb')
    output.write("<!DOCTYPE html>")
    output.write(etree.tostring(new_file))
    return new_file

def html_base(base_file, html_file, output):
    """Converts HTML back to xHTML
    :param str base_file: Unicode string or bytes(path to the source xhtml file)
    :param str html_file: Unicode string or bytes(path to the generated html file)
    :param str output: output will be written to this specified path in xhtml format
    :returns: converted xhtml file
    :rtype: unicode
    :raises FileNotFoundError: if the base file is not found
    :raises ModuleNotFoundError: if the required dependency is not found
    """
    base_html(base_file, output)
    html_file = './Tests/test_file.html'
    try:
        new_file = html.fromstring(open(html_file).read())
    except FileNotFoundError:
        print("Base File doesn't exist")
    output = open('./Tests/test_file.xhtml', 'rb+')
    output.write(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
    output.write(etree.tostring(new_file))
    return output

def base_qml(base_file, output):
    """Generate a Qml file to display base_file
    :param str base_file: Unicode string or bytes(path to the source xhtml file)
    :param str output: output will be written to this specified path in qml format
    :returns: converted xhtml file
    :rtype: unicode
    :raises FileNotFoundError: if the base file is not found
    :raises ModuleNotFoundError: if the required dependency is not found
    """
    with open(base_file, 'r') as file:
        data = file.read().replace('"', "'")
        new_file = open(output, 'w')
        new_file.write("import QtQuick 2.12\nimport QtQuick.Controls 2.12\nimport QtWebEngine 1.0")
        new_file.write("\nApplicationWindow {\nid: window\nvisible: true\nwidth:640\nheight:480\nWebEngineView {\nid: webEngineView\nanchors.fill: parent\n}")
        new_file.write("Component.onCompleted: {\nvar html="+'"' +data +'"'+"\nwebEngineView.loadHtml(html)\n}\n}")
    if __name__ == '__main__':

        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app = QtGui.QGuiApplication(sys.argv)

        engine = QtQml.QQmlApplicationEngine()

        url = QtCore.QUrl.fromLocalFile(output)
        engine.load(url)
        if not engine.rootObjects():
            sys.exit(-1)

        sys.exit(app.exec_())

