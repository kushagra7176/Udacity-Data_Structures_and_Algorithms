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
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True
    list_group = group.get_groups()
    for groups in list_group:
        if is_user_in_group(user,groups):
            return True
    return False

print("""***Test Case 1***""")
empty_grp = Group("empty")
user = "user"
print(empty_grp.get_name(), "Should be False:", is_user_in_group(user, empty_grp))

print("""***Test Case 2***""")
grp = Group("test_grp")
user1 = "user1"
user2 = "user2"
user3 = "user3"
user4 = "user4"
grp.add_user(user1)
grp.add_user(user2)
grp.add_user(user3)
print(grp.get_name(), "Should be True:", is_user_in_group(user1, grp))
print(grp.get_name(), "Should be True:", is_user_in_group(user2, grp))
print(grp.get_name(), "Should be True:", is_user_in_group(user3, grp))
print(grp.get_name(), "Should be False:", is_user_in_group(user4, grp))

print("***Test Case 3***")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_user_a = "sub_child_user_a"
child.add_group(sub_child)
parent.add_group(child)
print(parent.get_name(), "Should be True:", is_user_in_group(sub_child_user, parent))
print(child.get_name(), "Should be True:", is_user_in_group(sub_child_user, child))
print(sub_child.get_name(), "Should be True:", is_user_in_group(sub_child_user, sub_child))
print(parent.get_name(), "Should be False:", is_user_in_group(sub_child_user_a, parent))