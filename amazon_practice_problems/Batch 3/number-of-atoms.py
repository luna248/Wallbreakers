class Solution:
    def countOfAtoms(self, formula):
        #using regular expression to get to the solution
        pattern = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        elementCounts = [collections.Counter()]

        for elementName, firstCount, openParen, closeParen, secondCount in pattern:
            if elementName:
              elementCounts[-1][elementName] += int(firstCount or 1)
            if openParen:
              elementCounts.append(collections.Counter())
            if closeParen:
                top = elementCounts.pop()
                for i in top:
                  elementCounts[-1][i] += top[i] * int(secondCount or 1)

        return "".join(elementName + (str(elementCounts[-1][elementName]) if elementCounts[-1][elementName] > 1 else '')
                       for elementName in sorted(elementCounts[-1]))
