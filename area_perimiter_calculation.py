# Created by: Jacob Liberty 
# Created on: September 17 2017
# Created for: ICS3U
# This program calculates the perimiter and area of a rectangle

import ui

def calculate_perimiter_touch_up_inside(sender):
    #calculate the perimiter of the shape
    view['perimiter_label'].text = 'The perimiter is ' + str(5+3+5+3) + 'm'
	
def calculate_area_touch_up_inside(sender):
    #calculate the area of the shape
    view['area_label'].text = 'The area is ' + str(5*3) + 'm'

view = ui.load_view()
view.present('sheet')
