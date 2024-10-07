import unittest
from data_parser import DataParser

class TestDataParser(unittest.TestCase):
    def setUp(self):
        self.json_data = '{"name": "John", "age": 30, "city": "New York"}'
        self.xml_data = '<person><name>John</name><age>30</age><city>New York</city></person>'
        self.yaml_data = "name: John\nage: 30\ncity: New York"

    def test_parse_json(self):
        result = DataParser.parse_json(self.json_data)
        self.assertEqual(result['name'], 'John')
        self.assertEqual(result['age'], 30)
        self.assertEqual(result['city'], 'New York')

    def test_parse_xml(self):
        result = DataParser.parse_xml(self.xml_data)
        root = result.getroot()
        self.assertEqual(root.find('name').text, 'John')
        self.assertEqual(root.find('age').text, '30')
        self.assertEqual(root.find('city').text, 'New York')

    def test_parse_yaml(self):
        result = DataParser.parse_yaml(self.yaml_data)
        self.assertEqual(result['name'], 'John')
        self.assertEqual(result['age'], 30)
        self.assertEqual(result['city'], 'New York')

    def test_invalid_json(self):
        invalid_json = '{"name": "John", "age": 30'
        with self.assertRaises(ValueError):
            DataParser.parse_json(invalid_json)

    def test_invalid_xml(self):
        invalid_xml = '<person><name>John</name><age>30</city>'
        with self.assertRaises(ValueError):
            DataParser.parse_xml(invalid_xml)

    def test_invalid_yaml(self):
        invalid_yaml = 'name: John\nage: 30: city: New York'
        with self.assertRaises(ValueError):
            DataParser.parse_yaml(invalid_yaml)

if __name__ == '__main__':
    unittest.main()
