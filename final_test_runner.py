import subprocess
import os

def run_tests():
    # Path to Python executable in your virtual environment
    python_exe = r"c:\Users\LAPTOPS HUB\Desktop\AutoPx\pxvenv\Scripts\python.exe"
    
    # List of test files relative to current working directory
    test_files = [
        "tests/test_cleaner.py",
        "tests/test_decision_engine.py",
        "tests/test_report_builder.py"
    ]
    
    log_file = "final_test_output.log"
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("=== AutoPX Test Run ===\n")
        for test in test_files:
            f.write(f"\n--- Running {test} ---\n")
            try:
                result = subprocess.run(
                    [python_exe, test],
                    capture_output=True,
                    text=True,
                    timeout=120  # Increase timeout if some tests are long
                )
                f.write(result.stdout)
                f.write(result.stderr)
                
                # Simple pass/fail summary
                if result.returncode == 0:
                    f.write(f"\n>>> {test} PASSED\n")
                else:
                    f.write(f"\n>>> {test} FAILED (return code {result.returncode})\n")
            except subprocess.TimeoutExpired:
                f.write(f"\n>>> {test} TIMED OUT\n")
            except Exception as e:
                f.write(f"\n>>> Error running {test}: {str(e)}\n")
    
    print(f"Tests completed. See {log_file} for details.")

if __name__ == "__main__":
    run_tests()
