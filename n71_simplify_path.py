class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        path = []
        for dir in dirs:
            if not dir or dir == '.':
                continue
            elif dir == '..':
                if path:
                    path.pop()
            else:
                path.append(dir)

        return "/" + "/".join(path)


def test_simplify_path():
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"
    assert Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
    assert Solution().simplifyPath("/../") == "/"
    assert Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
