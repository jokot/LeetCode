// https://leetcode.com/problems/roman-to-integer
class Solution {
    fun romanToInt(s: String): Int {

        var number = 0
        var prev = 'Z'

        for (c in s) {
            when(c) {
                'I' -> {
                    number += 1
                }

                'V' -> if(prev == 'I') {
                    number += 3
                } else {
                    number += 5
                }

                'X' -> if(prev == 'I') {
                    number += 8
                } else {
                    number += 10
                }

                'L' -> if(prev == 'X') {
                    number += 30
                } else {
                    number += 50
                }

                'C' -> if(prev == 'X') {
                    number += 80
                } else {
                    number += 100
                }

                'D' -> if(prev == 'C') {
                    number += 300
                } else {
                    number += 500
                }

                'M' -> if(prev == 'C') {
                    number += 800
                } else {
                    number += 1000
                }
            }

            prev = c
        }

        return number
    }
}