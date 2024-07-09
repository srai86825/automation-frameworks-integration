import xml.etree.ElementTree as ET
import json

def parse_junit_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    results = []
    for testcase in root.findall('.//testcase'):
        subid = None
        for prop in testcase.findall('.//property'):
            if prop.get('name') == 'subid':
                subid = prop.get('value')
                break
        result = {
            'name': testcase.get('name'),
            'classname': testcase.get('classname'),
            'status': 'passed' if not testcase.find('failure') else 'failed',
            'subid': subid
        }
        results.append(result)
    return results

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    results = parse_junit_xml(file_path)
    print(json.dumps(results))
