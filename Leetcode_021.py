#Leetcode 21 Merge Two Sorted List
#input: [1, 2, 4], [1, 3, 4] / output: [1, 1, 2, 3, 4, 4]

def mergeTwoLists2(self, list1, list2):
    if not list1 or not list2:
        return list1 or list2
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
