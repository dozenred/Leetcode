import sys
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
a = list(map(lambda x: int(x), int(sys.stdin.readline().strip().split())))
def test():
    while True:
        try:
            n = int(sys.stdin.readline().strip() )
            childdic = dict()
            fatherdic = {str(_):[] for _ in range(n)}
            for i in range(n-1):
                f,c = sys.stdin.readline().strip().split()
                childdic[c]=f
                fatherdic[f].append(c)
            head=None
            for father in fatherdic.keys():
                if father not in childdic:
                    head = father
                    break
            height=1
            q=fatherdic[head]
            while q:
                new_q = []
                for i in range(len(q)):
                    node = q.pop(0)
                    new_q.extend(fatherdic[node])
                height+=1
                q=new_q
            print(height)
        except: break

if __name__ == '__main__':
    test()

