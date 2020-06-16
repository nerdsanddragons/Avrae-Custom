!alias dt tembed {{d, g, o, p, h, = "Downtime Points", load_json(get_gvar("03de1c2a-db68-4835-87aa-24b71c26e9b2")), "&1&".lower(), "%2%".lower(), "help" in "&1&" }}
{{j = load_json(get_gvar("5ac2cafb-291c-4c00-b29a-074eb4bf31b4"))}}
{{cc_exists(d) or create_cc("Downtime Points", 0, 5, "none", "bubble")}}
{{o=[x for x in ["feat","skill","lang","tool","magic","scroll","hired","fight","steal","points"] if "&1&".lower() in x]}}
{{p=[x for x in ["help"] if "&2&".lower() in x]}}
{{get_gvar(g[o[0]]).replace("@",  str(o+&ARGS&[1:])) if o else ""}}
{{get_gvar(j[p[0]]).replace("@",  str(p+&ARGS&[1:])) if p else ""}}
{{D = get_cc(d)}}
-desc "{{get_gvar(g.help) if h else get_gvar(j.help[o]) if p else get_gvar(g.main) if not o else ''}}"
-footer "!dt help | v1.0 | Developed by @NerdsAndDragons#2817"
-thumb <image> -color <color>
