# Count whites in the first window
    whites = s[:k].count('W')
    min_whites = whites
    
    # Sliding window
    for i in range(k, n):
        if s[i - k] == 'W':
            whites -= 1
        if s[i] == 'W':
            whites += 1
        min_whites = min(min_whites, whites)
    
    print(min_whites)
    """
    min_white=s[:k].count('W')
    r=k
    l=0
    while r < n:
        white=s[l:r].count('W')
        min_white=min(white,min_white)  
        r +=1
        l +=1
    print(min_white)
    """