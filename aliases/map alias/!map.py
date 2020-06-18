tembed 
<drac2>
# Set are base variables

# These are replaced with proper values from the base alias
args, defaults=argparse("@@@"),"&&&"
mapsize=defaults.get("size","")
mapoptions=defaults.get("options","")
mapbg=defaults.get("background","")
mapinfo=""
mapattach=""
map="http://otfbm.com/"
out={}
col,siz,alph="grbypcd","TSMLHG","ABCDEFGHIJKLMNOPQRSTUVWXYZ"
COL,SIZ = {"g":"Forest Green", "r":"Firebrick Red", "b":"Corn Flower Blue", "y":"Gold/Yellow", "p":"Dark Violet", "c":"Deep Sky Blue", "d":"Dark Golden Rod"},{"T":"Tiny", "S":"Small", "M":"Medium", "L":"Large", "H":"Huge", "G":"Gargantuan"}
overlays=[]
c=combat()
gt=c.get_combatant if c else None
debug = ""
desc = []
g = load_json(get_gvar("d456fdfa-a292-42a1-ab00-b884e79b702f"))
# F-Strings like to yell at me for \'s
newline, targD = "\n", "{targ}"
</drac2>
<drac2>
# If we're in combat, check all the things
if c:
 # Collect information on every combatant
 for combatant in combat().combatants:

  # Grab map information, if it exists
  for attack in combatant.attacks:
   if attack.name == 'map':
    mapattach=combatant
    mapinfo=attack.automation[0].text

  # Set every combatant to a random location and size.
  # Doesn't respect the size of the map (currently)
  if args.last('rand'):
   note=f"""Location: {alph[randint(26)]}{randint(20)+1}"""
   note+=f""" | Color: {col[randint(7)]}"""
   note+=f""" | Size: {siz[randint(6)]}"""
   combatant.set_note(note)
</drac2>
<drac2>
if c:
 # If we found a `map` attack with information, parse it now
 if mapinfo:
  # Split and convert to dict. Couldn't use | here because of how -attack effects are parsed
  mapinfo=mapinfo.split(' ~ ')
  mapinfo={x[0].lower():x[1] for x in [item.split(': ') for item in mapinfo]}
  mapsize=mapinfo.get('size')
  mapbg=mapinfo.get('background')
  mapoptions=mapinfo.get('options')
</drac2>
<drac2>
if c:
 # If theres a -mapsize, -mapbg, -mapoptions, or -mapattach arg, process that and add/replace the effect
 if args.last('mapsize') or args.last('mapbg') or args.last('mapoptions') or args.last('mapattach'):
  # Note to self: Should probably validate these arguments later
  # If the new mapsize is different from the old one, update and display
  if mapsize != args.last('mapsize', mapsize):
   mapsize = args.last('mapsize', mapsize)
   desc.append(f"Map size changed to `{mapsize}`")
  # If the new mapbg is different from the old one, update and display
  if mapbg != args.last('mapbg', mapbg):
   mapbg = args.last('mapbg', mapbg)
   desc.append(f"Map background changed to `{mapbg}`")
  if mapoptions != args.last('mapoptions', mapoptions):
  # If the new mapoptions are different from the old ones, update and display
   mapoptions = args.last('mapoptions', mapoptions)
   desc.append(f"Map options changed to `{mapoptions}`")   
  # If there is a -mapattach, and its a valid target in init
  if args.last('mapattach') and gt(args.last('mapattach')):
   # First check if there is an existing mapattach, and if its the same as the new one, then remove their map effect
   if typeof(mapattach)=="SimpleCombatant" and gt(args.last('mapattach')).name != mapattach.name:
    mapattach.remove_effect('map')
   # Then, set the new mapattach
   mapattach = gt(args.last('mapattach'))
  # If theres mapattach set, and they currently have a map effect, remove it
  if mapattach and mapattach.get_effect('map'):
   mapattach.remove_effect('map')
  # Format everything appropriately
  neweffect = f"""{f"Size: {mapsize}" if mapsize else ""}{f" ~ Background: {mapbg}" if mapbg else ""}{f" ~ Options: {mapoptions}" if mapoptions else ""}""".strip(" ~")
  # If mapattach exists, apply the new effect, and display
  if mapattach:
   mapattach.add_effect('map', f"""-attack "||{neweffect}" """)
   desc.append(f"Map settings attached to `{mapattach.name}`")
  # Otherwise, show that it was changed, but not saved
  else:
   desc.append("Map settings changed, but no map attach target was found. Settings not saved.")
</drac2>
<drac2>
if c:
 # Read each combatants notes for their information
 for target in combat().combatants:
  # If they have a note, perse it into a dict
  if target.note:
   note=target.note
   note=note.split(" | ")
   note={x[0].lower():x[1] for x in [item.split(": ") for item in note]}
   out[target.name]=note
</drac2>
<drac2>
if c:
 # If there is a -t argument given, and that target exists as a combatant, modify that target
 if args.last('t') and gt(args.last('t')):
  targ=gt(args.last('t'))
  # If they don't have a note/location set, add them to the list
  if not out.get(targ.name):
   out[targ.name] = {}
  # If there is a -size arg, change their size
  if args.last('size'):
   size=args.last('size')[0].upper()
   # Confirm that the given size is valid before updating
   if size in siz:
    out[targ.name].update({"size":f"{size} ({SIZ[size]})"})
    # Display the change in size
    desc.append(f"Changing size of {targ.name} to {SIZ[size]} ({size})")
   # If the size is None, erase the size, setting them back to Medium
   elif args.last('size') in (None,"None","none"):
    _ = out[targ.name].pop('size')
    # Display the change in size
    desc.append(f"Resetting size of {targ.name} to Medium (M)")
</drac2>
<drac2>
if c:
 # If there is a -t argument given, and that target exists as a combatant, modify that target
 if args.last('t') and gt(args.last('t')):
  # If there is a -color arg, change their color
  if args.last('color'):
   color=args.last('color')[0].lower()
   # Confirm that the given color is valid before updating
   if color in col:
    out[targ.name].update({"color":f"{color} ({COL[color]})"})
    # Display the change in color
    desc.append(f"Changing color of {targ.name} to {COL[color]} ({color})")
   # If the color is None, erase the color, setting them back to black
   elif args.last('color') in (None,"None","none"):
    _ = out[targ.name].pop('color')
    # Display the change in color
    desc.append(f"Resetting color of {targ.name} to Black")
  # If there is a -move arg, move them to the new location
</drac2>
<drac2>
if c:
 # If there is a -t argument given, and that target exists as a combatant, modify that target
 if args.last('t') and gt(args.last('t')):
  if args.last('move'):
   prevLoc = out[targ.name].get('location') 
   # Did they have a previous location? If so, lets calculate distance and draw a line
   if prevLoc:
    # Split previous location from XY to X and Y
    prevLocX, prevLocY = prevLoc[0], prevLoc[1:]
    # Same as new location
    newLocX, newLocY = args.last('move')[0].upper(), args.last('move')[1:]
    # Calculate the delta for X and Y between the two
    deltaX, deltaY = alph.index(prevLocX)-alph.index(newLocX), int(prevLocY)-int(newLocY)
    # Throw them in the pot with some pythag
    distance = int(round(sqrt((deltaX*deltaX)+(deltaY*deltaY)),0))*5
    # Grab the targets new color if changed, old color if set, or default to dark violet
    colr = args.last('color', out[targ.name].get('color','p'))[0]
    # Add the line to the overlay list
    overlays.append(f"*l{distance},2{colr}{prevLocX}{prevLocY}{newLocX}{newLocY}")
    # Display the change in location
    desc.insert(0, f"Moving {targ.name} from {prevLoc} to {args.last('move').upper()} ({distance} ft.).")
   else:
    # Display the change in location
    desc.insert(0, f"Moving {targ.name} to {args.last('move').upper()}.")
   out[targ.name].update({"location":args.last('move').upper()})
</drac2>
<drac2>
# Overlay stuff
if c:
 # Is the user trying to set an overlay?
 if args.last('over'):
  # Split the input by commas
  overlay = args.last('over').split(',')
  # First argument is always the shape
  oShape = overlay[0].lower()
  if oShape == "circle":
   # Circle takes four arguments, shape, size, color, and starting location
   if len(overlay)==4:
    oShape  = "c" 
    oSize   = overlay[1]
    oColor  = overlay[2]
    oLoc    = overlay[3]
    overlay = f"""*{oShape}{oSize}{oColor}{oLoc}"""
    overdesc= f"Creating a {COL[oColor]} circle overlay, {oSize} ft. in diameter, positioned at {oLoc}"
   else:
    overlay = None
  elif oShape == "triangle" or oShape == "cone":
   # Cone takes five arguments, shape, size, color, starting location, and the location its aimed at
   if len(overlay)==5:
    oShape  = "t" 
    oSize   = overlay[1]
    oColor  = overlay[2]
    oLoc    = overlay[3]
    oEloc   = overlay[4]
    overlay = f"""*{oShape}{oSize}{oColor}{oLoc}{oEloc}"""
    overdesc= f"Creating a {COL[oColor]} cone overlay, {oSize} ft. long, positioned at {oLoc}, aimed at {oEloc}"
   else:
    overlay = None
  elif oShape == "line":
   # Lines takes six arguments, shape, size, width, color, starting location, and the location its aimed at
   if len(overlay)==6:
    oShape  = "l" 
    oSize   = overlay[1]
    oWidth  = overlay[2]
    oColor  = overlay[3]
    oLoc    = overlay[4]
    oEloc   = overlay[5]
    overlay = f"""*{oShape}{oSize},{oWidth}{oColor}{oLoc}{oEloc}"""
    overdesc= f"Creating a {COL[oColor]} line overlay, {oSize} ft. long, {oWidth} ft. wide, starting at {oLoc}, aimed at {oEloc}"
   else:
    overlay = None
  elif oShape == "square":
   # Square takes five arguments, shape, size, color, starting location, and the location its aimed at
   if len(overlay)==5:
    oShape  = "s" 
    oSize   = overlay[1]
    oColor  = overlay[2]
    oLoc    = overlay[3]
    oEloc   = overlay[4]
    overlay = f"""*{oShape}{oSize}{oColor}{oLoc}{oEloc}"""
    overdesc= f"Creating a {COL[oColor]} square overlay, {oSize} ft. wide, positioned at {oLoc}, aimed at {oEloc}"
   else:
    overlay = None
  else:
   overlay = None
  # Search external overlay preset dict
  mode = [x for x in {g} if args in x]
  if args.last('t') and gt(args.last('t')) and (args.last('over') in ('mode')):
   get_gvar(g[mode])
   desc.append(f"Added overlay to {targ.name}")
  # If, after all the parsing above, we managed to get a proper overlay, continue
  if overlay:
   # Are we attaching this overlay to a target?
   if args.last('t') and gt(args.last('t')):
    # If so, lets attach it to the notes
    out[targ.name].update({"overlay": overlay})
    desc.append(overdesc.replace('{targ}', out[targ.name].get('location','A1')) + f", linked to {gt(args.last('t')).name}")
   else: 
    # Otherwise, lets just display it once
    overlays.append(overlay)
    desc.append(overdesc)
  # If we have a target, but our -over arg is none, we're trying to delete our overlay
  if args.last('t') and gt(args.last('t')) and (args.last('over') in ("none", None, "None")):
   _ = out[targ.name].pop('overlay')
   desc.append(f"Removed overlay linked to {targ.name}")
</drac2> 
<drac2>
if c:
 # Parse the collected notes and information into the format readable by otfbm.com
 # Removes any quotes in names, as that breaks the map for that target apparently
 people=[f"""{out[target].get('location')}{out[target].get('size','M')[0]}{out[target].get('color',[''])[0]}-{target.replace(' ','_').replace("'","").replace('"','')}"""for target in out if out[target].get('location')]
 overlays += [out[target].get('overlay').replace("{targ}", out[target].get('location','A1')) for target in out if out[target].get('overlay')]
 # Reconvert all of our map information back into the readable note format
 dataout={x:' | '.join([f"{item[0].title()}: {item[1]}"for item in out[x].items()])for x in out}
 # Then set everyones note again. Kinda a chainsaw instead of a scalpal situation here.
 for target in dataout:
  gt(target).set_note(dataout[target])
 # If a 'clear' arg is given, clear the entire map (clears everyones notes)
 if args.last('clear'):
  [i.set_note(None)for i in combat().combatants]
  people=[]
 # Join everything together and display the map if we aren't displaying the help
 if not (args.get('?') or args.get('help')):
  return f"""-image "{map}{mapsize}/{f"@{mapoptions}/"if mapoptions else""}{'/'.join(people+overlays)}{f"?bg={mapbg}" if mapbg else ""}" """ + (f"""  -desc "{newline.join(desc)}"  """ if desc else "")
</drac2>

<drac2>
# If we're not in combat, or "?" or "help" are given as arguments, display the help
if not c or args.get('?') or args.get('help'):
 help = f"""-title "Dude, where did I park my Tarrasque?"
            -desc "`!map` - View the map
            `!map [args]` - Edit the map, its combatants, or its overlays

            `!move [location]` - The `!move` alias allows you to quickly move your currently active character around. For example: `!move B3` would move your active character to B3

            **__Main Arguments__**
            `-t <target>` - Select a target for adjusting location, color and size.
            `-mapattach <target>` - Gives a target an effect that contains map information such as size and background
            `-over <overlay>` - Creates an overlay on the map. Options for thise are described below.

            **__Target Arguments__** - Requires a `-t` target
            `-move [location]` - Sets the `-t` targets location on the map. For example `-move G3`.
            `-color [color]` - Sets the `-t` targets color on the map. `-color none` will reset it to to black. Valid arguments can be seen in the fields below.
            `-size [size]` - Sets the `-t` targets size on the map. `-size none` will reset it back to medium. Valid arguments can be seen in the fields below. 
            
            **__Map Arguments__** - Requires the map info to be set with `-mapattach`
            `-mapsize [size]` - Sets the size of the map. For example: 20x20
            `-mapbg [url]` - Sets a url to serve as the background. Maps are expected to have a grid scale of 40 px.
            `-mapoptions [options]` - Sets map options. Available options can be seen below.
            Settings can be viewed by running `!i aoo <mapattachee> map`"

            -f "_ _|**__Overlay Arguments__**
            `-over \"circle,<diameter>,<color>,<center>\"` - Creates a circle of a given diameter and color, at the chosen location
            `-over \"cone,<size>,<color>,<start>,<end>\"` - Creates a circle of a given diameter and color, at the chosen location
            `-over \"line,<length>,<width>,<color>,<start>,<end>\"` - Creates a circle of a given diameter and color, at the chosen location
            `-over \"square,<size>,<color>,<center>,<end>\"` - Creates a circle of a given diameter and color, at the chosen location
            All of these overlays are displayed just once, unless there is a `-t` arg provided, in which case it will added to the targets notes. You can have the targets location be linked to the location of the overlay by using `{targD}`. For example `-over circle,30,b,{targD} -t OR1` would cause it to be positioned on top of OR1, regardless of where they move.
            To remove a linked overlay, run `-over none` with a `-t` selector." 

            -f "Valid Colors|{newline.join([f"`{x[0]}` - {x[1]}" for x in COL.items()])}|inline"
            -f "Valid Sizes|{newline.join([f"`{x[0]}` - {x[1]}" for x in SIZ.items()])}|inline"
            -f "Valid Map Options|`d` - Dark mode{newline}`h` - Grid at half transparancy{newline}`n` - Grid hidden{newline}`1`,`2`,`3` - Different zoom options|inline" 
            -f "OTFBM Help|Additional reading on OTFBM website and functionality can be found [here](https://github.com/digitalsadhu/otf-battlemaps/blob/master/README.md)" """.replace(" "*11,"")

 return help
</drac2>
-footer "!map ?{{f" | Map settings attached to {mapattach.name}" if mapattach else ""}}"