import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from manylayers import *

fig_size = (65, 12.5)
line_width = 2
circle_radius = 0.125
padding = 0.25
shift = 0.15

draw_board = drawBoard(line_width, circle_radius, padding, shift, fig_size, debug=False)

in_mat = Matrix(draw_board, 1, 2, 5, 5, dense=True, h_align=None, v_align=None, color='grey', bg_color='lightgrey')
in_mat_t = Text(draw_board, in_mat.bottom[0], in_mat.bottom[1]-padding, r'Input: $1 \times I \times I$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')

conv1 = multiDraw(draw_board, Matrix(draw_board, 5, 4.5, 3, 3, True, h_align=None, v_align=None, color='black', bg_color='lightgrey'), h_align=None, v_align=in_mat)
conv1_t = Text(draw_board, conv1.bottom[0], conv1.bottom[1]-padding, r'Conv1: $1 \times c_1 \times k_1 \times k_1$', 20, h_pos='center', v_pos='top', color='black', bg_color='lightgrey')
a1 = Arrow(draw_board, *in_mat.right, *conv1.left, color='grey', bg_color='lightgrey')
a1_t = Text(draw_board, *a1.middle, r'$*$', 20, h_pos='center', v_pos='bottom', color='black')

im1 = multiDraw(draw_board, Matrix(draw_board, 9, 4.5, 5, 5, True, h_align=None, v_align=None, color='grey', bg_color='lightgrey'), h_align=None, v_align=in_mat)
im1_t = Text(draw_board, im1.bottom[0], im1.bottom[1]-padding, r'$c_1 \times (I-k_1+1) \times (I-k_1+1)$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a2 = Arrow(draw_board, *conv1.right, *im1.left, color='grey', bg_color='lightgrey')

im2 = multiDraw(draw_board, Matrix(draw_board, 15.5, 4.5, 3, 3, True, h_align=None, v_align=None, color='grey', bg_color='lightgrey'), h_align=None, v_align=in_mat)
im2_t = Text(draw_board, im2.bottom[0], im2.bottom[1]-padding, r'$c_1 \times \frac{I-k_1+1}{p_1} \times \frac{I-k_1+1}{p_1}$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a3 = Arrow(draw_board, *im1.right, *im2.left, color='grey', bg_color='lightgrey')
a3_t = Text(draw_board, *a3.middle, r'MaxPool2D with $p_1$', 20, h_pos='center', v_pos='bottom', color='black')

lif1 = multiDraw(draw_board, Matrix(draw_board, 15.5, 8, 3, 3, True, h_align=None, v_align=None, color='black', bg_color='lightgrey'), h_align=im2, v_align=None)
lif1_t = Text(draw_board, lif1.top[0], lif1.top[1]+padding, r'Membrane Potential: $c_1 \times \frac{I-k_1+1}{p_1} \times \frac{I-k_1+1}{p_1}$', 20, h_pos='center', v_pos='bottom', color='black', bg_color='lightgrey')
l1 = Line(draw_board, *im2.top, *lif1.bottom, color='black', bg_color='lightgrey')
l1_t = Text(draw_board, *l1.middle, r'Leaky and Integrate', 20, h_pos='right', v_pos='center', color='black', bg_color='lightgrey')

im3 = multiDraw(draw_board, Matrix(draw_board, 20, 4.5, 3, 3, False, h_align=None, v_align=None, color='grey', bg_color='lightgrey'), h_align=None, v_align=in_mat)
im3_t = Text(draw_board, im3.bottom[0], im3.bottom[1]-padding, r'$c_1 \times \frac{I-k_1+1}{p_1} \times \frac{I-k_1+1}{p_1}$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a4 = Arrow(draw_board, *l1.middle, *im3.left, color='grey', bg_color='lightgrey')
a4_t = Text(draw_board, *a4.middle, r'Fire', 20, h_pos='left', v_pos='bottom', color='black', bg_color='lightgrey')
a5 = Arrow(draw_board, *im3.top, *lif1.right, color='black', bg_color='lightgrey')
a5_t = Text(draw_board, *a5.middle, r'Refractory', 20, h_pos='left', v_pos='bottom', color='black')

conv2 = multiDraw(draw_board, Matrix(draw_board, 24, 4.5, 3, 3, True, h_align=None, v_align=None, color='black', bg_color='lightgrey'), h_align=None, v_align=in_mat)
conv2_t = Text(draw_board, conv2.bottom[0], conv2.bottom[1]-padding, r'Conv2: $c_2 \times c_1 \times k_2 \times k_2$', 20, h_pos='center', v_pos='top', color='black', bg_color='lightgrey')
a6 = Arrow(draw_board, *im3.right, *conv2.left, color='black', bg_color='lightgrey')
a6_t = Text(draw_board, *a6.middle, r'$*$', 20, h_pos='center', v_pos='bottom', color='black')

im4 = multiDraw(draw_board, Matrix(draw_board, 29.5, 4.5, 3, 3, True, h_align=None, v_align=None, color='grey', bg_color='lightgrey'), h_align=None, v_align=in_mat)
im4_t = Text(draw_board, im4.bottom[0], im4.bottom[1]-padding, r'$c_2 \times (\frac{I-k_1+1}{p_1}-k_2+1) \times (\frac{I-k_1+1}{p_1}-k_2+1)$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a7 = Arrow(draw_board, *conv2.right, *im4.left, color='grey', bg_color='lightgrey')

im5 = multiDraw(draw_board, Matrix(draw_board, 35.5, 4.5, 2, 2, True, h_align=None, v_align=None, color='grey', bg_color='lightgrey'), h_align=None, v_align=in_mat)
im5_t = Text(draw_board, im5.bottom[0], im5.bottom[1]-padding, r'$c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a8 = Arrow(draw_board, *im4.right, *im5.left, color='grey', bg_color='lightgrey')
a8_t = Text(draw_board, *a8.middle, r'MaxPool2D with $p_2$', 20, h_pos='center', v_pos='bottom', color='black')

lif2 = multiDraw(draw_board, Matrix(draw_board, 35, 8, 2, 2, True, h_align=None, v_align=None, color='black', bg_color='lightgrey'), h_align=im5, v_align=None)
lif2_t = Text(draw_board, lif2.top[0], lif2.top[1]+padding, r'Membrane Potential: $c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', 20, h_pos='center', v_pos='bottom', color='black', bg_color='lightgrey')
l2 = Line(draw_board, *im5.top, *lif2.bottom, color='black', bg_color='lightgrey')
l2_t = Text(draw_board, *l2.middle, r'Leaky and Integrate', 20, h_pos='right', v_pos='center', color='black', bg_color='lightgrey')

im6 = multiDraw(draw_board, Matrix(draw_board, 40, 4.5, 2, 2, False, h_align=None, v_align=None, color='grey', bg_color='lightgrey'), h_align=None, v_align=in_mat)
im6_t = Text(draw_board, im6.bottom[0], im6.bottom[1]-padding, r'$c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a9 = Arrow(draw_board, *l2.middle, *im6.left, color='grey', bg_color='lightgrey')
a9_t = Text(draw_board, *a9.middle, r'Fire', 20, h_pos='left', v_pos='bottom', color='black', bg_color='lightgrey')
a10 = Arrow(draw_board, *im6.top, *lif2.right, color='black', bg_color='lightgrey')
a10_t = Text(draw_board, *a10.middle, r'Refractory', 20, h_pos='left', v_pos='bottom', color='black')

im7 = Matrix(draw_board, 44, 4.5, 1, 4, False, h_align=None, v_align=in_mat, color='grey', bg_color='lightgrey')
im7_t = Text(draw_board, im7.bottom[0], im7.bottom[1]-padding, r'$c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a11 = Arrow(draw_board, *im6.right, *im7.left, color='grey', bg_color='lightgrey')
a11_t = Text(draw_board, *a11.middle, r'Flatten', 20, h_pos='center', v_pos='bottom', color='black')

linear = Matrix(draw_board, 48, 4.5, 4, 2, True, h_align=None, v_align=in_mat, color='black', bg_color='lightgrey')
linear_t = Text(draw_board, linear.bottom[0], linear.bottom[1]-padding, r'Linear: $(c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}) \times L$', 20, h_pos='center', v_pos='top', color='black', bg_color='lightgrey')
a12 = Arrow(draw_board, *im7.right, *linear.left, color='grey', bg_color='lightgrey')
a12_t = Text(draw_board, *a12.middle, r'$\times$', 20, h_pos='center', v_pos='bottom', color='black')

im8 = Matrix(draw_board, 51, 4.5, 1, 2, True, h_align=None, v_align=in_mat, color='grey', bg_color='lightgrey')
im8_t = Text(draw_board, im8.bottom[0], im8.bottom[1]-padding, r'$L$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a13 = Arrow(draw_board, *linear.right, *im8.left, color='grey', bg_color='lightgrey')

im9 = Matrix(draw_board, 55, 4.5, 2, 1, True, h_align=None, v_align=in_mat, color='grey', bg_color='lightgrey')
im9_t = Text(draw_board, im9.bottom[0], im9.bottom[1]-padding, r'$L$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a14 = Arrow(draw_board, *im8.right, *im9.left, color='grey', bg_color='lightgrey')
a14_t = Text(draw_board, *a14.middle, r'Transpose', 20, h_pos='center', v_pos='bottom', color='black')

lif3 = Matrix(draw_board, 55, 8, 2, 1, True, h_align=im9, v_align=None, color='black', bg_color='lightgrey')
lif3_t = Text(draw_board, lif3.top[0], lif3.top[1]+padding, r'Membrane Potential: $L$', 20, h_pos='center', v_pos='bottom', color='black', bg_color='lightgrey')
l3 = Line(draw_board, *im9.top, *lif3.bottom, color='black', bg_color='lightgrey')
l3_t = Text(draw_board, *l3.middle, r'Leaky and Integrate', 20, h_pos='right', v_pos='center', color='black', bg_color='lightgrey')

im10 = Matrix(draw_board, 59, 8, 2, 1, False, h_align=None, v_align=in_mat, color='grey', bg_color='lightgrey')
im10_t = Text(draw_board, im10.bottom[0], im10.bottom[1]-padding, r'Output: $L$', 20, h_pos='center', v_pos='top', color='grey', bg_color='lightgrey')
a15 = Arrow(draw_board, *l3.middle, *im10.left, color='grey', bg_color='lightgrey')
a15_t = Text(draw_board, *a15.middle, r'Fire', 20, h_pos='left', v_pos='bottom', color='black')
a16 = Arrow(draw_board, *im10.top, *lif3.right, color='black', bg_color='lightgrey')
a16_t = Text(draw_board, *a16.middle, r'Refractory', 20, h_pos='left', v_pos='bottom', color='black')

frame = Frame(draw_board, 0, 0, 61, 12, [
    in_mat, in_mat_t, 
    conv1, conv1_t, a1, a1_t, 
    im1, im1_t, a2, 
    im2, im2_t, a3, a3_t, 
    lif1, lif1_t, l1, l1_t, 
    im3, im3_t, a4, a4_t, a5, a5_t, 
    conv2, conv2_t, a6, a6_t, 
    im4, im4_t, a7, 
    im5, im5_t, a8, a8_t, 
    lif2, lif2_t, l2, l2_t, 
    im6, im6_t, a9, a9_t, a10, a10_t, 
    im7, im7_t, a11, a11_t, 
    linear, linear_t, a12, a12_t, 
    im8, im8_t, a13, 
    im9, im9_t, a14, a14_t, 
    lif3, lif3_t, l3, l3_t,
    im10, im10_t, a15, a15_t, a16, a16_t
], h_align=None, v_align=None, color='black', bg_color='lightgrey')

SNN = multiDraw(draw_board, frame, h_align=None, v_align=None)
SNN.draw()
Text(draw_board, SNN.right[0], SNN.bottom[1], r'$B \times T$', 35, h_pos='left', v_pos='bottom', color='black', bg_color='lightgrey').draw()

draw_board.save('snn.png')
draw_board.save('snn.pdf')
