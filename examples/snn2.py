import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from manylayers import *

fig_size = (32.5, 22.5)
line_width = 2
circle_radius = 0.125
padding = 0.25
shift = 0.15

fontsize = 30

draw_board = drawBoard(line_width, circle_radius, padding, shift, fig_size, debug=False)

in_mat = Matrix(draw_board, 1, 12, 5, 5, dense=True, h_align=None, v_align=None, color='grey', bg_color='gainsboro')
in_mat_t = Text(draw_board, in_mat.bottom[0], in_mat.bottom[1]-padding, r'Input: $1 \times I \times I$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')

conv1 = multiDraw(draw_board, Matrix(draw_board, 5, 4.5, 3, 3, True, h_align=None, v_align=None, color='black', bg_color='gainsboro'), h_align=None, v_align=in_mat)
conv1_t = Text(draw_board, conv1.top[0], conv1.top[1]+padding, r'Conv1: $1 \times c_1 \times k_1 \times k_1$', fontsize, h_pos='center', v_pos='bottom', color='black', bg_color='gainsboro')
a1 = Arrow(draw_board, *in_mat.right, *conv1.left, color='grey', bg_color='gainsboro')
a1_t = Text(draw_board, *a1.middle, r'$*$', fontsize, h_pos='center', v_pos='bottom', color='black')

im1 = multiDraw(draw_board, Matrix(draw_board, 9, 4.5, 5, 5, True, h_align=None, v_align=None, color='grey', bg_color='gainsboro'), h_align=None, v_align=in_mat)
im1_t = Text(draw_board, im1.bottom[0], im1.bottom[1]-padding, r'$c_1 \times (I-k_1+1) \times (I-k_1+1)$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')
a2 = Arrow(draw_board, *conv1.right, *im1.left, color='grey', bg_color='gainsboro')

im2 = multiDraw(draw_board, Matrix(draw_board, 17.5, 4.5, 3, 3, True, h_align=None, v_align=None, color='grey', bg_color='gainsboro'), h_align=None, v_align=in_mat)
im2_t = Text(draw_board, im2.bottom[0], im2.bottom[1]-padding, r'$c_1 \times \frac{I-k_1+1}{p_1} \times \frac{I-k_1+1}{p_1}$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')
a3 = Arrow(draw_board, *im1.right, *im2.left, color='grey', bg_color='gainsboro')
a3_t = Text(draw_board, *a3.middle, r'MaxPool2D with $p_1$', fontsize, h_pos='center', v_pos='bottom', color='black')

lif1 = multiDraw(draw_board, Matrix(draw_board, 15.5, 18, 3, 3, True, h_align=None, v_align=None, color='black', bg_color='gainsboro'), h_align=im2, v_align=None)
lif1_t = Text(draw_board, lif1.top[0], lif1.top[1]+padding, r'Membrane Potential: $c_1 \times \frac{I-k_1+1}{p_1} \times \frac{I-k_1+1}{p_1}$', fontsize, h_pos='center', v_pos='bottom', color='black', bg_color='gainsboro')
l1 = Line(draw_board, *im2.top, *lif1.bottom, color='black', bg_color='gainsboro')
l1_t = Text(draw_board, l1.middle[0]-padding, l1.middle[1], r'Leaky and Integrate', fontsize, h_pos='right', v_pos='center', color='black', bg_color='gainsboro')

im3 = multiDraw(draw_board, Matrix(draw_board, 22, 4.5, 3, 3, False, h_align=None, v_align=None, color='grey', bg_color='gainsboro'), h_align=None, v_align=in_mat)
im3_t = Text(draw_board, im3.bottom[0], im3.bottom[1]-padding, r'$c_1 \times \frac{I-k_1+1}{p_1} \times \frac{I-k_1+1}{p_1}$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')
a4 = Arrow(draw_board, *l1.middle, *im3.left, color='grey', bg_color='gainsboro')
a4_t = Text(draw_board, *a4.middle, r'Fire', fontsize, h_pos='left', v_pos='bottom', color='black', bg_color='gainsboro')
a5 = Arrow(draw_board, *im3.top, *lif1.right, color='black', bg_color='gainsboro')
a5_t = Text(draw_board, *a5.middle, r'Refractory', fontsize, h_pos='left', v_pos='bottom', color='black')

conv2 = multiDraw(draw_board, Matrix(draw_board, 26, 4.5, 3, 3, True, h_align=None, v_align=None, color='black', bg_color='gainsboro'), h_align=None, v_align=in_mat)
conv2_t = Text(draw_board, conv2.top[0], conv2.top[1]+padding, r'Conv2: $c_2 \times c_1 \times k_2 \times k_2$', fontsize, h_pos='center', v_pos='bottom', color='black', bg_color='gainsboro')
a6 = Arrow(draw_board, *im3.right, *conv2.left, color='black', bg_color='gainsboro')
a6_t = Text(draw_board, *a6.middle, r'$*$', fontsize, h_pos='center', v_pos='bottom', color='black')

im4 = multiDraw(draw_board, Matrix(draw_board, 24, 8.5, 3, 3, True, h_align=None, v_align=None, color='grey', bg_color='gainsboro'), h_align=None, v_align=None)
im4_t = Text(draw_board, im4.left[0]-padding, im4.left[1], r'$c_2 \times (\frac{I-k_1+1}{p_1}-k_2+1) \times (\frac{I-k_1+1}{p_1}-k_2+1)$', fontsize, h_pos='right', v_pos='center', color='grey', bg_color='gainsboro')
a7 = Arrow(draw_board, *conv2.bottom, *im4.top, color='grey', bg_color='gainsboro')

im5 = multiDraw(draw_board, Matrix(draw_board, 35.5, 4.5, 2, 2, True, h_align=None, v_align=None, color='grey', bg_color='gainsboro'), h_align=im4, v_align=None)
im5_t = Text(draw_board, im5.right[0]+padding, im5.right[1], r'$c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', fontsize, h_pos='left', v_pos='center', color='grey', bg_color='gainsboro')
a8 = Arrow(draw_board, *im4.bottom, *im5.top, color='grey', bg_color='gainsboro')
a8_t = Text(draw_board, a8.middle[0]+padding, a8.middle[1], r'MaxPool2D with $p_2$', fontsize, h_pos='left', v_pos='center', color='black')

lif2 = multiDraw(draw_board, Matrix(draw_board, 35, 2, 2, 2, True, h_align=None, v_align=None, color='black', bg_color='gainsboro'), h_align=im5, v_align=None)
lif2_t = Text(draw_board, lif2.bottom[0], lif2.bottom[1]-padding, r'Membrane Potential: $c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', fontsize, h_pos='center', v_pos='top', color='black', bg_color='gainsboro')
l2 = Line(draw_board, *im5.bottom, *lif2.top, color='black', bg_color='gainsboro')
l2_t = Text(draw_board, l2.middle[0]+padding, l2.middle[1], r'Leaky and Integrate', fontsize, h_pos='left', v_pos='center', color='black', bg_color='gainsboro')

im6 = multiDraw(draw_board, Matrix(draw_board, 20, 4.5, 2, 2, False, h_align=None, v_align=None, color='grey', bg_color='gainsboro'), h_align=None, v_align=im5)
im6_t = Text(draw_board, im6.top[0], im6.top[1]+padding, r'$c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', fontsize, h_pos='center', v_pos='bottom', color='grey', bg_color='gainsboro')
a9 = Arrow(draw_board, *l2.middle, *im6.right, color='grey', bg_color='gainsboro')
a9_t = Text(draw_board, *a9.middle, r'Fire', fontsize, h_pos='left', v_pos='bottom', color='black', bg_color='gainsboro')
a10 = Arrow(draw_board, *im6.bottom, *lif2.left, color='black', bg_color='gainsboro')
a10_t = Text(draw_board, *a10.middle, r'Refractory', fontsize, h_pos='left', v_pos='bottom', color='black')

im7 = Matrix(draw_board, 16, 4.5, 1, 4, False, h_align=None, v_align=im5, color='grey', bg_color='gainsboro')
im7_t = Text(draw_board, im7.bottom[0], im7.bottom[1]-padding, r'$c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')
a11 = Arrow(draw_board, *im6.left, *im7.right, color='grey', bg_color='gainsboro')
a11_t = Text(draw_board, *a11.middle, r'Flatten', fontsize, h_pos='center', v_pos='bottom', color='black')

linear = Matrix(draw_board, 12, 4.5, 4, 2, True, h_align=None, v_align=im5, color='black', bg_color='gainsboro')
linear_t = Text(draw_board, linear.bottom[0], linear.bottom[1]-2*padding, r'Linear: $(c_2 \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2} \times \frac{\frac{I-k_1+1}{p_1}-k_2+1}{p_2}) \times L$', fontsize, h_pos='center', v_pos='top', color='black', bg_color='gainsboro')
a12 = Arrow(draw_board, *im7.left, *linear.right, color='grey', bg_color='gainsboro')
a12_t = Text(draw_board, *a12.middle, r'$\times$', fontsize, h_pos='center', v_pos='bottom', color='black')

im8 = Matrix(draw_board, 8, 4.5, 1, 2, True, h_align=None, v_align=im5, color='grey', bg_color='gainsboro')
im8_t = Text(draw_board, im8.bottom[0], im8.bottom[1]-padding, r'$L$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')
a13 = Arrow(draw_board, *linear.left, *im8.right, color='grey', bg_color='gainsboro')

im9 = Matrix(draw_board, 4, 4.5, 2, 1, True, h_align=None, v_align=im5, color='grey', bg_color='gainsboro')
im9_t = Text(draw_board, im9.bottom[0], im9.bottom[1]-padding, r'$L$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')
a14 = Arrow(draw_board, *im8.left, *im9.right, color='grey', bg_color='gainsboro')
a14_t = Text(draw_board, *a14.middle, r'Transpose', fontsize, h_pos='center', v_pos='bottom', color='black')

lif3 = Matrix(draw_board, 55, 8, 2, 1, True, h_align=im9, v_align=None, color='black', bg_color='gainsboro')
lif3_t = Text(draw_board, lif3.top[0], lif3.top[1]+padding, r'Membrane Potential: $L$', fontsize, h_pos='center', v_pos='bottom', color='black', bg_color='gainsboro')
l3 = Line(draw_board, *im9.top, *lif3.bottom, color='black', bg_color='gainsboro')
l3_t = Text(draw_board, l3.middle[0]+padding, l3.middle[1], r'Leaky and Integrate', fontsize, h_pos='left', v_pos='center', color='black', bg_color='gainsboro')

im10 = Matrix(draw_board, 1.5, 8, 2, 1, False, h_align=None, v_align=im5, color='grey', bg_color='gainsboro')
im10_t = Text(draw_board, im10.bottom[0], im10.bottom[1]-padding, r'Output: $L$', fontsize, h_pos='center', v_pos='top', color='grey', bg_color='gainsboro')
a15 = Arrow(draw_board, *l3.middle, *im10.right, color='grey', bg_color='gainsboro')
a15_t = Text(draw_board, a15.middle[0]-padding, a15.middle[1], r'Fire', fontsize, h_pos='right', v_pos='center', color='black')
a16 = Arrow(draw_board, *im10.top, *lif3.left, color='black', bg_color='gainsboro')
a16_t = Text(draw_board, *a16.middle, r'Refractory', fontsize, h_pos='right', v_pos='bottom', color='black')

frame = Frame(draw_board, 0, 0, 32, 22, [
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
], h_align=None, v_align=None, color='black', bg_color='gainsboro')

SNN = multiDraw(draw_board, frame, h_align=None, v_align=None)
SNN.draw()
Text(draw_board, SNN.bottom[0], SNN.bottom[1]-padding, r'$B \times T$', 35, h_pos='center', v_pos='top', color='black', bg_color='gainsboro').draw()

draw_board.save('snn2.pdf')
draw_board.save('snn2.png')
