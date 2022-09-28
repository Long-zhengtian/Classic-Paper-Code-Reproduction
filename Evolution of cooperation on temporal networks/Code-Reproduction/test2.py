@jit(nopython=True)
def sum_matrix(A):
    N = A.shape[0]
    cnt = 0
    for i in np.arange(N):
        for j in np.arange(N):
            cnt += A[i, j]
    return cnt


@jit(nopython=True)
def sum_vevtor(a):
    N = len(a)
    cnt = 0
    for i in np.arange(N):
        cnt += a[i]
    return cnt



@jit(nopython=True)
def prefer_attach_proportional_to_degree(degrees) :
    choose_array = List()
    length = len(degrees)
    for index in np.arange(length):
        degree = degrees[index]
        if degree != 0:
            for i in np.arange(degree):
                choose_array.append(index)
    length = len(choose_array)
    random_number = randint(0, length - 1)
    choice_node = choose_array[random_number]
    return choice_node


"""
aver_k must be even
"""
@jit(nopython=True)
def scale_free_matrix(N, k):
    static_matrix = np.zeros((N, N), dtype=np.int64)
    for i in np.arange(2*k-1):
        static_matrix[i, i+1] = 1
        static_matrix[i+1, i] = 1
    degrees = np.zeros(N, dtype=np.int64)
    while 1:
        nodex = randint(0, 2*k-1)
        nodey = randint(0, 2*k-1)
        print(nodex,nodey)
        if nodex != nodey:
            static_matrix[nodex, nodey] = 1
            static_matrix[nodey, nodex] = 1
        print(sum_matrix(static_matrix))
        if sum_matrix(static_matrix) == 2*k*k:
            break
    for i in np.arange(N):
        degrees[i] = sum_vevtor(static_matrix[i])
    for i in np.arange(2*k, N):
        while 1:
            choice_node = prefer_attach_proportional_to_degree(degrees)
            static_matrix[i,choice_node] = 1
            static_matrix[choice_node,i] = 1
            print(i,(i+1)*k,k,sum_matrix(static_matrix))
            if sum_matrix(static_matrix) == (i+1)*k:
                print('break')
                break
        for j in np.arange(N):
            degrees[j] = sum_vevtor(static_matrix[j])
    return static_matrix


@jit(nopython=True)
def cycle_matrix(N, k):
    static_matrix = np.zeros((N, N))
    for i in range(N):
        static_matrix[i, (N+i+1+np.arange(int(k/2)))%N] = 1
        static_matrix[i, (N+i+1-np.arange(int(k/2)))%N] = 1
    return static_matrix