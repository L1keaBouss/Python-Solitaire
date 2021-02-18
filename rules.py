NUMBER_OF_CARDS     = 52                		# Total 52 cards
rows        		= 2                 		# Two rows
columns     		= 7                 		# 7 colums
cells       		= rows * columns    		# Cells - total positions for cards
all         		= cells + NUMBER_OF_CARDS   # Total cards and blan cards
card_width  		= 153               		# Width of card in pixels
card_height 		= 200               		# height of card in pixels
pad_x       		= 36                		# Gap between cells on horizontal
pad_y       		= 36                		# Gap between celss on vertical
card_pad    		= 25                		# The distance between cards in stack
font        		= 'simsun 16 bold'  		# font used in buttons
path        		= 'static_assets/'   		# Sub-directory for card PNG files
width       		= (card_width + pad_x) * columns + pad_x            # Graphic width
height      		= (card_height + pad_y) * rows + pad_y + 9*card_pad # Graphic Height
# Coordinates for each cell
ref_x       		= [(pad_x + card_width) * int(i%7) + pad_x for i in range(cells)]
ref_y       		= [height - card_height * int(i/7) - pad_y * int(i/7 + 1)
                for i in range(cells)]
# Rack position for each cards
stack       		= [i for i in range(cells)] + [0 for i in range(24)]+[
               6+i for i in range(8) for j in range(i)]
show_card   		= [38, 40, 43, 47, 52, 58, 65]  # Cards shown when beginning
start_x     		= int((width-card_width)/2)     # Position for flash card show
start_y     		= card_height+pad_y
# Image filenames of cards with top-side and bottom-side
file        		= [['']+[path+'0.png' for i in range(52)],
               [path+'n.png']+[path+str(i+1)+'.png' for i in range(52)]]
# Area of rack in cells, 0 ~ 13 for all cells
top         		= [3, 4, 5, 6]
bottom      		= [7, 8, 9, 10, 11, 12, 13]

button_down 		= False     # Flag for mouse left button down
drag        		= False     # Flag for mouse in drag mode
start       		= True      # Flag for initial position of mouse
New_Start   		= True      # Flag for new game
import ctypes
ctypes.windll.user32.SetProcessDPIAware()   # Set unit of GUI to pixels