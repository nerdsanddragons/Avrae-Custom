#feat
{{d, a, g, s = "Downtime Points", "&1&", load_json(get_gvar("5ac2cafb-291c-4c00-b29a-074eb4bf31b4")), get_raw().skills}}
{{get_cc(d) or err(g.err.tooFewDT)}}
{{cT, cR, cP, B, il = ["cp", "sp", "ep", "gp", "pp"], {"cp": 100, "sp": 10, "ep": 2, "gp": 1, "pp": 0.1}, "Coin Pouch", load_json(bags), "|inline"}}
{{P = ([x for x in B if x[0] == cP]+[[]])[0]}}
{{error = P == []}}
{{error or P[1].update({"gp": P[1].gp-100})}}
{{error or [(set("y", cT[cT.index(x)+1]), set("R", int(cR[x]/cR[y])), set("p", P[1][x]//R),(P[1].update({y: P[1][y]+p}), P[1].update({x: P[1][x]-p*R}))if P[1][x] < 0 else'')for x in cT[:-1]]}}
{{error = [x for x in P[1]if P[1][x] < 0]}}
{{error or set_cvar("bags", dump_json(B))}}
{{error and err(g.err.noMoney)}}
{{mod_cc(d, -1)}}
{{args = argparse(a)}}
{{f =[x for x in g.feats if a[1].title() in x] if len(a)>1 else []}}
{{cc = "Feat Progress: "+f[0] if f else err(g.err.notFoundFeat+f"{', '.join([x for x in g.feats])}.")}}
{{f = f[0]}}
{{isNew = not cc_exists(cc)}}
{{create_cc_nx(cc, 0, 30)}}
{{set_cc(cc, 0) if isNew else ""}}
{{dice = ['1d20', '2d20kh1', '2d20kl1'][args.adv()]}}
{{ss = g.feats[f]}}
{{mod = max([s[x] for x in s if x in ss]+[0])}}
{{S = [x for x in ss if s[x] == mod][0] if ss else ""}}
{{b = "+".join(args.get('b'))}}
{{ch, dc = vroll(f"{dice}+{mod}{'+'+b if b else ''}"), 18}}
{{c = ch.result.crit == 1}}
{{r = (ch.total >= dc)+2*c}}
{{mod_cc(cc, r) if r else ""}}
-title "<name> uses 1 Downtime Point and spends 100gp to attempt a{{('n ' if S[0] in 'aeiou' else ' ')+S.title() if S else ''}} check towards learning the {{f}} feat!"
-f "DC:18|{{ch}}{{il}}"
-f "{{d}} (-1)|{{cc_str(d)+il}}"
-f "{{cc}} {{f"(+{r})" if r else ''}}|{{cc_str(cc)+(f"\nYou have completed your training and gained the {f} feat!" if get_cc(cc)>=30 else "")+il}}"
-f "{{cP}}|{{'\n'.join([f'{P[1][x]:,} '+x for x in P[1]])+il}}"
-f "{{("Critical " if c else "")+"Success" if r else "Failure"}}!"
