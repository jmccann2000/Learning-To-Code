'''
@brief This module contains unit tests for the FileReader class
'''

# Import the FileReader class definition so we can use it
from lesson000.file_reader import FileReader


class TestFileReader(object):
    ''' Unit tests for the FileReader class. '''

    def setup(self):
        '''
        This setup function is automatically called before each individual test. (It's called by the test runner
        program). This function can be used to perform setup operations shared by the tests.
        '''
        # Let's create a FileReader object to test
        self.file_reader = FileReader()

    def test_load_tokens_from_file_path__does_not_create_empty_tokens(self):
        '''
        This simple test loads tokens from a file containing a few lines followed by a trailing newline.
        The idea with this test is to confirm that the ending newline does not result in an empty token
        being created.
        '''
        # Load tokens from the test file
        tokens = self.file_reader.load_tokens_from_file_path('lesson000/testing/does_not_create_empty_tokens.txt')

        # Check the tokens were created correctly, without a trailing empty token
        assert len(tokens) == 4, "Expected 4 tokens, got %d tokens (tokens=%s)" % (len(tokens), tokens)
        assert tokens[0] == "she", "Expected tokens[0] == 'she', got '%s'" % tokens[0]
        assert tokens[1] == "sells", "Expected tokens[1] == 'sells', got '%s'" % tokens[1]
        assert tokens[2] == "sea", "Expected tokens[2] == 'sea', got '%s'" % tokens[2]
        assert tokens[3] == "shells", "Expected tokens[3] == 'shells', got '%s'" % tokens[3]

    def test_load_tokens_from_file_path__split_on_whitespace(self):
        '''
        This simple test loads tokens from a file containing text separated by whitespace. The idea with this test
        is to confirm that the whitespace separated text will be broken up into separate tokens.
        '''
        # Load tokens from the test file
        tokens = self.file_reader.load_tokens_from_file_path('lesson000/testing/split_on_whitespace.txt')

        # Check the tokens were created correctly, splitting on whitespaces
        assert len(tokens) == 8, "Expected 8 tokens, got %d tokens (tokens=%s)" % (len(tokens), tokens)
        assert tokens[0] == "she", "Expected tokens[0] == 'she', got '%s'" % tokens[0]
        assert tokens[1] == "sells", "Expected tokens[1] == 'sells', got '%s'" % tokens[1]
        assert tokens[2] == "sea", "Expected tokens[2] == 'sea', got '%s'" % tokens[2]
        assert tokens[3] == "shells", "Expected tokens[3] == 'shells', got '%s'" % tokens[3]
        assert tokens[4] == "at", "Expected tokens[4] == 'at', got '%s'" % tokens[4]
        assert tokens[5] == "the", "Expected tokens[5] == 'the', got '%s'" % tokens[5]
        assert tokens[6] == "sea", "Expected tokens[6] == 'sea', got '%s'" % tokens[6]
        assert tokens[7] == "shore", "Expected tokens[7] == 'shore', got '%s'" % tokens[7]

    def test_load_tokens_from_file_path__empty_file(self):
        '''
        This simple test loads tokens from an empty file. The idea with this test is to confirm that the file reader
        does not crash when given an empty file.
        '''
        # Load tokens from the test file
        tokens = self.file_reader.load_tokens_from_file_path('lesson000/testing/empty.txt')

        # Check the tokens were created correctly, splitting on whitespaces
        assert len(tokens) == 0, "Expected 0 tokens, got %d tokens (tokens=%s)" % (len(tokens), tokens)

    def test_load_tokens_from_file_path__single_token(self):
        '''
        This simple test loads tokens from a file containing exactly one token. The idea with this test is to confirm
        that the file reader does not *require* multiple tokens to operate without crashing.
        '''
        # Load tokens from the test file
        tokens = self.file_reader.load_tokens_from_file_path('lesson000/testing/does_not_create_empty_tokens.txt')

        # Check the tokens were created correctly, splitting on whitespaces
        assert len(tokens) == 1, "Expected 1 tokens, got %d tokens (tokens=%s)" % (len(tokens), tokens)
        assert tokens[0] == "BOO", "Expected tokens[0] == 'BOO', got '%s'" % tokens[0]
