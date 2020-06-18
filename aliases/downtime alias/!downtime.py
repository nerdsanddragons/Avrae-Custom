!alias dt tembed {{g = load_json(get_gvar("03de1c2a-db68-4835-87aa-24b71c26e9b2"))}}{{mode = ([x for x in g if "&1&".lower() in x]+['help?'])[0]}}{{get_gvar(g[mode]).replace("&AR"+"GS&", str(&ARGS&[1:]))}}

-title "Downtime Activities"
-desc "Welcome to Downtime Activities. Each activity will cost you a Downtime point as well as money, even if the activity you attempt fails.

**Training**
Feat Training: `!dt feat[feat]`
Skills Training: `!dt skill[skill]`
Learn Language: `!dt lang[language]`
Tools Training: `!dt tool[tool]`

**Craft Items**
Magical Items: `!dt magic`
Spell Scrolls: `!dt scroll[level]`

**Make Money**
Hired Work: `!dt hired`
Fighting Ring: `!dt fight`
Steal: `!dt steal` - Free but chance to loose money by spending time in jail

**Downtime Points**
Replenish spent downtime points: `!dt points`"

-footer "!dt help | v1.0 | Developed by @NerdsAndDragons#2817"
-thumb <image> -color <color>
