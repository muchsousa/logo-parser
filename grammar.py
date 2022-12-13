from lexer import reserved, tokens

from tree import new_leaf, new_node, append_node

from symbols import *
symTable = Symbols()

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV'),
    ('left', 'POW'),
)

def p_program(prod):
    '''
    program : statement other_statement
    '''
    node = new_node("program")
    append_node(node, prod[1])
    if prod[2]:
        append_node(node, prod[2])

    prod[0] = node

def p_other_statement(prod):
    '''
    other_statement : statement other_statement
        | empty 
    '''
    if prod[1]:
        node = new_node("other_statement")
        append_node(node, prod[1])

        if prod[2]:
            append_node(node, prod[2])

        prod[0] = node

def p_statement(prod):
    '''
    statement : instruction 
        | variable_declaration
        | procedure_declaration
        | procedure_call
        | if_then_else 
        | while_loop 
        | write 
    '''
    node = new_node("statement")
    append_node(node, prod[1])

    prod[0] = node

def p_instruction(prod):
    '''
    instruction : FO number_expression 
        | FORWARD number_expression
        | BK number_expression 
        | BACKWARD number_expression
        | RT number_expression 
        | RIGHT expression
        | LT number_expression 
        | LEFT number_expression
        | PD 
        | PENDOWN
        | PU 
        | PENUP
        | WC 
        | WIPECLEAN
        | CS 
        | CLEARSCREEN
        | HOME
        | HEADING
        | TYPEIN
        | SETXY number_expression COMMA number_expression
        | XCOR number_expression
        | YCOR number_expression
    '''

    node = new_node("instruction")

    if prod[1] == "SETXY":
        append_node(node, new_leaf("INSTRUCTION", value=prod[1]))
        append_node(node, new_leaf(prod.slice[2].type, value=prod[2]))
        append_node(node, new_leaf(prod.slice[4].type, value=prod[4]))

       # prod[0] = (reserved[prod[1]], prod[2], prod[4]) 
    elif len(prod) == 3:
        append_node(node, new_leaf("INSTRUCTION", value=prod[1]))
        append_node(node, new_leaf(prod.slice[2].type, value=prod[2]))

        # prod[0] = (reserved[prod[1]], prod[2])
    else:
        append_node(node, new_leaf("INSTRUCTION", value=prod[1]))

        # prod[0] = (reserved[prod[1]])        

    prod[0] = node


def p_variable_declaration(prod):
    '''
    variable_declaration : ID ASSIGN expression
    '''
    symTable.addSymbol(prod[1], "VARIABLE", prod.lineno(1), prod[3])

    node = new_node("variable_declaration")

    append_node(node, new_leaf("ID", value=prod[1]))
    append_node(node, new_leaf(prod.slice[2].type, value=prod[2]))
    append_node(node, prod[3])

    prod[0] = node

def p_variable(prod):
    '''
    variable : COLON ID
    '''
    node = new_node("variable")

    append_node(node, new_leaf("COLON_ID", value=prod[2]))
    prod[0] = node

    # prod[0] = prod[1] + prod[2]

def p_argument_list(prod):
    '''
    argument_list : argument_list COMMA argument
        | argument
    '''
    if len(prod) == 2:
        prod[0] = prod[1]
    else:
        prod[0] = prod[1] + prod[3]
    
def p_argument(prod):
    '''
    argument : expression
        | empty
    '''
    prod[0] = prod[1]

def p_procedure_declaration(prod):
    '''
    procedure_declaration : TO ID argument_list other_statement END
    '''
    args = [prod[3]]
    prod[0] = ('PROCEDURE_DECLARATION', prod[2], {
        'args': args,
        'body': prod[4]
    })

def p_expression_list(prod):
    '''
    expression_list : expression_list COMMA expression 
        | expression 
        | empty
    '''
    if len(prod) == 2:
        prod[0] = prod[1]
    else:
        prod[0] = prod[1] + prod[3]

def p_procedure_call(prod):
    '''
    procedure_call : ID expression_list
    '''
    args = [prod[2]]
    prod[0] = ('PROCEDURE_CALL', prod[1], args)

def p_expression(prod):
    '''
    expression : OPEN_PAR expression CLOSE_PAR
        | boolean_expression
        | number_expression
        | RANDOM
        | string
    '''
    node = new_node("expression")

    if len(prod) == 4: # parentesis
        append_node(node, new_leaf(prod.slice[1].type, value=prod[1]))
        append_node(node, prod[2])
        append_node(node, new_leaf(prod.slice[3].type, value=prod[3]))
    else:
        append_node(node, new_leaf(prod.slice[1].type, value=prod[1]))

    prod[0] = node

def p_number_expression_operation(prod):
    '''
    number_expression : number_expression ADD number_expression
        | number_expression SUB number_expression
        | number_expression MUL number_expression
        | number_expression DIV number_expression
        | number_expression POW number_expression
    '''
    prod[0] = (prod[2], prod[1], prod[3])

def p_number_expression_par(prod):
    '''
    number_expression : OPEN_PAR number_expression CLOSE_PAR
    '''
    node = new_node("number_expression_par")

    append_node(node, new_leaf(prod.slice[1].type, value=prod[1]))
    append_node(node, prod[2])
    append_node(node, new_leaf(prod.slice[3].type, value=prod[3]))

    prod[0] = node

def p_number_expression_variable(prod):
    '''
    number_expression : variable
    '''

    node = new_node("number_expression_variable")

    # if sym is None:
        # prod[0] = ('SYMBOL', prod[1])

        # append_node(node, new_leaf("SYMBOL", value=prod[1]))

        # raise Exception(f"Undefined symbol: {prod[1]}: {prod.lineno(1)}")
    # else:
        # prod[0] = sym["value"]

        #append_node(node, new_leaf("ID", value=prod[1]))
        
    append_node(node, new_leaf("ID", value=prod[1]))

    prod[0] = node

def p_number_expression_num(prod):
    '''
    number_expression : NUM
    '''
    node = new_node("number_expression")
    append_node(node, new_leaf("NUM", value=float(prod[1])))

    prod[0] = node

def p_boolean_expression(prod):
    '''
    boolean_expression : relational_operation 
        | boolean_expression OR boolean_expression
        | boolean_expression AND boolean_expression
        | NOT boolean_expression
        | variable
        | TRUE
        | FALSE
    '''
    node = new_node("boolean_expression")

    if len(prod) == 2:
        append_node(node, prod[1])
    elif len(prod) == 4:
        # prod[0] = (reserved[prod[2]], prod[1], prod[3])

        append_node(node, prod[1])
        append_node(node, new_leaf(prod.slice[2].type, value=prod[2]))
        append_node(node, prod[3])

    elif len(prod) == 3:
        # prod[0] = (reserved[prod[1]], prod[2])

        append_node(node, new_leaf(prod.slice[1].type, value=prod[2]))
        append_node(node, prod[2])

    prod[0] = node

def p_relational_operation(prod):
    '''
    relational_operation : expression GT_OP expression
        | expression LT_OP expression
        | expression GTE_OP expression
        | expression LTE_OP expression
        | expression EQ_OP expression
        | expression NE_OP expression
    '''
    node = new_node("relational_operation")

    append_node(node, prod[1])
    append_node(node, new_leaf(prod.slice[2].type, value=prod[2]))
    append_node(node, prod[3])

    prod[0] = node

def p_if_then_else(prod):
    '''
    if_then_else : IF OPEN_PAR boolean_expression CLOSE_PAR THEN other_statement END
        | IF OPEN_PAR boolean_expression CLOSE_PAR THEN other_statement ELSE other_statement END
    '''

    node = new_node("if_then_else")

    if len(prod) == 10 : # if with else
        append_node(
            node, 
            new_leaf(
                reserved[prod[1]], 
                value=new_leaf(prod.slice[3].type, value=prod[3])
            )
        )
        append_node(
            node, 
            new_leaf(
                reserved[prod[5]], 
                value=new_leaf(prod.slice[6].type, value=prod[6])
            )
        )
        append_node(
            node, 
            new_leaf(
                reserved[prod[7]], 
                value=new_leaf(prod.slice[8].type, value=prod[8])
            )
        )
        append_node(
            node, 
            new_leaf(
                reserved[prod[9]],
                value=new_leaf(prod.slice[8].type, value=prod[8])
            )
        )
        append_node(node, new_leaf(prod.slice[9].type, value=None))

        # prod[0] = (reserved[prod[1]], prod[3], prod[6], reserved[prod[7]], prod[8])
    else:
        append_node(
            node, 
            new_leaf(
                reserved[prod[1]], 
                value=new_leaf(prod.slice[3].type, value=prod[3])
            )
        )
        append_node(
            node, 
            new_leaf(
                reserved[prod[5]], 
                value=new_leaf(prod.slice[6].type, value=prod[6])
            )
        )
        append_node(node, new_leaf(prod.slice[7].type, value=None))

        # prod[0] = (reserved[prod[1]], prod[3], prod[6])

    prod[0] = node


def p_while_loop(prod):
    '''
    while_loop : WHILE OPEN_PAR boolean_expression CLOSE_PAR other_statement END
    '''
    node = new_node("while_loop")

    append_node(
        node, 
        new_leaf(
            reserved[prod[1]], 
            value=new_leaf(prod.slice[3].type, value=prod[3] )
        )
    )
    append_node(
        node, 
        new_leaf(prod.slice[5].type, value=prod[5])
    )
    append_node(node, new_leaf(prod.slice[6].type, value=None))

    prod[0] = node
    # prod[0] = (reserved[prod[1]], prod[3], prod[5])

def p_write(prod):
    '''
    write : WRITE expression 
        | WRITE string
    '''

    node = new_node("write")
    append_node(node, new_leaf(reserved[prod[1]], value=prod[2]))

    prod[0] = node

    # prod[0] = (reserved[prod[1]], prod[2])

def p_empty(prod):
    '''
    empty :
    '''
    prod[0] = None

def p_string(prod):
    '''
    string : STRING
    '''
    node = new_node("string")
    append_node(node, new_leaf(prod.slice[1].type, value=prod[1]))

    prod[0] = node

    # prod[0] = ('STRING', prod[1])

def p_error(token):
    '''
    Provide a simple error message.
    '''
    if token:
        raise Exception(
            f"Unexpected token:{token.lineno}: {token.type}:'{token.value}'"
        )

    raise Exception("Syntax error at EOF.")