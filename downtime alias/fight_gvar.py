#fight
{{d, a, g, s = "Downtime Points", @ , load_json(get_gvar("5ac2cafb-291c-4c00-b29a-074eb4bf31b4")), get_raw().skills}}
{{get_cc(d) or err(g.err.tooFewDT)}}
{{ath=get_raw().skills.athletics+roll('1d20')}}
{{acr=get_raw().skills.acrobatics+roll('1d20')}}
{{ins=get_raw().skills.insight+roll('1d20')}}
{{dc1=roll('1d10+5')}}
{{dc2=roll('1d10+5')}}
{{dc3=roll('1d10+5')}}
{{suc=(0 if dc1 > ath else 1)+(0 if dc2 > acr else 1)+(0 if dc3 > ins else 1)}}
{{prize=[0,50,100,200]}}
{{gold = prize[suc]}}
{{cT, cR, cP, B, il = ["cp", "sp", "ep", "gp", "pp"], {"cp": 100, "sp": 10, "ep": 2, "gp": 1, "pp": 0.1}, "Coin Pouch", load_json(bags), "|inline"}}
{{P = ([x for x in B if x[0] == cP]+[[]])[0]}}
{{error = P == []}}
{{error or P[1].update({"gp": P[1].gp-50+(gold)})}}
{{error or [(set("y", cT[cT.index(x)+1]), set("R", int(cR[x]/cR[y])), set("p", P[1][x]//R),(P[1].update({y: P[1][y]+p}), P[1].update({x: P[1][x]-p*R}))if P[1][x] < 0 else'')for x in cT[:-1]]}}
{{error = [x for x in P[1]if P[1][x] < 0]}}
{{error or set_cvar("bags", dump_json(B))}}
{{error and err(g.err.noMoney)}}
{{mod_cc(d, -1)}}
-title "**Downtime Activity: Fighting Arena**"
-f "Fighting Arena | This downtime activity covers boxing, wrestling, and other nonlethal forms of combat."
-f "Resolution| The character makes three checks: Strength (Athletics), Dexterity (Acrobatics), and Wisdom (Insight). The DC is 5 + 1d10, generating a separate DC for each check. Consult the Fighting Arena Results table to see how the character does."
{{f' -f "Round 1| The first opponent rolls {dc1}, {name} rolls {ath} for their athletics check"'}}
{{f' -f "Round 2| The second opponent rolls {dc2}, {name} rolls {acr} for their acrobatics check"'}}
{{f' -f "Round 3| The third opponent rolls {dc3}, {name} rolls {ins} for their insight check"'}}
{{f' -f "Description | {name} fights in the fighting arena and wins {suc} rounds and comes away with {gold} gp."'}}
-f "{{d}} (-1)|{{cc_str(d)+il}}"
-f "{{cP}}|{{'\n'.join([f'{P[1][x]:,} '+x for x in P[1]])+il}}"
