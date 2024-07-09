import xml.etree.ElementTree as ET
import json
import sys

def parse_junit_xml(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    results = {}
    
    for testcase in root.findall('.//testcase'):
        test_name = testcase.get('name')
        subid = testcase.get('subid', 'N/A')  # Default to 'N/A' if subid is not found
        status = 'passed' if not testcase.find('failure') else 'failed'
        results[subid] = status
    
    return results

if __name__ == "__main__":
    report_path = sys.argv[1]
    results = parse_junit_xml(report_path)
    print(json.dumps(results))
