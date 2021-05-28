
def identity():

    for i in range(15):
        for j in range(15):
            if j == i:
                identity_mat[i][j] = 1


def matMulti(matrix, base):

    m2 = [[0 for i in range(15)] for j in range(15)]
    for i in range(0, d):
        for k in range(0, d):
            for j in range(0, d):
                m2[i][k] += (matrix[i][j] * base[j][k])
                m2[i][k] %= m
    return m2


def power(base, exponent):
    remaining_multiplicand = identity_mat
    result = base

    while exponent > 1:
        remainder = exponent % 2
        if remainder > 0:
            remaining_multiplicand = matMulti(remaining_multiplicand, result)
        exponent = (exponent - remainder) / 2
        result = matMulti(result, result)

    return matMulti(result, remaining_multiplicand)


def answer(d, n, m, matrix, vector):
    aux_matrix = power(matrix, n)

    # for i in range(d):
    # print()
    # for j in range(d):
    #print(aux_matrix[i][j],end=" ")

    ans = 0

    for i in range(d):
        ans += aux_matrix[d-1][i]*vector[i]
    return(ans % m)


if __name__ == "__main__":

    identity_mat = [[0 for i in range(15)] for j in range(15)]
    identity()
    matrix_op = [[0 for i in range(15)] for j in range(15)]

    while True:
      d, n, m = input().split(" ")

      if d == n == m == '0':
        break

      last_fill = list(map(int, input().split(' ')))
      cocientes = list(map(int, input().split(' ')))
      empty_l = input()
      last_fill = last_fill[::-1]

      d = int(d)
      n = int(n)
      m = int(m)
      if n <= d:
          print(n)
      else:
          for i in range(d-1):
              for j in range(d):
                  if (i+1 == j):
                      matrix_op[i][j] = 1
                  else:
                      matrix_op[i][j] = 0

          for k in range(d):
              matrix_op[d-1][k] = last_fill[k]
          print(answer(d, n-d, m, matrix_op, cocientes))
