class Solution:
    def simplifyPath(self, path: str) -> str:
        flo = path.split('/')
        stac = []
        for it in flo:
            if it =='..' and len(stac) > 0:
                stac.pop()
            elif it != '.' and it != '' and it != '..':
                stac.append(it)
        return '/' + '/'.join(stac)
  