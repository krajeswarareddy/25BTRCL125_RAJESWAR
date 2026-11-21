import json
from collections import Counter
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
LOGS_FILE = BASE_DIR / "logs.json"
REPORT_FILE = BASE_DIR / "log_analysis_report.json"


def initialize_sample_logs():
    """Creates logs.json with structured sample application logs if missing."""
    if not LOGS_FILE.exists():
        sample_logs = [
            {
                "timestamp": "2026-11-21T09:00:12",
                "level": "INFO",
                "service": "auth-service",
                "message": "User 'rajeswar' authenticated successfully",
                "response_time_ms": 42,
            },
            {
                "timestamp": "2026-11-21T09:03:45",
                "level": "INFO",
                "service": "api-gateway",
                "message": "GET /api/v1/dashboard 200 OK",
                "response_time_ms": 68,
            },
            {
                "timestamp": "2026-11-21T09:07:19",
                "level": "WARNING",
                "service": "cache-service",
                "message": "Redis memory usage reached 82% threshold",
                "response_time_ms": 115,
            },
            {
                "timestamp": "2026-11-21T09:12:04",
                "level": "ERROR",
                "service": "payment-service",
                "message": "Upstream gateway timeout after 3000ms",
                "response_time_ms": 3005,
            },
            {
                "timestamp": "2026-11-21T09:15:30",
                "level": "INFO",
                "service": "api-gateway",
                "message": "POST /api/v1/orders 201 Created",
                "response_time_ms": 94,
            },
            {
                "timestamp": "2026-11-21T09:18:51",
                "level": "CRITICAL",
                "service": "db-cluster",
                "message": "Primary database connection pool exhausted",
                "response_time_ms": 5012,
            },
            {
                "timestamp": "2026-11-21T09:22:10",
                "level": "ERROR",
                "service": "auth-service",
                "message": "Invalid JWT signature detected from IP 192.168.1.44",
                "response_time_ms": 19,
            },
            {
                "timestamp": "2026-11-21T09:25:00",
                "level": "WARNING",
                "service": "api-gateway",
                "message": "Rate limit approaching for client token #884",
                "response_time_ms": 81,
            },
        ]
        with open(LOGS_FILE, "w", encoding="utf-8") as file:
            json.dump(sample_logs, file, indent=4)


def load_logs():
    """Loads and validates JSON log entries from logs.json."""
    try:
        with open(LOGS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Expected a JSON array of log objects.")
            return data
    except FileNotFoundError:
        print(f"Error: {LOGS_FILE.name} not found.")
    except json.JSONDecodeError as err:
        print(f"JSON syntax error in {LOGS_FILE.name}: {err}")
    except ValueError as err:
        print(f"Data format error: {err}")
    return []


def analyze_logs(logs):
    """Computes severity counts, service breakdown, latency metrics, and critical alerts."""
    if not logs:
        print("No log records available to analyze.")
        return None

    level_counts = Counter(entry.get("level", "UNKNOWN").upper() for entry in logs)
    service_counts = Counter(entry.get("service", "unknown") for entry in logs)
    response_times = [
        entry["response_time_ms"]
        for entry in logs
        if isinstance(entry.get("response_time_ms"), (int, float))
    ]
    avg_latency = sum(response_times) / len(response_times) if response_times else 0.0
    max_latency = max(response_times) if response_times else 0

    alerts = [
        entry
        for entry in logs
        if entry.get("level", "").upper() in {"ERROR", "CRITICAL"}
    ]

    print("\n=== JSON Log Analysis Summary ===")
    print(f"Total Log Entries   : {len(logs)}")
    print(f"Average Latency     : {avg_latency:.2f} ms")
    print(f"Peak Latency        : {max_latency} ms")

    print("\nBreakdown by Severity Level:")
    for level in ["INFO", "WARNING", "ERROR", "CRITICAL"]:
        print(f"  - {level:<10}: {level_counts.get(level, 0)}")

    print("\nBreakdown by Service:")
    for service, count in service_counts.items():
        print(f"  - {service:<18}: {count}")

    print("\nHigh-Severity Alerts (ERROR / CRITICAL):")
    for alert in alerts:
        print(f"  [{alert['timestamp']}] {alert['level']} ({alert['service']}): {alert['message']}")

    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_file": LOGS_FILE.name,
        "total_entries": len(logs),
        "average_response_time_ms": round(avg_latency, 2),
        "max_response_time_ms": max_latency,
        "severity_breakdown": dict(level_counts),
        "service_breakdown": dict(service_counts),
        "high_severity_alerts": alerts,
    }
    return report


def filter_by_level(logs):
    """Filters and displays log entries matching a user-specified severity level."""
    level = input("Enter severity level to filter (INFO / WARNING / ERROR / CRITICAL): ").strip().upper()
    matched = [entry for entry in logs if entry.get("level", "").upper() == level]

    print(f"\n--- Logs with Level: {level} ({len(matched)} found) ---")
    if not matched:
        print("No matching entries found.")
        return

    for entry in matched:
        print(
            f"[{entry.get('timestamp')}] {entry.get('service')} | "
            f"{entry.get('message')} ({entry.get('response_time_ms')} ms)"
        )


def export_report(report):
    """Writes the analyzed summary dictionary to log_analysis_report.json."""
    if not report:
        print("Run the full analysis first before exporting.")
        return
    try:
        with open(REPORT_FILE, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)
        print(f"Analysis report successfully exported to '{REPORT_FILE.name}'.")
    except OSError as err:
        print(f"Failed to write report: {err}")


def main():
    initialize_sample_logs()
    logs = load_logs()
    latest_report = None

    while True:
        print("\n=== JSON-Based Log File Analyzer ===")
        print("1. Run Full Log Analysis")
        print("2. Filter Logs by Severity Level")
        print("3. Export Analysis Report (JSON)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            latest_report = analyze_logs(logs)
        elif choice == "2":
            filter_by_level(logs)
        elif choice == "3":
            if latest_report is None:
                latest_report = analyze_logs(logs)
            export_report(latest_report)
        elif choice == "4":
            print("Exiting JSON Log File Analyzer.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()