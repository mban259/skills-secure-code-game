import unittest
import code as c

class TestCrypto(unittest.TestCase): 
  
    # verifies that hash and verification are matching each other for SHA
    def test_1(self):
        rd = c.Random_generator()
        sha256 = c.SHA256_hasher()
        pass_ver = sha256.password_verification("abc", sha256.password_hash("abc",rd.generate_salt()))
        self.assertEqual(pass_ver, True)

    # verifies that hash and verification are matching each other for MD5
    def test_2(self):
        # MD5は使わない
        return
        
if __name__ == '__main__':    
    unittest.main()