#!/usr/bin/env python3
"""Pre-commit checks for Claude Code hooks"""

import argparse
import subprocess
import sys


def run_command(cmd, description):
    """Run a command and handle its output"""
    print(f"🔍 {description}...")
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False


def run_format_check():
    """Run format check and attempt to fix if needed"""
    print("🎨 Checking format...")
    if not run_command("npm run format", "Format check"):
        print("❌ Format check failed. Running format fix...")
        if run_command("npm run format:fix", "Format fix"):
            print("✅ Format fixed")
        else:
            return False
    return True


def run_lint():
    """Run lint and attempt to fix if needed"""
    print("🔍 Running lint...")
    if not run_command("npm run lint", "Lint check"):
        print("❌ Lint failed. Trying to fix...")
        if run_command("npm run lint:fix", "Lint fix"):
            if run_command("npm run lint", "Lint check after fix"):
                return True
            else:
                print("❌ Lint errors could not be auto-fixed. Please fix manually.")
                return False
        else:
            return False
    return True


def run_tests():
    """Run tests"""
    print("🧪 Running tests...")
    if not run_command("npm test", "Tests"):
        print("❌ Tests failed. Please fix before committing.")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Pre-commit checks for Claude Code hooks"
    )
    parser.add_argument(
        "--format-only", action="store_true", help="Run only format and lint checks"
    )
    parser.add_argument("--no-tests", action="store_true", help="Skip tests")

    args = parser.parse_args()

    print("Running pre-commit checks...")

    # Run format check
    if not run_format_check():
        sys.exit(2)

    # Run lint
    if not run_lint():
        sys.exit(2)

    # Run tests if requested
    if not args.format_only and not args.no_tests:
        if not run_tests():
            sys.exit(2)

    print("✅ All checks passed!")
    sys.exit(0)


if __name__ == "__main__":
    main()
