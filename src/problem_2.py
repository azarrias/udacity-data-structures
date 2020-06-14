import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.exists(path):
      return []

    path = os.path.normpath(path)

    if os.path.isfile(path):
      if path.endswith(suffix):
        return [path]
      return []

    if os.path.isdir(path):
      subdir_list = []
      subdir_elements = os.listdir(path)
      while subdir_elements:
        listing = find_files(suffix, os.path.join(path, subdir_elements[0]))
        subdir_list.extend(listing)
        subdir_elements.pop(0)
      return subdir_list

def eval_test(test_number, expected_output, actual_output):
    print("")
    print("TEST CASE " + str(test_number))
    print("===========")
    print("- expected output:")
    print(expected_output)
    print("- actual output:")
    print(actual_output)
    print("")

# test case 1
expected_output = ['testdir\\subdir1\\a.c', 'testdir\\subdir3\\subsubdir1\\b.c', 'testdir\\subdir5\\a.c', 'testdir\\t1.c']
result = find_files(".c", "./testdir")
eval_test(1, expected_output, result)

# test case 2
expected_output = ['testdir\\subdir1\\a.h', 'testdir\\subdir3\\subsubdir1\\b.h', 'testdir\\subdir5\\a.h', 'testdir\\t1.h']
result = find_files(".h", "./testdir")
eval_test(2, expected_output, result)

# test case 3
expected_output = ['testdir\\subdir2\\.gitkeep', 'testdir\\subdir4\\.gitkeep']
result = find_files(".gitkeep", "./testdir")
eval_test(3, expected_output, result)
