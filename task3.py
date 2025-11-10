"""Log parser and analyzer."""
import sys
from collections import Counter
from typing import List, Dict, Optional

def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    Parses a single log line into components.

    Example line: "2024-01-22 08:30:01 INFO User logged in successfully."
    Returns dictionary: {'date': '2024-01-22', 'time': '08:30:01', 
                        'level': 'INFO', 'message': '...'}
    Or None if line has incorrect format.
    """
    try:
        parts = line.strip().split(' ', 3)
        if len(parts) == 4:
            return {
                'date': parts[0],
                'time': parts[1],
                'level': parts[2],
                'message': parts[3]
            }
    except (ValueError, IndexError, AttributeError) as e:
        print(f"Error parsing line: {line.strip()} - {e}", file=sys.stderr)
    return None

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Loads and parses log file.

    Handles FileNotFoundError and IOError exceptions.
    Uses list comprehension to filter out lines that 
    couldn't be parsed (returned None).
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            logs = [parsed for line in f if (parsed := parse_log_line(line))]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1) # Exit with error code
    except PermissionError as e:
        print(f"Permission denied: {e}", file=sys.stderr)
        sys.exit(1) # Exit with error code
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}", file=sys.stderr)
        sys.exit(1) # Exit with error code
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}", file=sys.stderr)
        sys.exit(1) # Exit with error code

    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Filters list of logs by specified level (case insensitive).
    """
    # Use another list comprehension for filtering
    target_level = level.lower()
    return [log for log in logs if log['level'].lower() == target_level]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Counts number of entries for each logging level.
    """
    return Counter(log['level'] for log in logs)

def display_log_counts(counts: Dict[str, int]):
    """
    Displays count results as formatted table.
    """
    print("\nLogging level statistics:")
    print("Logging level    | Count")
    print("-----------------|-----------")
    # :<16 - left alignment, 16 characters
    # :>9 - right alignment, 9 characters
    for level, count in sorted(counts.items()):
        print(f"{level:<16} | {count:>9}")

def main():
    """
    Main script function. Processes command line arguments.
    """
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"python {sys.argv[0]} <path_to_log_file> [log_level]")
        print("\nExample for statistics:")
        print(f"python {sys.argv[0]} example.log")
        print("\nExample for filtering (e.g., by 'ERROR' level):")
        print(f"python {sys.argv[0]} example.log ERROR")
        sys.exit(1)

    file_path = sys.argv[1]
    all_logs = load_logs(file_path)

    if not all_logs:
        print("Log file is empty or contains no valid entries.")
        return

    # Mode 2: Filtering by level
    if len(sys.argv) == 3:
        level_to_filter = sys.argv[2]
        filtered = filter_logs_by_level(all_logs, level_to_filter)

        print(f"\nLog details for level '{level_to_filter.upper()}':\n")
        if not filtered:
            print(f"No entries found for level '{level_to_filter.upper()}'.")
        else:
            # Display filtered lines in original format
            for log in filtered:
                print(f"{log['date']} {log['time']} {log['level']} {log['message']}")

    # Mode 1: General statistics
    elif len(sys.argv) == 2:
        counts = count_logs_by_level(all_logs)
        display_log_counts(counts)

    else:
        print("Error: Too many arguments.", file=sys.stderr)
        print(f"Usage: python {sys.argv[0]} <path_to_log_file> [log_level]")
        sys.exit(1)

if __name__ == "__main__":
    main()
