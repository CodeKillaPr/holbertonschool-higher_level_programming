import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML to.

    Returns:
        None
    """
    def add_items(parent, d):
        """
        Add dictionary items to the XML tree.

        Args:
            parent (Element): The parent XML element.
            d (dict): The dictionary to add to the XML tree.

        Returns:
            None
        """
        for key, value in d.items():
            element = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_items(element, value)
            else:
                element.text = str(value)

    root = ET.Element("data")
    add_items(root, dictionary)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    def parse_element(element):
        """
        Convert XML element and its children to a dictionary.

        Args:
            element (Element): The XML element to convert.

        Returns:
            dict: The converted dictionary.
        """
        parsed_dict = {}
        for child in element:
            if len(child) > 0:
                parsed_dict[child.tag] = parse_element(child)
            else:
                parsed_dict[child.tag] = child.text
        return parsed_dict

    tree = ET.parse(filename)
    root = tree.getroot()
    return parse_element(root)


# Example usage
if __name__ == "__main__":
    data = {
        'name': 'John',
        'age': 30,
        'address': {
            'street': '123 Elm St',
            'city': 'Somewhere'
        }
    }

    # Serialize to XML
    serialize_to_xml(data, 'data.xml')

    # Deserialize from XML
    deserialized_data = deserialize_from_xml('data.xml')
    print(deserialized_data)
