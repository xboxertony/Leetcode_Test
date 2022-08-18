class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ancestors = [set() for _ in range(n)]

        ### 條列式所有的入度 list，得知目前每一個頂點v，有多少頂點連接
        indices = [0] * n

        ### 整理每一個頂點v，走一步能抵達多少的頂點集合
        edge_mapping = [[] for _ in range(n)]

        ### 目前祖先的集合
        q = deque([])

        for u, v in edges:
            edge_mapping[u].append(v)
            indices[v] += 1

        ### 先利用入度=0為祖先的特點，收集第一波的祖先
        for i in range(n):
            if indices[i] == 0:
                q.append(i)

        while q:
            begin = q.popleft()
            for v in edge_mapping[begin]:
                ancestors[v].add(begin)
                ancestors[v].update(ancestors[begin])
                indices[v] -= 1
                ### 進行後續幾波的祖先更新，只要入度為0，就是下一個祖先
                if indices[v] == 0:
                    q.append(v)

        return [sorted(list(i)) for i in ancestors]