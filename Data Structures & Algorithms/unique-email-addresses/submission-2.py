class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            my_index = emails[i].index('@')
            local_part = emails[i][:my_index]
            domain_part = emails[i][my_index:]

            clean_local = ""
            for char in local_part:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    clean_local+= char

            emails[i] = clean_local+domain_part
        count = Counter(emails)
        return len(count)
