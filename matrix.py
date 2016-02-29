import math

def make_translate( x, y, z ):
    translate_matrix = new_matrix()
    ident(translate_matrix)
    translate_matrix[3][0] = x
    translate_matrix[3][1] = y
    translate_matrix[3][2] = z
    return translate_matrix

def make_scale( x, y, z ):
    scale_matrix = new_matrix()
    ident(scale_matrix)
    scale_matrix[0][0] = x
    scale_matrix[1][1] = y
    scale_matrix[2][2] = z
    return scale_matrix

def make_rotX( theta ):
    rotX_matrix = new_matrix()
    ident(rotX_matrix)
    degrees = math.radians(theta)
    rotX_matrix[1][1] = math.cos(degrees)
    rotX_matrix[2][1] = -1*math.sin(degrees)
    rotX_matrix[1][2] = math.sin(degrees)
    rotX_matrix[2][2] = math.cos(degrees)
    return rotX_matrix

def make_rotY( theta ):
    rotY_matrix = new_matrix()
    ident(rotY_matrix)
    degrees = math.radians(theta)
    rotY_matrix[0][0] = math.cos(degrees)
    rotY_matrix[1][0] = -1*math.sin(degrees)
    rotY_matrix[0][1] = math.sin(degrees)
    rotY_matrix[1][1] = math.cos(degrees)
    return rotY_matrix

def make_rotZ( theta ):
    rotZ_matrix = new_matrix()
    ident(rotZ_matrix)
    degrees = math.radians(theta)
    rotZ_matrix[0][0] = math.cos(degrees)
    rotZ_matrix[2][0] = -1*math.sin(degrees)
    rotZ_matrix[0][2] = math.sin(degrees)
    rotZ_matrix[2][2] = math.cos(degrees)
    return rotZ_matrix

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    output = ""
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            output += '{:6}'.format("{:.5}".format(str(matrix[x][y])))
        output += "\n"
    print output

def ident( matrix ):
    for x in range(len(matrix)):
        matrix[x][x] = 1

def scalar_mult( matrix, x ):
    for col in range(len(matrix)):
        for row in range(3):
            matrix[col][row] *= x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = m2
    for y1 in range(len(m1[0])):
        for x2 in range(len(temp)):
            temp_sum = 0
            for x in range(len(m1)):
                temp_sum += m1[x][y1] * temp[x2][x]
            m2[x2][y1] = temp_sum
