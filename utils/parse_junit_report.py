import xml.etree.ElementTree as ET
import json

def parse_junit_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    results = {}
    for testcase in root.findall('.//testcase'):
        result = 'passed' if not testcase.find('failure') else 'failed'
        subid = None
        for property in testcase.findall('properties/property'):
            if property.get('name') == 'subid':
                subid = property.get('value')
        if subid:
            results[subid] = result
    return results

if __name__ == "__main__":
    results = parse_junit_xml("samples/python/pytest/sample_reports/junit-report.xml")
    print(json.dumps(results, indent=2))
