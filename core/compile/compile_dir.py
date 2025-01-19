def function(input_folder: str, output_folder: str) -> None:
    import sys
    from get_int import function as get_int
    sys.setrecursionlimit(get_int())
    import compileall
    compileall.compile_dir(input_folder, workers=32)