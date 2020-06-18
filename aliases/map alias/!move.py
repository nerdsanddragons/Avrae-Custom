!alias move embed
<drac2>
location="&1&".upper()
note= f"""{location}"""
if combat() and combat().me:
    combat().me.set_note(note)
    output= f'-title "Moving" -desc "{name} moves to {location}" -color {color} -thumb {image}'
else:
    output= f'-title "You currently aren\'t in combat" -color {color} -thumb {image}'

return output
</drac2>


!alias over embed
<drac2>
input= ''.join([f'*{arg}/' for arg in &ARGS&])
if combat():
    spell= combat().get_combatant("Overlay")
    spell.set_note(input)
    output= f'-title "Added Spell Effect Overlay" -color {color}'
else:
    output= f'-title "You currently aren\'t in combat" -color {color}'

return output
</drac2>
