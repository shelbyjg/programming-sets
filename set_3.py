def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    n=len(board)
    for i in range(n):
        if len(set(board[i])) == 1 and board[i][0] != '':
            return board[i][0]
    for i in range(n):
        if len(set(row[i] for row in board)) == 1 and board[0][i] != '':
            return board[0][i]
    if len(set(board[i][i] for i in range(n))) == 1 and board[0][0]!='':
        return board[0][0]
    if len(set(board[i][n-i-1] for i in range(n))) == 1 and board[0][n-1]!='':
        return board[0][n-1]    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_travel_time = 0

    while current_stop != second_stop:
        for (from_stop, to_stop), travel_time in route_map.items():
            if from_stop == current_stop:
                total_travel_time += travel_time["travel_time_mins"]
                current_stop = to_stop
                break
    return total_travel_time
    
