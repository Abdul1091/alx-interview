#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys
import re


if __name__ == "__main__":
    status = {"200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}
    count = 1
    file_size = 0

    def get_line(line):
        """Parse log line and extract file size and status code."""
        try:
            # Match <status code> <file size> at the end of the line
            pattern = r'.* (\d{3}) (\d+)$'
            match = re.match(pattern, line)
            if match:
                status_code = match.group(1)  # Get status code
                if status_code in status:
                    status[status_code] += 1
                return int(match.group(2))  # Get file size
        except Exception:
            return 0
        return 0

    def print_stats():
        """Print the accumulated statistics."""
        print("File size: {}".format(file_size))
        for key in sorted(status.keys()):
            if status[key]:
                print("{}: {}".format(key, status[key]))

    try:
        for line in sys.stdin:
            file_size += get_line(line)
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)
    
    # Final stats print
    print_stats()
