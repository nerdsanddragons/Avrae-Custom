#steal
{{d, a, g, s = "Downtime Points", @ , load_json(get_gvar("5ac2cafb-291c-4c00-b29a-074eb4bf31b4")), get_raw().skills}}
{{get_cc(d) or err(g.err.tooFewDT)}}
{{ste=get_raw().skills.stealth+roll('1d20')}}
{{sle=get_raw().skills.sleightOfHand+roll('1d20')}}
{{per=get_raw().skills.perception+roll('1d20')}}
{{dc1=roll('2d4+8')}}{{dc2=roll('2d4+8')}}{{dc3=roll('2d4+8')}}
{{suc=(0 if dc1 > ste else 1) + (0 if dc2 > sle else 1) + (0 if dc3 > per else 1)}}
{{rew=roll('8d4')}}
{{fate=roll('1d3') - 1}}
{{fail=2 if suc > fate else 1}}
{{total=rew * suc if fail==2 else 0}}
{{jail=roll('1d4')*10}}
{{cT, cR, cP, B, il = ["cp", "sp", "ep", "gp", "pp"], {"cp": 100, "sp": 10, "ep": 2, "gp": 1, "pp": 0.1}, "Coin Pouch", load_json(bags), "|inline"}}
{{P = ([x for x in B if x[0] == cP]+[[]])[0]}}
{{error = P == []}}
{{error or P[1].update({"gp": P[1].gp+(total)}) if fail==2 else P[1].update({"gp": P[1].gp-(jail)})}}
{{error or [(set("y", cT[cT.index(x)+1]), set("R", int(cR[x]/cR[y])), set("p", P[1][x]//R),(P[1].update({y: P[1][y]+p}), P[1].update({x: P[1][x]-p*R}))if P[1][x] < 0 else'')for x in cT[:-1]]}}
{{error = [x for x in P[1]if P[1][x] < 0]}}
{{error or set_cvar("bags", dump_json(B))}}
{{error and err(g.err.noMoney)}}
{{mod_cc(d, -1)}}
{{args = argparse(a)}}
-title "**Downtime Activity: Stealing from Nobles!**"
{{res=f"**{name}** attempts to steal!\n\nYou keep an eye out for any guards! (DC {dc3})\n**Perception:** {per}\n\nYou sneak around trying not to be noticed by the guards! (DC {dc1})\n**Stealth:** {ste}\n\nYou try to pickpocket some gold! (DC {dc2})\n**Sleight of Hand:** {sle}\n\n{'**Success!** You steal the gold! You gain **' + str(total) + 'gp**' if fail==2 else 'You **failed** and got caught by the guards! They bring you to jail and you must now spend **' + str(jail) + 'gp** for bail.'}"}}
-f "{{res}}"
-f "{{d}} (-1)|{{cc_str(d)+il}}"
-f "{{cP}}|{{'\n'.join([f'{P[1][x]:,} '+x for x in P[1]])+il}}"
