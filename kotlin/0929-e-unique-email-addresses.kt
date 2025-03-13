
class Solution {
    fun numUniqueEmails(emails: Array<String>): Int {
        if (emails.size == 1) return 1

        for (i in 0 until emails.size) {
            emails[i] = cleanFormat(emails[i])
        }

        return emails.toSet().size
    }

    fun cleanFormat(email: String): String {
        val parts = email.split('@')
        val local = parts[0]
        var cleanLocal = ""
        for (i in 0 until local.length) {
            if (local[i] == '+') break
            if (local[i] != '.') {
                cleanLocal += local[i]
            }
        }
        val domain = "@"+parts[1]
        return cleanLocal+domain
    }
}