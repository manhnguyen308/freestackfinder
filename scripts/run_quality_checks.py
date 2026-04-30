"""
Run all FreeStackFinder QA scripts in sequence.

Usage:
    python scripts/run_quality_checks.py
    python scripts/run_quality_checks.py --with-build
    python scripts/run_quality_checks.py --quiet
    python scripts/run_quality_checks.py --with-counts

Flags:
    --with-build   Run Hugo build after QA checks (requires Hugo on PATH)
    --quiet        Suppress verbose child output; only show headers and summary
    --with-counts  Print article count by silo report, including future-dated warnings

Exit code is non-zero if any check or build fails.
Article count mismatches do not affect exit code. Future-dated live articles
are blocked by the front matter validator because Hugo excludes them from
normal production builds.
Hugo build: run `hugo` from repo root. If Hugo is not on PATH, install it
or run the build separately using the repo's documented build command.
"""

import subprocess
import sys
import os
import argparse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHECKS = [
    ("Front matter validation", "scripts/validate_front_matter.py"),
    ("Internal link check",     "scripts/check_internal_links.py"),
    ("Feature image check",     "scripts/check_feature_images.py"),
]


def run_check(label, script_path, quiet):
    print(f"\n{'=' * 56}", flush=True)
    print(f"  {label}", flush=True)
    print(f"{'=' * 56}", flush=True)
    full_path = os.path.join(REPO_ROOT, script_path)
    result = subprocess.run(
        [sys.executable, full_path],
        cwd=REPO_ROOT,
        capture_output=quiet,
        text=True,
    )
    if quiet:
        if result.stdout:
            last_lines = result.stdout.strip().splitlines()[-4:]
            print("\n".join(last_lines))
        if result.returncode != 0 and result.stderr:
            print(result.stderr.strip())
    return result.returncode


def run_hugo_build(quiet):
    print(f"\n{'=' * 56}", flush=True)
    print("  Hugo build", flush=True)
    print(f"{'=' * 56}", flush=True)
    result = subprocess.run(
        ["hugo", "--minify"],
        cwd=REPO_ROOT,
        capture_output=quiet,
        text=True,
    )
    if quiet:
        if result.stdout:
            print(result.stdout.strip()[-400:])
        if result.returncode != 0 and result.stderr:
            print(result.stderr.strip())
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Run FreeStackFinder QA checks")
    parser.add_argument("--with-build", action="store_true", help="Run Hugo build after QA checks")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose child output")
    parser.add_argument("--with-counts", action="store_true", help="Print article count by silo report")
    args = parser.parse_args()

    results = {}

    for label, script in CHECKS:
        code = run_check(label, script, args.quiet)
        results[label] = code

    if args.with_build:
        code = run_hugo_build(args.quiet)
        results["Hugo build"] = code

    if args.with_counts:
        print(f"\n{'=' * 56}", flush=True)
        print("  Article count by silo", flush=True)
        print(f"{'=' * 56}", flush=True)
        counts_path = os.path.join(REPO_ROOT, "scripts", "report_article_counts.py")
        subprocess.run([sys.executable, counts_path], cwd=REPO_ROOT)

    passed = [k for k, v in results.items() if v == 0]
    failed = [k for k, v in results.items() if v != 0]

    print(f"\n{'=' * 56}", flush=True)
    print("  Summary", flush=True)
    print(f"{'=' * 56}", flush=True)
    for label in passed:
        print(f"  PASSED   {label}")
    for label in failed:
        print(f"  FAILED   {label}")
    print(f"\n  {len(passed)} passed · {len(failed)} failed")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
