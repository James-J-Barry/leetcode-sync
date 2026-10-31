class Solution:
    def simplifyPath(self, path: str) -> str:
        pathparts = path.split('/')
        pathparts = [item for item in pathparts if item != '' and item != '.']
        newpath = []
        for item in pathparts:
            if item == '..':
                if newpath:
                    newpath.pop()
            else:
                newpath.append(item)
        return '/' + '/'.join(newpath)
