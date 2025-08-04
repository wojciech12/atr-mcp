#!/usr/bin/env python3
"""Git hook checker for Claude Code"""

import json
import sys
import subprocess
import os


def run_pre_commit_checks(format_only=False):
    """Run pre-commit checks script"""
    script_path = "./.claude/hooks/pre-commit-checks.py"

    cmd = ["uv", "run", script_path]
    if format_only:
        cmd.append("--format-only")

    try:
        result = subprocess.run(cmd, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        return False


def main():
    try:
        # Read JSON input from stdin
        input_data = sys.stdin.read().strip()
        if not input_data:
            print("No input data received")
            sys.exit(0)

        # Parse JSON
        data = json.loads(input_data)

        # Extract command from JSON
        command = data.get("tool_input", {}).get("command", "")

        print(f"🔍 Checking command: {command}")

        # Check if it's a git command
        if command.startswith("git"):
            if "git add" in command:
                print("🔍 Git add detected - running format and lint checks...")
                if not run_pre_commit_checks(format_only=True):
                    print("❌ Pre-commit checks failed for git add")
                    sys.exit(2)
                print("✅ Format and lint checks passed for git add")

            elif "git push" in command:
                print(
                    "🚀 Git push detected - running full checks (format, lint, tests)..."
                )
                if not run_pre_commit_checks(format_only=False):
                    print("❌ Pre-commit checks failed for git push")
                    sys.exit(2)
                print("✅ All checks passed for git push")

        # Allow the command to proceed
        sys.exit(0)

    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(0)


if __name__ == "__main__":
    main()
