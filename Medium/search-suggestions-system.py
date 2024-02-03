class Solution(object):
    def suggestedProducts(self, products, searchWord):
        ans = []
        products.sort()
        for i in range(1, len(searchWord) + 1):
            block = []
            for product in products:
                if searchWord[:i] in product[:i]:
                    block.append(product)
            products = block
            ans.append(block[:3])
        return ans
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        