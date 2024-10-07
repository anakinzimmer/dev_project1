import json
import xml.etree.ElementTree as ET
import yaml
import requests


class DataParser:
    @staticmethod
    def parse_json(data: str):
        """Parse JSON data."""
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")

    @staticmethod
    def parse_xml(data: str):
        """Parse XML data."""
        try:
            return ET.ElementTree(ET.fromstring(data))
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML data: {e}")

    @staticmethod
    def parse_yaml(data: str):
        """Parse YAML data."""
        try:
            return yaml.safe_load(data)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML data: {e}")

    @staticmethod
    def get_data_from_api(url: str, headers: dict = None):
        """Make a GET request to an API and return the response."""
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            raise ConnectionError(f"Failed to fetch data from API: {response.status_code}")
