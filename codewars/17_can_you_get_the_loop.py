# def loop_size(node):
#     slow = node.next
#     fast = node.next.next
#     count = 1
#     while slow is not fast:
#         slow = slow.next
#         fast = fast.next.next
#         count +=1
#     return count


def loop_size(node):
    """
    find a point in the loop,any point will do.Since the rabbit moves faster than the turtle and Kata guarantee a loop,
    the rabbit will eventually catch up with the turtle.
    """
    slow = node.next
    fast = node.next.next
    while slow is not fast:
        slow = slow.next
        fast = fast.next.next
    """
    The turtle and rabbit are now in the same node,but we know that node is in a loop.So now we keep the turtle 
    motionless and move the rabbit until it finds turtle again,counting the nodes the rabbit visits in the meas time.
    """
    count = 1
    fast = fast.next
    while slow is not fast:
        count += 1
        fast = fast.next
    return count
