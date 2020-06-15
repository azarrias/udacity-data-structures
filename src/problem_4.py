class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

"""
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
"""

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return user_inheritance(user, group, [])

def user_inheritance(user, group, groups):
    if user in group.get_users():
        return True

    # if there are no other groups to recurse and this group has no children, 
    # the user is not within the inheritance tree
    #if len(groups) == 0:
    groups.extend(group.get_groups())
    if len(groups) == 0:
        return False

    return user_inheritance(user, groups[0], groups[1:])

def eval_test(test_number, expected_output, actual_output):
    print("")
    print("TEST CASE " + str(test_number))
    print("===========")
    print("- expected output:")
    print(expected_output)
    print("- actual output:")
    print(actual_output)
    print("")

if __name__ == "__main__":
    # setup data
    g1 = Group("g1")
    g2 = Group("g2")
    g1_1 = Group("g1_1")
    g1_2 = Group("g1_2")
    g1.add_group(g1_1)
    g1.add_group(g1_2)
    g1_1_1 = Group("g1_1_1")
    g1_1_2 = Group("g1_1_2")
    g1_1.add_group(g1_1_1)
    g1_1.add_group(g1_1_2)
    user1 = "user1"
    g1.add_user(user1)
    user1_1_2 = "user1_1_2"
    g1_1_2.add_user(user1_1_2)

    # test case 1
    result = is_user_in_group(user1, g1)
    expected_output = True
    eval_test(1, expected_output, result)

    # test case 2
    result = is_user_in_group(user1, g2)
    expected_output = False
    eval_test(2, expected_output, result)

    # test case 3
    result = is_user_in_group(user1_1_2, g1)
    expected_output = True
    eval_test(3, expected_output, result)

    # test case 4
    result = is_user_in_group(user1_1_2, g2)
    expected_output = False
    eval_test(4, expected_output, result)

    # test case 5
    result = is_user_in_group("nonexistent_user", g1_2)
    expected_output = False
    eval_test(5, expected_output, result)