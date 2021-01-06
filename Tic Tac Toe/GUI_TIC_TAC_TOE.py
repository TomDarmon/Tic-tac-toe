import ui

def button_tapped(sender):
	return True

ui.load_view('My UI').present('popover')


"""def button_tapped(sender):
    sender.title = 'Hello'

ui.load_view('My UI').present('sheet')
	
view = ui.View() #Make a view to make things appear
view.name = "Demo" #Title of the view
view.background_color = "white" #color of the background
button = ui.Button(title = 'Tap me') #Creation of the button
button.center = (view.width * 0.5, view.height *0.5) #center
button.flex = "LRTB" #auto resizing Left Right Top Bottom
button.action = button_tapped #action of the button
view.add_subview(button) #Add a child ? 
view.present("sheet") #we call the view as 'sheet' view"""
