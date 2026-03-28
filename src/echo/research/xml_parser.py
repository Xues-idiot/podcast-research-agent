"""XML解析工具"""

import xml.etree.ElementTree as ET
from typing import Optional, Dict, List


class XmlParserTool:
    _instance: Optional["XmlParserTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parse(self, xml_str: str) -> Optional[Dict]:
        try:
            root = ET.fromstring(xml_str)
            return self._element_to_dict(root)
        except:
            return None

    def _element_to_dict(self, element: ET.Element) -> Dict:
        result: Dict = {}
        if element.attrib:
            result["@attributes"] = element.attrib
        if element.text and element.text.strip():
            if len(element) == 0:
                return element.text.strip()
            result["#text"] = element.text.strip()
        for child in element:
            child_dict = self._element_to_dict(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_dict)
            else:
                result[child.tag] = child_dict
        return result


def get_xml_parser_tool() -> XmlParserTool:
    return XmlParserTool()