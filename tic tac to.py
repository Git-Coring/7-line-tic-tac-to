ttt_list = [" "," "," "," "," "," "," "," "," ","O","X"]
for a in range(9):
    ttt_list[int(input("\nChoose player {} number 1 ~ 9 >>>".format(ttt_list[9+a%2]))) - 1] = ttt_list[9+a%2]
    print("\n{}\nI {} I {} I {} I\n{}\nI {} I {} I {} I\n{}\nI {} I {} I {} I\n{}".format("-"*14, ttt_list[0], ttt_list[1],ttt_list[2],"-"*14,ttt_list[3],ttt_list[4],ttt_list[5],"-"*14,ttt_list[6],ttt_list[7],ttt_list[8],"-"*14))
    if ttt_list[0] == ttt_list[9+a%2] and ttt_list[0] == ttt_list[4] and ttt_list[4] == ttt_list[8] or ttt_list[0] == ttt_list[9+a%2] and ttt_list[0] == ttt_list[1] and ttt_list[1] == ttt_list[2] or ttt_list[3] == ttt_list[9+a%2] and ttt_list[3] == ttt_list[4] and ttt_list[4] == ttt_list[5] or ttt_list[6] == ttt_list[9+a%2] and ttt_list[6] == ttt_list[7] and ttt_list[7] == ttt_list[8] or  ttt_list[2] == ttt_list[9+a%2] and ttt_list[2] == ttt_list[4] and ttt_list[2] == ttt_list[6] or tt_list[0] == ttt_list[9+a%2] and ttt_list[0] == ttt_list[3] and ttt_list[3] == ttt_list[6] or ttt_list[1] == ttt_list[9+a%2] and ttt_list[1] == ttt_list[4] and ttt_list[4] == ttt_list[7] or ttt_list[2] == ttt_list[9+a%2] and ttt_list[2] == ttt_list[5] and ttt_list[5] == ttt_list[8]:
        print("\nPlayer {} Win!\n".format(ttt_list[9+a%2]))
        break
