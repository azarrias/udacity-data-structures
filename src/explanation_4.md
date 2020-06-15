# Problem 4: Active Directory
## Time complexity
Time complexity depends on the number of groups below the group in the active directory's tree hierarchy.
Worst case complexity involves traversing a tree, which is O(n) where n is the number of nodes.
It also involves searching for the user in each node until it is found, which is also O(n) where n is the number of users registered to each group.
So, complexity of the whole search would be O(n^2) in a worst-case scenario.
## Space complexity
Space complexity is linear O(n), since the implementation is recursive, and needs to keep track of the number of subnodes under the input group.