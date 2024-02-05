import unittest

def count_names_exceeding_length(prenoms: list[str]) -> int:
    """
    Count the number of names exceeding a specific length.

    :param prenoms: List of names.
    :return: Count of names longer than the specified length.
    """
    NUMBER_OF_LETTERS = 7
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > NUMBER_OF_LETTERS:
            more_than_seven += 1
            print(f"Prenom supérieur à {NUMBER_OF_LETTERS} : {prenom}")
        else:
            print(f"Prenom inférieur ou égal à {NUMBER_OF_LETTERS} : {prenom}")
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
    def test_names(self) -> None:
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_names_exceeding_length(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()