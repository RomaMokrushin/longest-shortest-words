class MinMaxWordFinder:
    def __init__(self):
        self.al = list()

    def add_sentence(self, sen):
        self.al.append(sen.split())

    def shortest_words(self):
        mn = 10000000
        ans = list()
        for i in self.al:
            for j in i:
                if len(j) <= mn:
                    mn = len(j)
        for i in self.al:
            for j in i:
                if len(j) == mn:
                    ans.append(j)
        ans = sorted(ans)
        return ans

    def longest_words(self):
        mx = 0
        ans = list()
        ans1 = list()
        for i in self.al:
            for j in i:
                if len(j) >= mx:
                    mx = len(j)
        for i in self.al:
            for j in i:
                if len(j) == mx:
                    ans.append(j)
        for i in ans:
            if i not in ans1:
                ans1.append(i)
        ans1 = sorted(ans1)
        return ans1


finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('abc')
finder.add_sentence('world')
finder.add_sentence('abc')
finder.add_sentence('def')
finder.add_sentence('asdf')
finder.add_sentence('abc')
finder.add_sentence('qwert')
finder.add_sentence('world')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
