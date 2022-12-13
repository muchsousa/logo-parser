reserved = {
    'fo': 'FO',
    'forward': 'FORWARD',
    # --
    'bk': 'BK',
    'backward': 'BACKWARD',
    # --
    'rt': 'RT',
    'right': 'RIGHT',
    # --
    'lt': 'LT',
    'left': 'LEFT',
    # --
    'pu': 'PU',
    'penup': 'PENUP',
    # --
    'pd': 'PD',
    'pendown': 'PENDOWN',
    # --
    'wc': 'WC',
    'wipeclean': 'WIPECLEAN',
    # --
    'cs': 'CS',
    'clearscreen': 'CLEARSCREEN',
    # --
    'home': 'HOME',
    'setxy': 'SETXY',
    'xcor': 'XCOR',
    'ycor': 'YCOR',
    'heading': 'HEADING',
    'random': 'RANDOM',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'end': 'END',
    'while': 'WHILE',
    'write': 'WRITE',
    'typein': 'TYPEIN',
    'to': 'TO',
    'or': 'OR',
    'and': 'AND',
    'not': 'NOT',
    'true': 'TRUE',
    'false': 'FALSE'
}

tokens = [
    "OPEN_PAR", "CLOSE_PAR",
    "ADD", "SUB", "MUL", "DIV", "POW",
    "GT_OP", "LT_OP", "GTE_OP", "LTE_OP", "EQ_OP", "NE_OP",
    "COMMA", "COLON", "ASSIGN", "STRING",
    "ID", "NUM"
] + list(reserved.values())

# -----------------------------------------------

t_ignore = " \t\r"          # will be ignored by lexer
t_ignore_COMMENT = r'\#.*'  # will ignore comments

t_OPEN_PAR = r'\('
t_CLOSE_PAR = r'\)'

t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_POW = r'\^'

t_GT_OP = r'>'
t_LT_OP = r'<'
t_GTE_OP = r'>='
t_LTE_OP = r'<='
t_EQ_OP = r'=='
t_NE_OP = r'<>'

t_COMMA = r','
t_COLON = r':'
t_ASSIGN = r'='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') # Check for reserved words
    return t

def t_NUM(t):
    r'[+-]?(\d+(\.\d*)?|\.\d+)(e\d+)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'("[a-zA-Z0-9, ]*")|(\'[a-zA-Z0-9, ]*\')'
    t.value = t.value.replace('"', '')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)