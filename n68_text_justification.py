from typing import List

import pytest

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth
# characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does
# not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # make word lines
        word_lines: List[List[str]] = []
        word_lines_width: List[int] = []
        line_nmb, line_width = 0, 0

        word_lines.append([])
        for word in words:
            if not word_lines[line_nmb]:
                word_lines[line_nmb].append(word)
                word_lines_width.append(len(word))
                line_width = len(word)
            else:
                if line_width + 1 + len(word) <= maxWidth:
                    word_lines[line_nmb].append(word)
                    word_lines_width[line_nmb] += len(word)
                    line_width += len(word) + 1
                else:
                    line_nmb += 1
                    word_lines.append([])
                    word_lines[line_nmb].append(word)
                    word_lines_width.append(len(word))
                    line_width = len(word)

        # full justification for all lines except for the last
        lines = []
        for i in range(len(word_lines) - 1):
            lines.append("")
            lines[i] += word_lines[i][0]
            if len(word_lines[i]) == 1:
                lines[i] += ' ' * (maxWidth - len(lines[i]))
            else:
                first_words = (maxWidth - word_lines_width[i]) % (len(word_lines[i]) - 1)
                first_words_spaces = (maxWidth - word_lines_width[i]) // (len(word_lines[i]) - 1) + 1
                second_words = len(word_lines[i]) - first_words - 1
                second_words_spaces = first_words_spaces - 1

                for j in range(first_words):
                    lines[i] += ' ' * first_words_spaces
                    lines[i] += word_lines[i][j + 1]

                for j in range(second_words):
                    lines[i] += ' ' * second_words_spaces
                    lines[i] += word_lines[i][j + 1 + first_words]

        lines.append(word_lines[-1][0])
        for word in word_lines[-1][1:]:
            lines[-1] += ' '
            lines[-1] += word
        lines[-1] += ' ' * (maxWidth - len(lines[-1]))

        return lines


@pytest.mark.parametrize('words, maxWidth, res', [
    (["This", "is", "an", "example", "of", "text", "justification."], 16, [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]),
    (["What","must","be","acknowledgment","shall","be"], 16, [
         "What   must   be",
         "acknowledgment  ",
         "shall be        "
     ]),
    (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is",
      "everything","else","we","do"], 20, [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]),
])
def test_full_justification(words: List[str], maxWidth: int, res: List[str]):
    assert Solution().fullJustify(words, maxWidth) == res