import re


class Analizador:
    lin_num = 1

    def tokenize(self, code, reserv):

        rules = [
            ('Reservados', r'(' + reserv + ')'),                 # RESERVADOS          
            ('Operacao', r'\b(\+|\-|\*|\^|\=|\:|\=)\b'),         # OPER
            ('Variavel', r'[a-zA-Z]\w*'),                        # VARS
            ('Float', r'\d(\d)*\.\d(\d)*'),                      # FLOAT
            ('Int', r'\d(\d)*'),                                 # INT
            ('UNKNOWN', r'.'),                                   # UNKNOWN
            ('NEWLINE', r'\n'),        
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        token = []
        lexeme = []
        row = []
        column = []

        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                lin_start = m.end()
                self.lin_num += 1

            else:
                col = m.start() - lin_start
                column.append(col)
                token.append(token_type)
                lexeme.append(token_lexeme)
                row.append(self.lin_num)
                
                if token_lexeme != '' and token_lexeme != ' ':
                    print('Token = {0}, Lexema = \'{1}\' '.format(token_type, token_lexeme))

        return token, lexeme, row, column
