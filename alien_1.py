alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:"+str(alien_0['x_position']))
alien_0['speed'] = 'fast'

#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #移动很快
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:"+str(alien_0['x_position']))

