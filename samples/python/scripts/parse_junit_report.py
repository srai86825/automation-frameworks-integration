import sys
import os
import xml.etree.ElementTree as ET
import json

def parse_junit_report(report_path):
    log_file = 'parse_junit_log.txt'
    with open(log_file, 'w') as log:
        def log_print(message):
            print(message)
            log.write(message + '\n')

        log_print(f"Reading JUnit report from: {report_path}")

        if not os.path.exists(report_path):
            log_print(f"Error: File not found: {report_path}")
            return

        tree = ET.parse(report_path)
        root = tree.getroot()

        test_results = []
        for testcase in root.findall('testcase'):
            test_case_info = {
                'name': testcase.get('name'),
                'classname': testcase.get('classname'),
                'time': testcase.get('time'),
                'status': 'passed'
            }
            failure = testcase.find('failure')
            if failure is not None:
                test_case_info['status'] = 'failed'
                test_case_info['message'] = failure.get('message')
                test_case_info['type'] = failure.get('type')
            test_results.append(test_case_info)

        output_file = 'test_results.json'
        with open(output_file, 'w') as f:
            json.dump(test_results, f, indent=4)
        
        log_print(f"Test results written to: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python parse_junit_report.py <junit-report.xml>")
    else:
        parse_junit_report(sys.argv[1])
