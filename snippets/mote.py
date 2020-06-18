!snippet mote {{c = 'Star-like Motes'}}
{{create_cc_nx(c, 0, 7, "none", "bubble") if not cc_exists(c) else ''}}
{{v = get_cc(c) > 0}}
{{(mod_cc(c, -1)) if v else ''}}
{{f'-phrase "{"Using a mote"} ({get_cc(c)} remaining)"'}}{{"" if v else delete_cc(c)}}{{"" if v else combat().me.remove_effect("crown")}}