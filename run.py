from packaging.specifiers import SpecifierSet
from packaging.version import Version

def check_dependency_conflict():
    try:
        spec1 = SpecifierSet("==2.24.0")
        spec2 = SpecifierSet(">=2.28")

        # Check if any version can satisfy both
        for v in ["2.24.0", "2.28.0", "2.30.0"]:
            if Version(v) in spec1 and Version(v) in spec2:
                return None

        raise Exception("Dependency conflict: requests==2.24.0 AND requests>=2.28")

    except Exception as e:
        return str(e)


def write_log(error):
    with open("logs/dependency_check.log", "w") as f:
        f.write(error)


if __name__ == "__main__":
    error = check_dependency_conflict()

    if error:
        print("ERROR DETECTED:")
        print(error)
        write_log(error)
    else:
        print("No dependency issues found.")
