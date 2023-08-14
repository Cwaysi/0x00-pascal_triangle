!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_metrics(file_size, status_codes):
    """
    Printing the metrics
    """
    print("File size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


codes_counting = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
file_size_total = 0
counter = 0

if __name__ == "__main__":
    try:
        for li in sys.stdin:
            try:
                status_code = li.split()[-2]
                if status_code in codes_counting.keys():
                    codes_counting[status_code] += 1
                file_size = int(li.split()[-1])
                file_size_total += file_size
            except Exception:
                pass
            counter += 1
            if counter == 10:
                print_metrics(file_size_total, codes_counting)
                counter = 0
    except KeyboardInterrupt:
        print_metrics(file_size_total, codes_counting)
        raise
   print_metrics(file_size_total, codes_counting)
