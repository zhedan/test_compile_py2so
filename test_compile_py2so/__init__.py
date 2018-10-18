def main():
  from . import mod_a
  from test_compile_py2so import mod_a

  from test_compile_py2so.mod_a import a_fun
  from mod_a import a_fun
