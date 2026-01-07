import unittest
import sys
import os

def run_tests():
    # Ensure current directory is in path
    sys.path.insert(0, os.path.abspath(os.getcwd()))
    
    print("=== AutoPX Test Suite Running ===")
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n=== Test Summary ===")
    print(f"Tests Run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("\nALL TESTS PASSED! ✅")
    else:
        print("\nSOME TESTS FAILED. ❌")
        for failure in result.failures:
            print(f"\nFAILURE: {failure[0]}")
            print(failure[1])
        for error in result.errors:
            print(f"\nERROR: {error[0]}")
            print(error[1])
            
if __name__ == "__main__":
    run_tests()
