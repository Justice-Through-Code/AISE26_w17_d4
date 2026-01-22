"""
Automated test runner for W17D4 Assignment

Reads TEST_PLAN.md, executes tests, and writes results to RESULTS.md
"""

import argparse
from pathlib import Path
import re


def parse_test_plan(test_plan_path):
    """
    Parse TEST_PLAN.md and extract test cases.

    TODO: Implement test plan parsing
    - Read TEST_PLAN.md file
    - Parse the evidence table
    - Extract test case IDs, inputs, and expected behaviors
    - Return list of test case dictionaries

    Args:
        test_plan_path (str): Path to TEST_PLAN.md

    Returns:
        list: List of test case dictionaries with keys:
              - test_case_id
              - input_description
              - expected_behavior
    """
    # TODO: Implement this function
    # Hint: Look for the evidence table in the markdown file
    # Hint: Use regex or simple string parsing to extract rows

    raise NotImplementedError("TODO: Implement parse_test_plan()")


def run_test_case(test_case, model, processor, embeddings=None):
    """
    Execute a single test case.

    TODO: Implement test case execution
    - Based on test_case_id, determine test type (normal, vision_stress, uncertain)
    - Load appropriate input (image, audio, or text query)
    - Run pipeline on input
    - Capture actual output
    - Determine pass/fail based on expected_behavior
    - Return test result dictionary

    Args:
        test_case (dict): Test case from parse_test_plan()
        model: Loaded model
        processor: Loaded processor
        embeddings (dict): Image embeddings (for CLIP retrieval)

    Returns:
        dict: Test result with keys:
              - test_case_id
              - input_description
              - expected_behavior
              - actual_output
              - pass_fail (True/False or "PASS"/"FAIL")
              - notes_next_step
    """
    # TODO: Implement this function

    raise NotImplementedError("TODO: Implement run_test_case()")


def write_results(results, output_path):
    """
    Write test results to RESULTS.md.

    TODO: Implement results writing
    - Create RESULTS.md with proper formatting
    - Include summary statistics (X/Y passed)
    - Write filled evidence table with actual outputs
    - Categorize failures by type (blur, low-light, etc.)
    - Include representative failure examples

    Args:
        results (list): List of test result dictionaries
        output_path (str): Path to RESULTS.md
    """
    # TODO: Implement this function
    # Hint: Use the RESULTS.md.template as a guide

    raise NotImplementedError("TODO: Implement write_results()")


def categorize_failures(results):
    """
    Categorize failures by type.

    TODO: Implement failure categorization
    - Group failures by category (blur, low-light, clutter, etc.)
    - Count failures per category
    - Return categorized failure dictionary

    Args:
        results (list): List of test result dictionaries

    Returns:
        dict: Failures grouped by category
    """
    # TODO: Implement this function

    raise NotImplementedError("TODO: Implement categorize_failures()")


def main():
    """
    Main entry point for test runner.

    TODO: Implement test runner logic
    - Parse command-line arguments
    - Load model
    - Parse test plan
    - Run all test cases
    - Write results to RESULTS.md
    - Print summary statistics
    """
    parser = argparse.ArgumentParser(description="W17D4 Test Runner")

    # TODO: Add arguments
    # parser.add_argument("--test-plan", default="TEST_PLAN.md")
    # parser.add_argument("--output", default="RESULTS.md")
    # parser.add_argument("--model", default="openai/clip-vit-base-patch32")

    args = parser.parse_args()

    # TODO: Implement test runner logic
    print("TODO: Implement test runner")

    # Example structure:
    # 1. Load model
    # 2. Parse test plan
    # 3. Run each test case
    # 4. Collect results
    # 5. Write RESULTS.md
    # 6. Print summary (X/Y passed, Z failures)


if __name__ == "__main__":
    main()
