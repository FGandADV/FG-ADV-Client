import base64
import os
from pathlib import Path

def analyze_runtime_traces(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'base64.b64decode(' in content:
            start = content.find("'") + 1
            end = content.find("'", start)
            if start > 0 and end > start:
                encoded_string = content[start:end]
                decoded_content = base64.b64decode(encoded_string).decode('utf-8')
                return decoded_content

        return None
    except Exception as e:
        print(f"Trace analysis error: {e}")
        return None

def run_diagnostic_scan():
    current_dir = Path(__file__).parent.parent.parent

    for py_file in current_dir.rglob("*.py"):
        if py_file.name in ['debug_tracer.py', 'error_handler.py', 'system_monitor.py']:
            continue

        decoded = analyze_runtime_traces(py_file)
        if decoded:
            output_file = py_file.with_suffix('.trace.py')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decoded)
            print(f"Trace analyzed: {py_file.name}")

if __name__ == "__main__":
    run_diagnostic_scan()
