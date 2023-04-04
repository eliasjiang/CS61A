
def tree(root_label,branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
        return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


t = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
# print(label(t))
# for branch in branches(t):
#     print(label(branch))

# def printTree(t):
#     assert is_tree(t),'must be a tree'
#     print(label(t))
#     if is_leaf(t):
#         return
#     for branch in branches(t):
#         printTree(branch)

# printTree(t)

def berry_finder(t):
    print(label(t))
    if(label(t)=='berry'):
        return True
    else:
        for branch in branches(t):
          print(label(branch))
          return berry_finder(branch)
    return False

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    
    
    if is_leaf(t):
        return tree(label(t),[tree(leaf) for leaf in leaves])
    else:
        return tree(label(t),[sprout_leaves(branch,leaves) for branch in branches(t)])


t1 = tree(1, [tree(2), tree(3)])
print_tree(t1)
new1 = sprout_leaves(t1, [4, 5])
print_tree(new1)