####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Setbacks' # Only 10 chars displayed.
strategy_name = 'Survival'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0:
        return 'b'
    elif my_history[-1] == 'b' and their_history[-1] == 'b':
        return 'b'
    else:
        return 'c'
       