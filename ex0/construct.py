import sys
import os
import site


def inside_output() -> None:
    print()
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual environment: {os.path.basename(sys.prefix)}")
    print(f"Environment path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    print("Package installation path:")
    print(site.getsitepackages()[0])


def outside_output() -> None:
    print()
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again")


def main() -> None:
    if sys.prefix == sys.base_prefix:
        outside_output()
    else:
        inside_output()


if __name__ == "__main__":
    main()
