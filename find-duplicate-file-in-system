class Solution:
    def findDuplicate(self, paths):
        content = defaultdict(list)
        for path in paths:
            parts = path.split()
            for i in range(1, len(parts)):
                file = parts[i]
                name, _, text = file.partition("(")
                content[text[:-1]].append(parts[0] + "/" + name)
        return [x for x in content.values() if len(x) > 1]
