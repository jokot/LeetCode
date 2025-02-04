// https://leetcode.com/problems/guess-number-higher-or-lower/

/** 
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * fun guess(num:Int):Int {}
 */

 class Solution:GuessGame() {
    override fun guessNumber(n:Int):Int {
        return guessHelper(1, n)
    }

    fun guessHelper(left: Int, right: Int): Int {
        val pick = left + (right - left) / 2
        return when(guess(pick)) {
            -1 -> guessHelper(left, pick - 1)
            1 -> guessHelper(pick + 1, right)
            else -> pick
        }
    }
}