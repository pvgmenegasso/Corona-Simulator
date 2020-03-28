import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Coronavirus Simulation",
    options={"build_exe": {"packages":["pygame, sys, random, time, threading, math"],}},
    executables = executables

    )
