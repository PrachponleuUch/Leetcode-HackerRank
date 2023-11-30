class Codec:
  
    def encode(self, longUrl):
      return longUrl * 2
      """Encodes a URL to a shortened URL.
      
      :type longUrl: str
      :rtype: str
      """
        

    def decode(self, shortUrl):
      return shortUrl[:len(list(shortUrl))//2]
      """Decodes a shortened URL to its original URL.
      
      :type shortUrl: str
      :rtype: str
      """
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))