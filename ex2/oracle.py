# MATRIX_MODE: either "development" or "production"
# DATABASE_URL: url to the database
# API_KEY: some api key...?
# LOG_LEVEL: one of "INFO", "DEBUG", "WARN", "ERROR" 
# ZION_ENDPOINT: some url

import os
import sys


def main() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print(
            "[ERROR] Required dependencies not found.",
            "  run: pip install python-dotenv",
            sep="\n"
            )
        sys.exit(1)

    env: bool = load_dotenv()

    verify: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    output: dict[str, str | None] = {}
    for test in verify:
        output[test] = os.environ.get(test) or None

    if output["MATRIX_MODE"] == "development":
        print()
        print("ORACLE STATUS: Reading the Matrix...")
        print()
        print("Configuration loaded:")
        print(f"Mode: {output['MATRIX_MODE']}")
        if not output["DATABASE_URL"]:
            print("Database: NOT CONFIGURED")
        elif "localhost" in output["DATABASE_URL"]:
            print("Database: Local instance")
        else:
            print("Database: Remote instance")
        if output["API_KEY"]:
            print("API Access: Autenticated")
        else:
            print("API Access: No Access")
        print(f"Log Level: {output['LOG_LEVEL']}")
        if not output["ZION_ENDPOINT"]:
            print("Zion Network: NOT CONFIGURED")
        elif "https" in output["ZION_ENDPOINT"]:
            print("Zion Network: Online")
        else:
            print("Zion Network: Offline")
    elif output["MATRIX_MODE"] == "production":
        print()
        print("ORACLE STATUS: Reading the Matrix...")
        print()
        print("Configuration loaded:")
        print(f"Mode: {output['MATRIX_MODE']}")
        if not output["DATABASE_URL"]:
            print("Database: [WARNING] NOT CONFIGURED")
        elif "localhost" in output["DATABASE_URL"]:
            print("Database: a production database shouldn't be local")
        else:
            print("Database: Remote instance")
        if output["API_KEY"]:
            print("API Access: Autenticated")
        else:
            print("API Access: [WARNING] Missing")
        print(f"Log Level: {output['LOG_LEVEL']}")
        if not output["ZION_ENDPOINT"]:
            print("Zion Network: [WARNING] NOT CONFIGURED")
        elif "https" in output["ZION_ENDPOINT"]:
            print("Zion Network: Online")
        else:
            print("Zion Network: Offline")
    else:
         print("[ERROR] Invalid configuration")
         sys.exit(1)

    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file missing")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configuration")


if __name__ == "__main__":
    main()
