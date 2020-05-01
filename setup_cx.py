import cx_Freeze

executables = [cx_Freeze.Executable("sudoku.py")]

cx_Freeze.setup(
    name="just a test",
    options={
        "build.exe": {
            "packages": ["pygame"],
            "include_files": ["common.py", "ptext.py"]
        }
    },
    executables=executables
)
