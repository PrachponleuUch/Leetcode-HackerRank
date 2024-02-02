class Solution(object):
    def suggestedProducts(self, products, searchWord):
        ans = []
        for i in range(1, len(searchWord) + 1):
            block = []
            for product in products:
                if searchWord[:i] in product[:i]:
                    block.append(product)
            block.sort()
            if len(block) > 3:
                block = block[:3]
            ans.append(block)
        if not ans: ans = products.sort()
        return ans
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        