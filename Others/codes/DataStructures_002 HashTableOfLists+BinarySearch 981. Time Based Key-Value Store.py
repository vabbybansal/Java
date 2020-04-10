# Hash Table of Lists
# 2 design choices could be used
#   1) HashTable of Lists:
#       set - O(1) {since times[secondary key] are inserted in strictly increasing order, we just need to append the element at the end of the list of the key in hashtable}
#       get - O(log(m)) where m are the total number of elements (timestamps) for a give key. We use binary search since the time elements would already be sorted {inserted in strictly increasing manner}
#   2) HashTable of HashTable
#       set - O(1) here for each primary 'key', our time will also be another key of a hashtable stored at the primary hash
#       get - O(mlogm) since we would need to sort the secondary hash table and then get the element
#           For get, the problem here is that we do not use the fact that the insertions are in a strictly increasing fashion, which is used by the first design, hence faster




# Create a timebased key-value store class TimeMap, that supports two operations.
#
# 1. set(string key, string value, int timestamp)
#
# Stores the key and value, along with the given timestamp.
# 2. get(string key, int timestamp)
#
# Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
#     If there are multiple such values, it returns the one with the largest timestamp_prev.
# If there are no values, it returns the empty string ("").
#
#
# Example 1:
#
# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:
# TimeMap kv;
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
# kv.get("foo", 1);  // output "bar"
# kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
# kv.set("foo", "bar2", 4);
# kv.get("foo", 4); // output "bar2"
# kv.get("foo", 5); //output "bar2"


class TimeMap(object):

    # Not here as this should not be a static variable since different objects of this class will have their own different hashtable
    # firstAccessHashTable = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # first level key goes here
        self.firstAccessHashTable = {}




    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.firstAccessHashTable:
            # create 2-D lists for each second level key {first list for timestamps which can be binary searched upon, and second for value}
            self.firstAccessHashTable[key] = [[], []]

        # Since the timestamps are inserted in a strictly increasing fashion, we simply append the new values in the list
        # Append timestamp
        self.firstAccessHashTable[key][0].append(timestamp)
        # Append value
        self.firstAccessHashTable[key][1].append(value)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        # if key itself is not present, return empty string
        if key not in self.firstAccessHashTable:
            return ""

        increasingTimestampsList = self.firstAccessHashTable[key][0]
        # To get the value, we first do binary search within the timestamps list to get that or the smaller timestamp
        # This is possible since the lists are sorted because the insertions are done in a strictly increasing order

        pivotIndexBinarySearch = self.binarySearchLessThanListDriver(increasingTimestampsList, timestamp)
        if pivotIndexBinarySearch >= 0:
            return self.firstAccessHashTable[key][1][pivotIndexBinarySearch]
        else:
            return ""

    def binarySearchLessThanListDriver(self, theList, numberTOFind):

        # start the binary search program using the main method
        return self.binarySearchLessThanList(theList, numberTOFind, 0, len(theList)-1)

    def binarySearchLessThanList(self, theList, numberTOFind, virtualStartIndex, virtualEndIndex):

        lenList = virtualEndIndex - virtualStartIndex + 1
        pivot = int((virtualEndIndex + virtualStartIndex) /2)

        pivotElm = theList[pivot]
        if lenList == 0:
            return pivot

        if pivotElm == numberTOFind:
            return pivot

        # number less than pivot, number in first half
        if numberTOFind < pivotElm:
            return self.binarySearchLessThanList(theList, numberTOFind, virtualStartIndex, pivot-1)
        # else, number in second half
        else:
            return self.binarySearchLessThanList(theList, numberTOFind, pivot+1, virtualEndIndex)



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set(1,'a',5)
obj.set(1,'b',10)
obj.set(1,'c',20)
obj.set(1,'d',30)
obj.set(1,'e',40)
obj.set(1,'f',50)
obj.set(1,'g',60)
obj.set(1,'h',70)

# param_2 = obj.get(key,timestamp)
print obj.get(1,5)