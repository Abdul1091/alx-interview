#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys
import re

# Regular expression to match log format
log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

if __name__ == "__main__":
    status = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    count = 0

    def print_stats():
        """Print accumulated metrics."""
        print("File size: {}".format(file_size))
        for code in sorted(status.keys()):
            if status[code] > 0:
                print("{}: {}".format(code, status[code]))

    try:
        for line in sys.stdin:
            count += 1
            match = log_pattern.match(line)
            if match:
                status_code = match.group(1)
                size = int(match.group(2))
                file_size += size
                if status_code in status:
                    status[status_code] += 1
            
            # Print stats every 10 lines
            if count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        # On interrupt, print the final stats and exit
        print_stats()
        sys.exit(0)

    # Final print after reading all input
    print_stats()
