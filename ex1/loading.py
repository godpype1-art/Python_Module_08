import importlib.metadata


def check_dependencies() -> bool:
    import_missing: bool = False
    dependencies: dict[str, str] = {
        "numpy": "Numerical computation",
        "pandas": "Data manipulation",
        "matplotlib": "Visualization"
        }
    for lib in dependencies:
        try:
            importlib.import_module(lib)
        except ModuleNotFoundError as error:
            if not import_missing:
                print("[WARNING] Some modules are missing!")
            print(f"[WARNING] {error}")
            import_missing = True
    if import_missing:
        print()
        print(
            "Install the correct dependencies with pip or Poetry and try again"
            )
        print(" run: pip install -r requirements.txt  # with pip")
        print("  python3 loading.py")
        print("  or")
        print(" run: poetry install                 # with Poetry")
        print(" poetry run python loading.py")
        return False
    else:
        print()
        print("LOADING STATUS: Loading programs...")
        print()
        print("Checking dependencies:")
        for lib, value in dependencies.items():
            print(
                f"[OK] {lib} "
                f"({importlib.metadata.version(lib)}) - {value} ready"
                )
        return True


def matrix_data() -> None:

    import numpy
    import matplotlib.pyplot as mpl
    import pandas

    rng = numpy.random.default_rng()

    warning_type = rng.integers(1, 6, 1000)
    sectors = rng.integers(1, 11, 1000)
    risk = rng.normal(35, 12, 1000).round(2)

    df = pandas.DataFrame(
        {"Warning": warning_type, "Sector": sectors, "Danger": risk}
        )
    peak = df.groupby("Sector")["Danger"].max()
    counts = pandas.crosstab(df["Sector"], df["Warning"])

    counts.plot(kind="bar", stacked=False)
    fig, ax = mpl.subplots()
    positions = numpy.arange(len(peak))
    counts.plot(kind="bar", stacked=False, ax=ax)
    ax.set_title("Damage Report")
    ax.set_xlabel("Sector")
    ax.set_ylabel("Warning Count")
    ax2 = ax.twinx()
    ax2.plot(positions, peak.values, marker="o", color="black")
    ax2.set_ylabel("Damage peak (%)")
    ax2.set_ylim(0, 100)
    print()
    print("Analysing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
    print()
    print("Analysis complete!")
    mpl.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if check_dependencies():
        matrix_data()
