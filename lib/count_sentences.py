#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        self.value = value  # Uses the setter to validate input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # Print instead of raising an error

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        """Returns the number of sentences in the string."""
        if not self._value:
            return 0  # Return 0 for empty string

        sentences = re.split(r'[.!?]+', self._value)  # Split on sentence-ending punctuation
        sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty strings
        
        return len(sentences)  # Return the count of sentences

# Example usage:
simple_string = MyString("one. two. three?")
print(simple_string.count_sentences())  # Should print 3
