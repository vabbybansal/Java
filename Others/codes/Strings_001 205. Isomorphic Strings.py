# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# class Solution(object):
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#
#         # Lengths of strings should be same
#         if len(s) != len(t):
#             return False
#
#         # Map character freq
#         s_char_freq_map = dict()
#         t_char_freq_map = dict()
#         s_char_freq_map_len = 0
#         t_char_freq_map_len = 0
#
#
#         for elm in s:
#             if elm not in s_char_freq_map:
#                 s_char_freq_map[elm] = 0
#                 s_char_freq_map_len += 1
#             s_char_freq_map[elm] += 1
#         for elm in t:
#             if elm not in t_char_freq_map:
#                 t_char_freq_map[elm] = 0
#                 t_char_freq_map_len += 1
#             t_char_freq_map[elm] += 1
#
#         # Since number of distinct characters should be the same in both the string, length of char_freq_maps should be the same
#         if s_char_freq_map_len != t_char_freq_map_len:
#             return False
#
#         # Create freq map of char freq
#         s_char_freq_map_freq_map = dict()
#         t_char_freq_map_freq_map = dict()
#         s_char_freq_map_freq_map_len = 0
#         t_char_freq_map_freq_map_len = 0
#
#         for elm in s_char_freq_map.values():
#             if elm not in s_char_freq_map_freq_map:
#                 s_char_freq_map_freq_map[elm] = 0
#                 s_char_freq_map_freq_map_len += 1
#             s_char_freq_map_freq_map[elm] += 1
#
#         for elm in t_char_freq_map.values():
#             if elm not in t_char_freq_map_freq_map:
#                 t_char_freq_map_freq_map[elm] = 0
#                 t_char_freq_map_freq_map_len += 1
#             t_char_freq_map_freq_map[elm] += 1
#
#         # Since number of chharacters with the same freq count should be the same as well, length of freqfreq maps should be the same as well
#         if s_char_freq_map_freq_map_len != t_char_freq_map_freq_map_len:
#             return False
#
#         # Finally, the number of characters with same freq should be the same
#         for key in s_char_freq_map_freq_map:
#             if s_char_freq_map_freq_map[key] != t_char_freq_map_freq_map[key]:
#                 return False
#
#         # If the code reaches here, means all checks were fine and return True
#         return True


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_map = {}
        t_set = set()

        # Iterate all indices one by one
        for i in range(len(s)):

            # If char at index in s already in map, simply check if the corresponding one in t is same as that in map
            if s[i] in s_map:
                if t[i] != s_map[s[i]]:
                    return False
            # If not
            else:
                # Check if char in t is already taken. If yes, then not isomorphic as a char can be mapped to only one char
                if t[i] in t_set:
                    return False
                # Else create a mapping
                else:
                    s_map[s[i]] = t[i]
                    t_set.add(t[i])
        # if code reaches here, it means the strings are isomorphic
        return True


obj = Solution()
print obj.isIsomorphic("paper", "title")