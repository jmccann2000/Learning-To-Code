'''
@brief This module contains the FileReader class, which provides the basic functionality for reading a code file
    and decomposing it into its whitespace separated tokens.
'''


class FileReader(object):


    def load_tokens_from_file_path(self, file_path):
        '''
        This function reads in the contents of the file at file_path, decomposing that files contents into
        a list of tokens. A token is any continuous sequence of non-whitespace characters separated from other
        tokens by a whitespace.

        @param file_path File path of the code module to read in
        @returns A list of tokens (strings) comprising the contents of the file
        '''
        tokens=[]
        with open(file_path, "r") as read:
            bigline= " ".join(line.strip() for line in read)
            tokens = bigline.split()
            print(tokens)
        return tokens
