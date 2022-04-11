# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy

import pandas as pd
from psychopy import visual, sound, core
import random

# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)

df = pd.read_csv('picture_verification_stimuli.csv')

# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)

for _, row in df.iterrows():
    print(df['item'][_])

# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().

window = visual.Window(size=(400, 400))
message = visual.TextStim(window)

for _, row in df.iterrows():    
    message.text = df['item'][_] 
    message.draw()
    window.flip()
    core.wait(1.0)

# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.

for _, row in df.iterrows():
    image = visual.ImageStim(window, image=df['image_file'][_])
    image.draw()  # Draw the loaded image
    window.flip()
    core.wait(1.0)

## Exercise B
# 1. Load the lexical decision stimuli file 
# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)
# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')
# 4. Play the sounds one-by-one, making sure there is some time between them

df_lexdec = pd.read_csv('lexical_decision_stimuli.csv')

category = 'HF'
df_lexdec_HF_mask = df_lexdec['freq_category'] == category
df_new = df_lexdec.loc[df_lexdec_HF_mask, 'word']

window = visual.Window(size=(400, 400))

for ind in df_new.index:
    theSound = df_new[ind]    
    audio = sound.Sound(f'sounds/HF/{theSound}.wav')
    audio.play()    
    core.wait(2.0)

## Bonus exercise
# 1. Try to load in the image and/or sound stimuli first, 
#     before showing/playing them. You can use a list, and the .append()
#     method, to build a list of stimuli, and then use another for loop
#     to show/play them one by one.
# 2. Before showing/playing, try to randomise the order of stimuli; 
#     Google how to randomise the order of a list!

df = pd.read_csv('picture_verification_stimuli.csv')
window = visual.Window(size=(400, 400))
message = visual.TextStim(window)
piclist = []

for _, row in df.iterrows():
    piclist.append(visual.ImageStim(window, image=df['image_file'][_]))

random.seed()
random.shuffle(piclist)

for x in piclist:
    message.text = x.image.replace('images/', '').replace('.png', '')
    message.pos = (0.0, -0.9)
    x.draw()
    message.draw() 
    window.flip()
    core.wait(2.0)

# I carried out this experiment with the Furhat --> https://www.youtube.com/watch?v=Fgh8Ho_ioyg