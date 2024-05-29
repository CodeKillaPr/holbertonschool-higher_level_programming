import xml.etree.ElementTree as ET
""" explore serialization and deserialization of XML data """


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML
    format and save it to the given filename.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename where the XML data will be saved.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a given filename into a Python dictionary.

    Parameters:
    filename (str): The filename from which to read the XML data.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}

        for key, value in dictionary.items():
            if value.isdigit():
                dictionary[key] = int(value)
            else:
                try:
                    dictionary[key] = float(value)
                except ValueError:

                    pass

        return dictionary
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")
        return None
