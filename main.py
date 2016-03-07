from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
edge_matrix = new_matrix(0, 0)

add_edge(edge_matrix, 0, 0, 0, 50, 0, 0)
add_edge(edge_matrix, 0, 0, 0, 0, 50, 0)
add_edge(edge_matrix, 50, 0, 0, 50, 50, 0)
add_edge(edge_matrix, 0, 50, 0, 50, 50, 0)
draw_lines(edge_matrix, screen, color)
for x in range(1000):
    translate_matrix = make_translate(10, 10, 0)
    rotX_matrix = make_rotX(7)
    rotY_matrix = make_rotY(7)
    matrix_mult(rotX_matrix, edge_matrix)
    matrix_mult(rotY_matrix, edge_matrix)
    matrix_mult(translate_matrix, edge_matrix)
    draw_lines(edge_matrix, screen, color);


# ident_matrix = new_matrix()
# ident(ident_matrix)
# translate_matrix = make_translate(5, 6, 8)
# scale_matrix = make_scale(3, 2, 7)
# rotX_matrix = make_rotX(60)
# rotY_matrix = make_rotY(60)
# rotZ_matrix = make_rotZ(60)
#
# # draw shape
# add_edge(edge_matrix, 0, 0, 0, 499, 499, 0)
# add_edge(edge_matrix, 499, 0, 0, 0, 499, 0)
# add_edge(edge_matrix, 200, 300, 0, 80, 400, 0)
# draw_lines(edge_matrix, screen, color)
#
# # scalar multiplication
# scalar_mult(edge_matrix, 5)
#
# print("edge matrix")
# print_matrix(edge_matrix)
# print("identitiy matrix")
# print_matrix(ident_matrix)
# print("translate matrix")
# print_matrix(translate_matrix)
# print("scale matrix")
# print_matrix(scale_matrix)
# print("rotX matrix")
# print_matrix(rotX_matrix)
# print("rotY matrix")
# print_matrix(rotY_matrix)
# print("rotZ matrix")
# print_matrix(rotZ_matrix)
#
# matrix_mult(scale_matrix, edge_matrix)
# print("matrix after scale matrix multiplication")
# print_matrix(edge_matrix)

display(screen)
