#!/usr/bin/env python

"""
"""

if __name__ == "__main__":
    import os
    input_folder = os.path.dirname(__file__)
    output_folder = os.path.abspath(os.path.join(input_folder, "../LibS/"))

    import os
    from pathlib import Path
    input_folder = os.path.dirname(__file__)
    output_folder = Path(input_folder).parent / "LibS"
    output_folder = output_folder.resolve()
    print(type(output_folder))
    print(type(Path(input_folder).parent))

    from compile_dir import function as compile_dir
    compile_dir(input_folder, output_folder)
    import shutil
    shutil.move(os.path.join(input_folder, '__pycache__', 'compile_dotpy.cpython-311.pyc'), os.path.join(output_folder, 'tools.pyc'))
