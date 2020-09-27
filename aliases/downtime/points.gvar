{{d, a, g, s = "Downtime Points", &ARGS& , load_json(get_gvar("5ac2cafb-291c-4c00-b29a-074eb4bf31b4")), get_raw().skills}}
{{cT, cR, cP, B, il = ["cp", "sp", "ep", "gp", "pp"], {"cp": 100, "sp": 10, "ep": 2, "gp": 1, "pp": 0.1}, "Coin Pouch", load_json(bags), "|inline"}}
{{P = ([x for x in B if x[0] == cP]+[[]])[0]}}
{{error = P == []}}
{{error or P[1].update({"gp": P[1].gp-50})}}
{{error or [(set("y", cT[cT.index(x)+1]), set("R", int(cR[x]/cR[y])), set("p", P[1][x]//R),(P[1].update({y: P[1][y]+p}), P[1].update({x: P[1][x]-p*R}))if P[1][x] < 0 else'')for x in cT[:-1]]}}
{{error = [x for x in P[1]if P[1][x] < 0]}}
{{error or set_cvar("bags", dump_json(B))}}
{{error and err(g.err.noMoney)}}
{{mod_cc(d, +5)}}
{{args = argparse(a)}}
-title "<name> spends 50gp and regains 5 Downtime Points. Spend them wisely!"
-f "{{d}} (+5)|{{cc_str(d)+il}}"
-f "{{cP}}|{{'\n'.join([f'{P[1][x]:,} '+x for x in P[1]])+il}}"
