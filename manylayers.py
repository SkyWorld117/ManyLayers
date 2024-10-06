import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

plt.rcParams['text.usetex'] = True

class drawBoard:
    def __init__(self, line_width, circle_radius, padding, shift, fig_size, debug=False):
        self.line_width = line_width
        self.lw = line_width/72
        self.circle_radius = circle_radius
        self.padding = padding
        self.shift = shift
        self.fig_size = fig_size
        self.debug = debug

        self.fig, self.ax = plt.subplots(figsize=fig_size)
        self.ax.set_xlim(0, fig_size[0])
        self.ax.set_ylim(0, fig_size[1])

        if debug:
            self.ax.axis('on')
        else:
            self.ax.axis('off')

    def save(self, filename):
        if self.debug:
            self.fig.savefig(filename)
        else:
            self.fig.savefig(filename, bbox_inches='tight', pad_inches=1)

class Line:
    def __init__(self, drawBoard, coord_x, coord_y, target_x, target_y, color='black', bg_color='white'):
        self.drawBoard = drawBoard
        self.start = (coord_x, coord_y)
        self.end = (target_x, target_y)
        self.color = color
        self.bg_color = bg_color

        self.middle = ((coord_x+target_x)/2, (coord_y+target_y)/2)

        self.layers = 1

    def draw(self, zorder=0, shift_x=0, shift_y=0):
        self.drawBoard.ax.plot([self.start[0]+shift_x, self.end[0]+shift_x], [self.start[1]+shift_y, self.end[1]+shift_y], '-', lw=self.drawBoard.line_width, color=self.color, zorder=zorder)

class Arrow: 
    def __init__(self, drawBoard, coord_x, coord_y, target_x, target_y, color='black', bg_color='white'): 
        self.drawBoard = drawBoard
        self.start = (coord_x, coord_y)
        self.end = (target_x, target_y)
        self.color = color
        self.bg_color = bg_color

        self.middle = ((coord_x+target_x)/2, (coord_y+target_y)/2)

        self.layers = 1

    def draw(self, zorder=0, shift_x=0, shift_y=0): 
        self.drawBoard.ax.annotate("", xy=(self.end[0]+shift_x, self.end[1]+shift_y), xytext=(self.start[0]+shift_x, self.start[1]+shift_y), arrowprops=dict(arrowstyle="->", color=self.color, lw=self.drawBoard.line_width), zorder=zorder)

class Text: 
    def __init__(self, drawBoard, coord_x, coord_y, text, fontsize, h_pos='center', v_pos='center', color='black', bg_color='white'): 
        self.drawBoard = drawBoard
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.text = text
        self.fontsize = fontsize
        self.h_pos = h_pos
        self.v_pos = v_pos
        self.color = color
        self.bg_color = bg_color

        self.layers = 1

    def draw(self, zorder=0, shift_x=0, shift_y=0): 
        self.drawBoard.ax.text(self.coord_x+shift_x, self.coord_y+shift_y, self.text, horizontalalignment=self.h_pos, verticalalignment=self.v_pos, fontsize=self.fontsize, color=self.color, zorder=zorder)

class Matrix: 
    def __init__(self, drawBoard, coord_x, coord_y, rows, cols, dense, h_align=None, v_align=None, color='black', bg_color='white'): 
        self.drawBoard = drawBoard
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.rows = rows
        self.cols = cols
        self.dense = dense

        self.width = cols*(drawBoard.circle_radius*2) + (cols+1)*drawBoard.padding + 2*self.drawBoard.lw
        self.height = rows*(drawBoard.circle_radius*2) + (rows+1)*drawBoard.padding + 2*self.drawBoard.lw

        if h_align is not None:
            self.coord_x = h_align.top[0] - 0.5*self.width
        if v_align is not None:
            self.coord_y = v_align.left[1] - 0.5*self.height

        self.left = (self.coord_x, self.coord_y + 0.5*self.height)
        self.right = (self.coord_x + self.width, self.coord_y + 0.5*self.height)
        self.top = (self.coord_x + 0.5*self.width, self.coord_y + self.height)
        self.bottom = (self.coord_x + 0.5*self.width, self.coord_y)

        self.color = color
        self.bg_color = bg_color

        self.layers = 2

    def draw(self, zorder=0, shift_x=0, shift_y=0): 
        self.drawBoard.ax.add_patch(Rectangle((self.coord_x-self.drawBoard.lw+shift_x, self.coord_y-self.drawBoard.lw+shift_y), self.width+2*self.drawBoard.lw, self.height+2*self.drawBoard.lw, edgecolor='none', facecolor=self.bg_color, zorder=zorder))
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.dense and (i+j)%2 == 1:
                    continue
                center_x = self.coord_x + (1+j)*self.drawBoard.padding + (j*2+1)*self.drawBoard.circle_radius + self.drawBoard.lw
                center_y = self.coord_y + (1+i)*self.drawBoard.padding + (i*2+1)*self.drawBoard.circle_radius + self.drawBoard.lw
                self.drawBoard.ax.add_patch(Circle((center_x+shift_x, center_y+shift_y), self.drawBoard.circle_radius, color=self.color, zorder=zorder+1))

        self.drawBoard.ax.plot([self.coord_x+shift_x, self.coord_x+shift_x], [self.coord_y+shift_y, self.coord_y + self.height+shift_y], '-', lw=self.drawBoard.line_width, color=self.color, zorder=zorder+1)
        self.drawBoard.ax.plot([self.coord_x+self.width+shift_x, self.coord_x+self.width+shift_x], [self.coord_y+shift_y, self.coord_y + self.height+shift_y], '-', lw=self.drawBoard.line_width, color=self.color, zorder=zorder+1)
        self.drawBoard.ax.plot([self.coord_x+shift_x, self.coord_x + 0.1*self.height+shift_x], [self.coord_y+shift_y, self.coord_y+shift_y], '-', lw=self.drawBoard.line_width, color=self.color, zorder=zorder+1)
        self.drawBoard.ax.plot([self.coord_x+shift_x, self.coord_x + 0.1*self.height+shift_x], [self.coord_y + self.height+shift_y, self.coord_y + self.height+shift_y], '-', lw=self.drawBoard.line_width, color=self.color, zorder=zorder+1)
        self.drawBoard.ax.plot([self.coord_x + self.width+shift_x, self.coord_x + self.width - 0.1*self.height+shift_x], [self.coord_y+shift_y, self.coord_y+shift_y], '-', lw=self.drawBoard.line_width, color=self.color, zorder=zorder+1)
        self.drawBoard.ax.plot([self.coord_x + self.width+shift_x, self.coord_x + self.width - 0.1*self.height+shift_x], [self.coord_y + self.height+shift_y, self.coord_y + self.height+shift_y], '-', lw=self.drawBoard.line_width, color=self.color, zorder=zorder+1)

class multiDraw: 
    def __init__(self, drawBoard, target, h_align=None, v_align=None):
        self.drawBoard = drawBoard
        self.coord_x = target.coord_x
        self.coord_y = target.coord_y
        self.target = target

        self.width = self.target.width + 2*self.drawBoard.shift
        self.height = self.target.height + 2*self.drawBoard.shift

        if h_align is not None:
            self.coord_x = h_align.top[0] - 0.5*self.width
            self.target.coord_x = self.coord_x
        if v_align is not None:            
            self.coord_y = v_align.left[1] - 0.5*self.height
            self.target.coord_y = self.coord_y

        self.left = (self.coord_x, self.coord_y + 0.5*self.height)
        self.right = (self.coord_x + self.width, self.coord_y + 0.5*self.height)
        self.top = (self.coord_x + 0.5*self.width, self.coord_y + self.height)
        self.bottom = (self.coord_x + 0.5*self.width, self.coord_y)

        self.layers = 3 * self.target.layers

    def draw(self, zorder=0, shift_x=0, shift_y=0):  
        self.target.draw(zorder=zorder, shift_x=shift_x, shift_y=shift_y)
        self.target.draw(zorder=zorder+self.target.layers, shift_x=self.drawBoard.shift+shift_x, shift_y=self.drawBoard.shift+shift_y)
        self.target.draw(zorder=zorder+2*self.target.layers, shift_x=2*self.drawBoard.shift+shift_x, shift_y=2*self.drawBoard.shift+shift_y)

# Element should be a list of drawables
class Frame: 
    def __init__(self, drawBoard, coord_x, coord_y, width, height, elements, h_align=None, v_align=None, color='black', bg_color='white'): 
        self.drawBoard = drawBoard
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.width = width
        self.height = height
        self.elements = elements

        if h_align is not None:
            self.coord_x = h_align.top[0] - 0.5*self.width
        if v_align is not None:
            self.coord_y = v_align.left[1] - 0.5*self.height

        self.left = (self.coord_x, self.coord_y + 0.5*self.height)
        self.right = (self.coord_x + self.width, self.coord_y + 0.5*self.height)
        self.top = (self.coord_x + 0.5*self.width, self.coord_y + self.height)
        self.bottom = (self.coord_x + 0.5*self.width, self.coord_y)

        self.color = color
        self.bg_color = bg_color

        self.layers = 1 + max([element.layers for element in elements])

    def draw(self, zorder=0, shift_x=0, shift_y=0): 
        self.drawBoard.ax.add_patch(Rectangle((self.coord_x+shift_x, self.coord_y+shift_y), self.width, self.height, edgecolor=self.color, facecolor=self.bg_color, zorder=zorder))
        for element in self.elements: 
            element.draw(zorder=zorder+1, shift_x=self.coord_x, shift_y=self.coord_y)
