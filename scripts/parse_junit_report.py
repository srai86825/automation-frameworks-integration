

import xml.etree.ElementTree as ET
import json
import os

def parse_junit_xml(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    results = []

    for testcase in root.findall('.//testcase'):
        # Extract the test case details
        result = {
            'name': testcase.get('name'),
            'classname': testcase.get('classname'),
            'status': 'passed' if not testcase.find('failure') else 'failed'
        }
        
        # Check for `subid` as a property or attribute (modify this based on actual format)
        subid = None
        for property in testcase.findall('properties/property'):
            if property.get('name') == 'subid':
                subid = property.get('value')
                break
        
        result['subid'] = subid if subid else 'not_available'
        results.append(result)

    return results

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]  # Path to the JUnit XML file
    results = parse_junit_xml(file_path)
    print(json.dumps(results, indent=2))
