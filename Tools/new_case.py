from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent

    cases_dir = base_dir / "cases"
    cases_dir.mkdir(exist_ok=True)

    print("=== VulnForge New CVE Case Tool ===")
    cve_id = input("CVE ID (e.g., CVE-2024-12345): ").strip()
    if not cve_id:
        print("CVE ID is required. Exiting.")
        return

    # Normalize CVE ID a bit
    cve_id = cve_id.upper()

    short_title = input("Short title (e.g., SQL Injection in XYZ App): ").strip()
    if not short_title:
        print("Short title is required. Exiting.")
        return

    case_dir = cases_dir / cve_id
    case_dir.mkdir(exist_ok=True)

    notes_path = case_dir / "notes.md"

    if notes_path.exists():
        print(f"notes.md already exists for {cve_id}. Not overwriting.")
        print(f"Location: {notes_path}")
        return

    content = f"""# {cve_id} — {short_title}

## Summary

## CVSS & Metadata

- CVSS:
- CWE:
- Vendor:
- Disclosure Date:

## Lab Environment

## Exploitation Steps

## Impact

## Mitigations

## Defender Playbook
"""

    notes_path.write_text(content, encoding="utf-8")

    print(f"Created case directory: {case_dir}")
    print(f"Created notes file:     {notes_path}")


if __name__ == "__main__":
    main()
