import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Create the root element of the XML tree """
    root = ET.Element("data")

    """ Iterate over the dictionary and create elements for each key-value pair """
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    """ Create the XML tree and write it to the file """
    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        return False


def deserialize_from_xml(filename):
    try:
        """ Parse the XML file and get the root element """
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {}

        """ Iterate over the child elements of the root element """
        for child in root:
            value = child.text
            if value.isdigit():
                dictionary[child.tag] = int(value)
            else:
                try:
                    dictionary[child.tag] = float(value)
                except ValueError:
                    dictionary[child.tag] = value

        return dictionary
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")
        return None
