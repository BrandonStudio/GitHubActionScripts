from sys import argv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse(argv[0])
root = tree.getroot()

# Define the namespace
namespace = {'msbuild': 'http://schemas.microsoft.com/developer/msbuild/2003'}

# Look for ApplicationVersion element
application_version = root.find('.//msbuild:ApplicationVersion', namespace).text

# Extract the version prefix
version_prefix = '.'.join(application_version.split('.')[:3])

print(version_prefix)
