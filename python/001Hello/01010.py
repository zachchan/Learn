
"""

二进制转换十进制

 128 64 32 16 8 4 2 1   (计算方法：够减就是1，不够减就是0。直到数字变成0)
  0  0  0  0  5 1 0 1
60  -> 0 0 1 1 1 1 0 0
13  -> 0 0 0 0 1 1 0 1


位运算

（and &） （上下都为真则为真 反之为假）
60 & 13 =  0   0   0   0   1   1   0   0
        =  0 + 0 + 0 + 0 + 8 + 4 + 0 + 0
        = 12

（or |） （上下有一个为真则为真 反之为假）
60 | 13 = 0   0   1    1    1   1   0   1
         = 0 + 0 + 32 + 16 + 8 + 4 + 0 + 1
         = 61

( ^ 异或运算) （上下同真（同假）则为假 反之为真）
60 ^ 13  = 0   0    1   1    0   0   0   1
         = 0 + 0 + 32 + 16 + 0 + 0 + 0 + 1
         = 49

(~ 按位取反运算)
（32位计算机中的存储实际上8位，
    在计算机中首位为符号位，是0表示正数，
        是1表示负数，即是求补码的逆，
            步骤：先取反  若为负数先减1，再取反，取反时符号位不变）
 60 = 0     0    1    1    1   1   0   0
~60 = 1     1    0    0    0   0   1   1 （取反）
      1     1    0    0    0   0   1   0 （首位是1为负数 需要减1）
      1     0    1    1    1   1   0   1 （再取反，符号位不变）
      - （  0  + 32 + 16 + 8 + 4 + 0 + 1 ） （转化为十进制）
    = -61

(>> 右移) (二进制向右移，右移1位，就是十进制除以2，右移2位，就是十进制除以4...)
 60      = 0     0    1    1    1   1   0   0
 60 >> 1 = 0     0    0    1    1   1   1   0
         = 60 / 2
         = 30

(<< 左移) (二进制向左移，左移1位，就是十进制乘以2，左移2位，就是十进制乘以4...)
 60      = 0     0    1    1    1   1   0   0
 60 << 1 = 0     1    1    1    1   0   0   0
         = 60 * 2
         = 120


注：二进制运算提高性能
"""

#练习
#22 = 00010110
#56 = 00111000

#22 and 56 = 00010000 = 16
#22 or 56  = 00111110 = 62

#22 ^ 56   = 00101110 = 46

#~ 22  = 11101001
#      = 11101000
#      = 10010111
#      = -23
#~ 56  = 11000111
#      = 11000110
#      = 10111001
#      =-57

#22>>1 = 22/2 =11
#22<<1 = 22*2 =44

#56>>1 = 56/2 =28
#56<<1 = 56*2 =112
