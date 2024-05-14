// TODO
// 1. print_random_letter should not print spaces (should it?)

// STRAT
// [DONE] 1. Print a word
// [DONE] 2. Return a random letter from <word>, print <letter>
// [DONE] 3. Return N random letters from <word>, where <N> == <len(word)>
// [DONE] 4. Reduce the source for <letter> by 1 each time [Retro: 3/4 can be implemented in 1 step]
// [DONE] 5. Remove the specific letter that was randomly chosen from the pool of letters to choose from
// 6. For sentences, respect the position of spaces (should this be a requirement?)
// 7. Re-capitalize letters (L -> U && U -> L) where appropriate
// 8. TESTS! [This should be requirement #1]
//	- How many iterations does it take for the program to turn "Tom Malvolo Riddle" into "I am Lord Voldemort"?

package main

import (
	"bytes"
	"fmt"
	"math/rand"
	"time"
	"os"
)

func remove_letter_from_word(word string, letter byte) string {
	out := bytes.NewBufferString("")
	removed := false
	for i := 0; i < len(word); i++ {
		if (word[i] != letter) {
			out.WriteByte(word[i])
		} else if (word[i] == letter && removed == true) {
			out.WriteByte(word[i])
		} else {
			removed = true
		}
	}
	return out.String()
}

func random_letter(word string) byte {
	return word[rand.Intn(len(word))]
}

func n_random_letters(word string, n int) string {
	out := bytes.NewBufferString("")
	for i := 0; i < n; i++ {
		letter := random_letter(word)
		out.WriteByte(letter)
		word = remove_letter_from_word(word, letter)
	}
	return out.String()
}


func main() {
	rand.Seed(time.Now().UnixNano())
	word := os.Args[1]
	anagram := n_random_letters(word, len(word))
	fmt.Printf("Your word:\t%s\t(Length: %d)\n", word, len(word))
	fmt.Printf("Anagram:\t%s\t(Length: %d)\n", anagram, len(anagram))
}